#!/usr/bin/env python3

""""Cache class for Redis"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    '''Tracks the number of calls made to a method in a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Invokes the given method after incrementing its call counter.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    '''Tracks the call details of a method in a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Returns the method's output after storing its inputs and output.
        '''
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(fn: Callable) -> None:
    '''Displays the call history of a Cache class' method.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    func_name = fn.__qualname__
    in_key = '{}:inputs'.format(func_name)
    out_key = '{}:outputs'.format(func_name)
    fxn_call_count = 0
    if redis_store.exists(func_name) != 0:
        fxn_call_count = int(redis_store.get(func_name))
    print('{} was called {} times:'.format(func_name, fxn_call_count))
    func_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(func_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            func_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


class Cache:
    """Redis cache class"""

    def __init__(self) -> None:
        """Initializes the Redis cache"""
        self._redis = redis.Redis()
        # Flush instance
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store input data and return the key"""
        key: uuid.UUID = uuid.uuid4()
        key: str = str(key)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> None:
        """Gets data from the cache and optionally converts
            back to desired format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str):
        """Gets a string from the cache"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str):
        """Gets a integer from the cache"""
        return self.get(key, lambda x: int(x))

#!/usr/bin/env python3

"""expiring web cache and tracker"""
import requests
import redis
from functools import wraps
from typing import Callable

store = redis.Redis()


def url_data_cache(method: Callable) -> Callable:
    """Caches data fetched from url"""
    @wraps(method)
    def invoker(url) -> str:
        store.incr(f'count:{url}')
        value = store.get(f'data:{url}')
        if value:
            return value.decode('utf-8')
        value = method(url)
        store.set(f'count:{url}', 0)
        store.setex(f'data:{url}', 10, value)
        return value
    return invoker


@url_data_cache
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL and returns it."""
    requests.get(url).text

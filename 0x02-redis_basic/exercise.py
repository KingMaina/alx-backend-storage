#!/usr/bin/env python3

""""Cache class for Redis"""
import redis
import uuid
from typing import Union

class Cache:
    """Redis cache class"""

    def __init__(self):
        self._redis = redis.Redis()
        # Flush instance
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store input data and return the key"""
        key: uuid.UUID = uuid.uuid4()
        # self._redis.save()
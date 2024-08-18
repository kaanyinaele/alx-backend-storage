#!/usr/bin/env python3
"""
This module defines a Cache class with a method call counter using Redis.
"""
import redis
import uuid
from typing import Union, Callable
import functools

def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of calls to a method.

    Args:
        method: The method to be decorated.

    Returns:
        A wrapped function that increments a Redis counter each time the method is called.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to increment the call count in Redis."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis with a randomly generated key.

        Args:
            data: The data to be stored in Redis. It can be a str, bytes, int, or float.

        Returns:
            The randomly generated key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: The key of the data to retrieve.
            fn: A callable to convert the data to the desired format.

        Returns:
            The data stored in Redis, potentially converted by fn, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve a string from Redis."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve an integer from Redis."""
        return self.get(key, fn=int)


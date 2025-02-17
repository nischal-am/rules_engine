"""
This module defines a CacheFactory class that provides a method to create different types of cache instances
based on the provided cache type. It supports Redis, LRU, and NoCache implementations.
"""
import redis
from config import REDIS_CONFIG
from rules.rule_cache.lru_cache import LRUCache
from rules.rule_cache.no_cache import NoCache
from rules.rule_cache.redis_cache import RedisCache
from rules.models.cache_types import CacheType


class CacheFactory:
    """Factory for selecting the appropriate cache implementation."""
    
    @staticmethod
    def create_cache(cache_type : CacheType):
        if cache_type == CacheType.REDIS:
            return RedisCache(redis.Redis(**REDIS_CONFIG, decode_responses=True))
        elif cache_type == CacheType.LRU:
            return LRUCache()
        elif cache_type == CacheType.NOCACHE:
            return NoCache()
        else:
            raise ValueError(f"Invalid cache type: {cache_type}")

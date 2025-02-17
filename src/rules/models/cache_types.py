"""
Enumerator for available cache types.

Attributes:
    LRU (str): Least Recently Used cache type.
    REDIS (str): Redis cache type.
    NOCACHE (str): No cache type.
"""

from enum import Enum

class CacheType(Enum):
    """Enumerator for available cache types."""
    LRU = "lru"
    REDIS = "redis"
    NOCACHE = "nocache"

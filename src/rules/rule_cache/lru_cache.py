"""
LRUCache is a class that implements a Least Recently Used (LRU) cache mechanism.

Methods:
    get_cached_rules():
        Retrieves cached rules. This method is decorated with @lru_cache with a max size of 5.
        Returns:
            None: This method currently returns None.
    
    set_cached_rules(rules):
        Sets the cached rules. If there are existing cached rules, it clears the cache before setting new rules.
        Args:
            rules: The rules to be cached.
    
    clear_cache():
        Clears the entire cache.
"""
from functools import lru_cache
from rules.rule_cache.cache_base import CacheBase

class LRUCache(CacheBase):
    """LRU Cache Implementation."""

    @staticmethod
    @lru_cache(maxsize=5)
    def get_cached_rules():
        return None  

    @staticmethod
    def set_cached_rules(rules):
        if LRUCache.get_cached_rules is not None:
            LRUCache.get_cached_rules.cache_clear()
        LRUCache.get_cached_rules = staticmethod(lambda: rules)

    @staticmethod
    def clear_cache():
        LRUCache.get_cached_rules.cache_clear()

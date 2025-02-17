# This file contains the NoCache class which is a no op cache implementation.
from rules.rule_cache.cache_base import CacheBase

class NoCache(CacheBase):
    """A no op Cache Implementation."""

    @staticmethod
    def get_cached_rules():
        return None  

    @staticmethod
    def set_cached_rules(rules):
        return

    @staticmethod
    def clear_cache():
        return

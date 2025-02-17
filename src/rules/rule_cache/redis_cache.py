import redis
import json
from rules.rule_cache.cache_base import CacheBase

class RedisCache(CacheBase):
    """Redis Cache Implementation."""

    def __init__(self, redis_client: redis.Redis):
        self.client = redis_client

    def get_cached_rules(self):
        cached_rules = self.client.get("rules_cache")
        return json.loads(cached_rules) if cached_rules else None

    def set_cached_rules(self, rules):
        self.client.setex("rules_cache", 3600, json.dumps(rules))

    def clear_cache(self):
        self.client.delete("rules_cache")

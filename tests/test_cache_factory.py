from rules.models.cache_factory import CacheFactory
from rules.rule_cache.lru_cache import LRUCache
from rules.rule_cache.redis_cache import RedisCache
from rules.models.cache_types import CacheType

def test_cache_factory_lru():
    """Test if CacheFactory returns LRU cache when LRU is selected."""
    cache = CacheFactory.create_cache(CacheType.LRU)
    assert isinstance(cache, LRUCache)

def test_cache_factory_redis(monkeypatch):
    """Test if CacheFactory returns Redis cache when Redis is selected."""
    monkeypatch.setattr("config.CACHE_TYPE", CacheType.REDIS)
    cache = CacheFactory.create_cache(CacheType.REDIS)
    assert isinstance(cache, RedisCache)

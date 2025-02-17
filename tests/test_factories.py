from rules.models.rule_factory import RuleEngineFactory
from rules.models.storage_factory import RuleStorageFactory
from rules.models.cache_factory import CacheFactory
from rules.models.cache_types import CacheType
from rules.models.rule_types import RuleEngineType
from rules.models.storage_types import RuleStorageType


def test_rule_engine_factory():
    cache = CacheFactory.create_cache(CacheType.LRU)
    storage = RuleStorageFactory.create_storage(RuleStorageType.FILE)
    engine = RuleEngineFactory.create_rule_engine(RuleEngineType.BUSINESS, cache, storage)
    assert engine is not None

def test_rule_storage_factory():
    storage = RuleStorageFactory.create_storage(RuleStorageType.FILE)
    assert storage is not None

def test_cache_factory_lru(monkeypatch):
    monkeypatch.setattr("config.CACHE_TYPE", CacheType.LRU)
    cache = CacheFactory.create_cache(CacheType.LRU)
    assert cache is not None

def test_cache_factory_redis(monkeypatch):
    monkeypatch.setattr("config.CACHE_TYPE", CacheType.REDIS)
    cache = CacheFactory.create_cache(CacheType.REDIS)
    assert cache is not None

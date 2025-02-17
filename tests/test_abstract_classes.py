import pytest
from rules.rule_base import RuleEngineBase
from rules.storage.storage_base import RuleStorageBase
from rules.rule_cache.cache_base import CacheBase

def test_abstract_class_instantiation():
    with pytest.raises(TypeError):
        RuleEngineBase()

    with pytest.raises(TypeError):
        RuleStorageBase()

    with pytest.raises(TypeError):
        CacheBase()

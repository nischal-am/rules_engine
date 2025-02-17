import pytest
from rules.models.rule_types import RuleEngineType
from rules.models.storage_types import RuleStorageType

def test_enum_values():
    assert RuleEngineType.BUSINESS.value == "business-rules"

    assert RuleStorageType.FILE.value == "file"
    assert RuleStorageType.DATABASE.value == "database"

def test_invalid_rule_engine_type():
    with pytest.raises(ValueError):
        RuleEngineType("invalid-engine")

def test_invalid_rule_storage_type():
    with pytest.raises(ValueError):
        RuleStorageType("invalid-storage")

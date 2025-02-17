import pytest
from rules.business_rules import BusinessRulesEngine
from rules.rule_cache.lru_cache import LRUCache
from rules.storage.file_storage import FileRuleStorage
from rules.rule_actions import RuleActions


@pytest.fixture
def mock_cache():
    return LRUCache()

@pytest.fixture
def mock_storage():
    return FileRuleStorage()

@pytest.fixture
def sample_input_data():
    """Mock input data that meets the rule conditions."""
    return {
        "transaction_amount": 8000,
        "funding_type": "instant-funding"
    }

@pytest.fixture
def sample_dynamic_params():
    """Mock dynamic params data that are used for evaluating the rule conditions."""
    return {
        "threshold_amount": 2500
    }

def test_business_rules_fetch_file_lru_cache(mock_cache, mock_storage):
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)

    #cached_rules = rule_engine.cache.get_cached_rules()
    #assert cached_rules is None  # Cache should be empty

    print(rule_engine.fetch_rules())
    assert isinstance(rule_engine.fetch_rules(), list)  # Should return a list

    cached_rules = rule_engine.cache.get_cached_rules()
    assert isinstance(cached_rules, list)  # Should return a list

def test_business_rules_evaluate_file_lru_cache(mock_cache, mock_storage, sample_input_data, sample_dynamic_params):
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)

    actions = RuleActions()

    cached_rules = rule_engine.cache.get_cached_rules()
    assert isinstance(cached_rules, list)  # Should return a list

    results = rule_engine.evaluate_rules(sample_input_data, sample_dynamic_params)
    assert isinstance(results, dict)  # Should return a dictionary

    actions.results = results["triggered_rules"]
    assert isinstance(actions.results, list)  # Should return a list

    assert len(actions.results) > 0  # Some should be triggered
    # Validate expected action was triggered
    expected_result = [{"action": "boolean_trigger", "result": True}]
    assert actions.results == expected_result
    assert any(action["action"] == "boolean_trigger" for action in actions.results)

    

def test_business_rules_fetch_file_global_lru_cache(mock_cache, mock_storage):
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)

    cached_rules = rule_engine.cache.get_cached_rules()
    assert isinstance(cached_rules, list)  # Should return a list

def test_business_rules_evaluate_file_lru_cache_no_trigger(mock_cache, mock_storage, sample_dynamic_params):
    transaction_data = {"transaction_amount": 2000, "funding_type": "instant-funding"}
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)

    actions = RuleActions()

    cached_rules = rule_engine.cache.get_cached_rules()
    assert isinstance(cached_rules, list)  # Should return a list

    results = rule_engine.evaluate_rules(transaction_data, sample_dynamic_params)
    assert isinstance(results, dict)  # Should return a dictionary

    actions.results = results["triggered_rules"]
    assert isinstance(actions.results, list)  # Should return a list

    assert len(actions.results) == 0  # No rules should be triggered
    # Validate expected action was triggered
    expected_result = []
    assert actions.results == expected_result
    assert not any(action["action"] == "boolean_trigger" for action in actions.results)


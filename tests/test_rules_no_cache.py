import pytest
from rules.business_rules import BusinessRulesEngine
from rules.rule_cache.no_cache import NoCache
from rules.storage.file_storage import FileRuleStorage
from rules.rule_actions import RuleActions


@pytest.fixture
def mock_cache():
    return NoCache()

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

def test_business_rules_fetch_file_no_cache(mock_cache, mock_storage):
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)
    print(rule_engine.fetch_rules())
    assert isinstance(rule_engine.fetch_rules(), list)  # Should return a list

def test_business_rules_evaluate_file_no_cache(mock_cache, mock_storage, sample_input_data, sample_dynamic_params):
    rule_engine = BusinessRulesEngine(mock_cache, mock_storage)

    actions = RuleActions()

    rule_list = rule_engine.fetch_rules()
    assert isinstance(rule_list, list)  # Should return a list

    results = rule_engine.evaluate_rules(sample_input_data, sample_dynamic_params)
    assert isinstance(results, dict)  # Should return a dictionary

    actions.results = results["triggered_rules"]
    assert isinstance(actions.results, list)  # Should return a list

    assert len(actions.results) > 0  # Some should be triggered
    # Validate expected action was triggered
    expected_result = [{"action": "boolean_trigger", "result": True}]
    assert actions.results == expected_result
    assert any(action["action"] == "boolean_trigger" for action in actions.results)


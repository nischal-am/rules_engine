import pytest
from business_rules import engine
from rules.rule_variables import RuleVariables
from rules.rule_actions import RuleActions

@pytest.fixture
def sample_rules():
    """Mock rule set that triggers a boolean return of true if transaction_amount > threshold_amount and funding_type is instant-funding."""
    return [
        {
            "conditions": {
                "all": [
                {
                    "name": "transaction_amount",
                    "operator": "greater_than",
                    "value": "threshold_amount"
                },
                {
                    "name": "funding_type",
                    "operator": "equal_to_case_insensitive",
                    "value": "instant-funding"
                }
            ]
        },
            "actions": [
                {
                    "name": "boolean_trigger"
                }
            ]
        }
    ]  # ✅ Ensure this is a list

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

def test_rule_evaluation(sample_rules, sample_input_data, sample_dynamic_params):
    """Test if Business Rules Engine applies a discount correctly."""
    
    # Initialize Variables and Actions
    variables = RuleVariables(sample_input_data, sample_dynamic_params)
    actions = RuleActions()

    # ✅ FIX: Iterate over the list and pass one rule at a time
    for rule in sample_rules:
        for condition in rule["conditions"].get("all", []):
                if isinstance(condition["value"], str) and condition["value"] in sample_dynamic_params:
                    condition["value"] = sample_dynamic_params[condition["value"]]  # ✅ Convert string to numeric value
        engine.run(rule, variables, actions)

    # Validate expected action was triggered
    expected_result = [{"action": "boolean_trigger", "result": True}]
    assert actions.results == expected_result

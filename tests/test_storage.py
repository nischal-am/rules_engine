import pytest
from rules.storage.file_storage import FileRuleStorage
from rules.storage.db_storage import DBRuleStorage

@pytest.fixture
def mock_file_storage():
    return FileRuleStorage()

@pytest.fixture
def sample_rules():
    """Mock rule set that triggers a boolean return of true if transaction_amount > threshold_amount and funding_type is instant-funding.."""
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

def test_file_storage_initial(mock_file_storage):
    assert isinstance(mock_file_storage.fetch_rules(), list)

@pytest.fixture
def mock_db_storage():
    return DBRuleStorage()

def test_db_storage_initial(mock_db_storage):
    assert isinstance(mock_db_storage.fetch_rules(), list)

def test_db_storage_add_rule(sample_rules, mock_db_storage):

    rules = mock_db_storage.fetch_rules()
    if rules:
        return
    # only add rules in test cases if there are none in the database
    for rule in sample_rules:
        mock_db_storage.add_rule(rule)

    rules = mock_db_storage.fetch_rules()
    assert isinstance(rules, list)

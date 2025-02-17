import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

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

def test_get_rules():
    """Test retrieving rules from API."""
    response = client.get("/rules")
    assert response.status_code == 200
    assert "rules" in response.json()

def test_evaluate_rules():
    """Test rule evaluation endpoint."""
    test_data = {"transaction_amount": 2500, "funding_type": "instant-funding"}
    test_dynamic_params = {"threshold_amount": 2500}
    payload = {"transaction_data": test_data, "dynamic_params": test_dynamic_params}
    response = client.post("/evaluate", json=payload)

    assert response.status_code == 200
    assert "triggered_rules" in response.json()


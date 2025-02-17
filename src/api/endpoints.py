"""
This module defines the API endpoints for the rules engine.

Endpoints:
- GET /rules: Fetch all rules from the rule engine.
- POST /evaluate: Evaluate input data against the rules in the rule engine.
- POST /rules: Create a new rule and add it to the rule engine.

Dependencies:
- FastAPI: Used to create the API router and define endpoints.
- config: Contains configuration constants for cache, rule storage, and rule engine types.
- rules.models.models: Contains the RuleCreate model used for creating new rules.
- rules.models.rule_factory: Contains the RuleEngineFactory for creating rule engine instances.
- rules.models.storage_factory: Contains the RuleStorageFactory for creating rule storage instances.
- rules.models.cache_factory: Contains the CacheFactory for creating cache instances.

Attributes:
- cache: Cache instance created based on the CACHE_TYPE configuration {config.py}.
- storage: Rule storage instance created based on the RULE_STORAGE_TYPE configuration {config.py}.
- rule_engine: Rule engine instance created based on the RULE_ENGINE_TYPE configuration  {config.py}, using the cache and storage instances.
- router: FastAPI APIRouter instance for defining API endpoints.

Functions:
- get_rules: Endpoint to fetch all rules from the rule engine.
- evaluate_rules: Endpoint to evaluate input data against the rules in the rule engine.
- create_rule: Endpoint to create a new rule and add it to the rule engine.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Any
from config import CACHE_TYPE, RULE_STORAGE_TYPE, RULE_ENGINE_TYPE
from rules.models.rule import RuleCreate
from rules.models.rule_factory import RuleEngineFactory
from rules.models.storage_factory import RuleStorageFactory
from rules.models.cache_factory import CacheFactory

class TransactionData(BaseModel):
    transaction_data: Dict[str, Any]  # ✅ Example: {"transaction_amount": 750}
    dynamic_params: Dict[str, Any]    # ✅ Example: {"threshold_1": 500, "threshold_2": 1000}


cache = CacheFactory.create_cache(CACHE_TYPE)
storage = RuleStorageFactory.create_storage(RULE_STORAGE_TYPE)
rule_engine = RuleEngineFactory.create_rule_engine(RULE_ENGINE_TYPE, cache, storage)

router = APIRouter()

@router.get("/rules")
def get_rules():
    return {"rules": rule_engine.fetch_rules()}

@router.post("/evaluate")
def evaluate_rules(payload: TransactionData):
    return {"triggered_rules": rule_engine.evaluate_rules(payload.transaction_data, payload.dynamic_params)}

@router.post("/rules")
def create_rule(rule: RuleCreate):
    rule_engine.add_rule(rule.conditions, rule.actions)
    rule_engine.cache.clear_cache()
    return {"message": "Rule added successfully", "rule": rule}


"""
Factory for selecting the appropriate Rule Engine.
This module provides a factory class `RuleEngineFactory` that is responsible for creating instances of different rule engines based on the provided type. It supports the creation of a `BusinessRulesEngine` and can be extended to support other types of rule engines.
Classes:
    RuleEngineFactory: A factory class for creating rule engine instances.
Methods:
    create_rule_engine(rules_engine_type: RuleEngineType, cache: CacheBase, storage: RuleStorageBase):
        Creates and returns an instance of the appropriate rule engine based on the provided type.
        Args:
            rules_engine_type (RuleEngineType): The type of rule engine to create.
            cache (CacheBase): The cache instance to be used by the rule engine.
            storage (RuleStorageBase): The storage instance to be used by the rule engine.
        Returns:
            An instance of the appropriate rule engine.
        Raises:
            ValueError: If an invalid rule engine type is provided.
"""
from rules.business_rules import BusinessRulesEngine
from rules.models.rule_types import RuleEngineType
from rules.storage.storage_base import RuleStorageBase
from rules.rule_cache.cache_base import CacheBase

class RuleEngineFactory:
    """Factory for selecting the appropriate Rule Engine."""
    
    @staticmethod
    def create_rule_engine(rules_engine_type : RuleEngineType, cache : CacheBase, storage : RuleStorageBase):
        if rules_engine_type == RuleEngineType.BUSINESS:
            return BusinessRulesEngine(cache, storage)
        else:
            raise ValueError(f"Invalid rule engine type: {rules_engine_type}")

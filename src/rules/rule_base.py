from abc import ABC, abstractmethod
from rules.rule_cache.cache_base import CacheBase
from rules.storage.storage_base import RuleStorageBase


class RuleEngineBase(ABC):
    """Abstract base class for rule engines. Cannot be instantiated."""

    def __init__(self, cache : CacheBase, storage: RuleStorageBase):
        if isinstance(type(self), RuleEngineBase):
            raise TypeError("Cannot instantiate abstract class RuleEngineBase directly.")
        self.cache = cache
        self.storage = storage

    @abstractmethod
    def fetch_rules(self):
        pass

    @abstractmethod
    def add_rule(self, conditions, actions):
        pass

    @abstractmethod
    def evaluate_rules(self, input_data, dynamic_params):
        pass

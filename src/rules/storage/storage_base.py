from abc import ABC, abstractmethod

class RuleStorageBase(ABC):
    """Abstract base class for rule storage implementations. Cannot be instantiated."""

    def __init__(self):
        if isinstance(type(self), RuleStorageBase):
            raise TypeError("Cannot instantiate abstract class RuleStorageBase directly.")

    @abstractmethod
    def fetch_rules(self):
        pass

    @abstractmethod
    def add_rule(self, rule):
        pass

    @abstractmethod
    def clear_rules(self):
        pass

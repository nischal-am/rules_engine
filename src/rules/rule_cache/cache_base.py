"""
Abstract base class for cache implementations. This class cannot be instantiated directly.

Methods
-------
get_cached_rules():
    Abstract method to retrieve cached rules. Must be implemented by subclasses.

set_cached_rules(rules):
    Abstract method to set cached rules. Must be implemented by subclasses.

clear_cache():
    Abstract method to clear the cache. Must be implemented by subclasses.
"""
from abc import ABC, abstractmethod

class CacheBase(ABC):
    """Abstract base class for cache implementations. Cannot be instantiated."""

    def __init__(self):
        if isinstance(type(self), CacheBase):
            raise TypeError("Cannot instantiate abstract class CacheBase directly.")

    @abstractmethod
    def get_cached_rules(self):
        pass

    @abstractmethod
    def set_cached_rules(self, rules):
        pass

    @abstractmethod
    def clear_cache(self):
        pass

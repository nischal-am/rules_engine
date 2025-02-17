"""
Enumerator for available rule storage types.

Attributes:
    FILE (str): Represents storage type as a file.
    DATABASE (str): Represents storage type as a database.
"""
from enum import Enum

class RuleStorageType(Enum):
    """Enumerator for available rule storage types."""
    FILE = "file"
    DATABASE = "database"
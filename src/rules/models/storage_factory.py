"""
RuleStorageFactory is a factory class responsible for creating instances of rule storage implementations based on the specified storage type.

Methods:
    create_storage(storage_type: RuleStorageType):
        Creates and returns an instance of a rule storage implementation based on the provided storage type.
        Args:
            storage_type (RuleStorageType): The type of storage to create (e.g., DATABASE, FILE).
        Returns:
            An instance of the corresponding rule storage implementation.
        Raises:
            ValueError: If an invalid storage type is provided.
"""
from rules.storage.file_storage import FileRuleStorage
from rules.storage.db_storage import DBRuleStorage
from rules.models.storage_types import RuleStorageType

class RuleStorageFactory:
    """Factory for selecting rule storage implementation."""

    @staticmethod
    def create_storage(storage_type : RuleStorageType):
        if storage_type == RuleStorageType.DATABASE:
            return DBRuleStorage()
        elif storage_type == RuleStorageType.FILE:
            return FileRuleStorage()
        else:
            raise ValueError(f"Invalid rule storage type: {storage_type}")

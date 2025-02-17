from rules.models.cache_types import CacheType
from rules.models.rule_types import RuleEngineType
from rules.models.storage_types import RuleStorageType

# Cache Type
CACHE_TYPE = CacheType.LRU  # Change to CacheType.REDIS for Redis

# Rule Engine Type
RULE_ENGINE_TYPE = RuleEngineType.BUSINESS  # Change to DURABLE or PYKE

# Rule Storage Type
RULE_STORAGE_TYPE = RuleStorageType.FILE  # Change to DATABASE for PostgreSQL

DB_CONFIG = {
    "dbname": "rules_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432
}

RULES_FILE_PATHS = {
    RuleEngineType.BUSINESS : "rules_json/business_rules.json"
}

REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "db": 0
}
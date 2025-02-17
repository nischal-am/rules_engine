import json
import psycopg2
from config import DB_CONFIG, RULE_ENGINE_TYPE
from rules.storage.storage_base import RuleStorageBase

class DBRuleStorage(RuleStorageBase):
    def __init__(self):
        self.conn = psycopg2.connect(**DB_CONFIG)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS rules (
                id SERIAL PRIMARY KEY,
                engine TEXT NOT NULL,
                rule_data JSONB NOT NULL
            )
        """)
        self.conn.commit()
        cursor.close()

    def fetch_rules(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT rule_data FROM rules WHERE engine=%s", (RULE_ENGINE_TYPE.value,))
    
        rules = []
        for row in cursor.fetchall():
            rule = json.loads(row[0]) if isinstance(row[0], str) else row[0]  # ✅ Ensure it's parsed
            if isinstance(rule["conditions"], str):
                rule["conditions"] = json.loads(rule["conditions"])  # ✅ Ensure `conditions` is a dictionary
            rules.append(rule)
            
        cursor.close()
        return rules

    def add_rule(self, rule):
        cursor = self.conn.cursor()
        # ✅ Ensure conditions is a valid dictionary, not a raw string
        rule["conditions"] = json.loads(rule["conditions"]) if isinstance(rule["conditions"], str) else rule["conditions"]
    
        cursor.execute("INSERT INTO rules (engine, rule_data) VALUES (%s, %s)",
                   (RULE_ENGINE_TYPE.value, json.dumps(rule)))  # ✅ Store as JSON
        self.conn.commit()
        cursor.close()

    def clear_rules(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM rules WHERE engine=%s", (RULE_ENGINE_TYPE.value,))
        self.conn.commit()
        cursor.close()

import json
import os
from config import RULES_FILE_PATHS, RULE_ENGINE_TYPE
from rules.storage.storage_base import RuleStorageBase

class FileRuleStorage(RuleStorageBase):
    def __init__(self):
        """Loads rules from an external JSON file in the script's directory."""
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
        print(f"Debug: script_dir: {script_dir}")
        self.file_path = os.path.join(script_dir, RULES_FILE_PATHS[RULE_ENGINE_TYPE])  # Construct full path
        print(f"Debug: file_path: {self.file_path}")

    def fetch_rules(self):
        if not os.path.exists(self.file_path):
            print(f"File not found: {self.file_path}")
            return []
        
        with open(self.file_path, "r") as file:
            return json.load(file)

    def add_rule(self, rule):
        rules = self.fetch_rules()
        rules.append(rule)

        with open(self.file_path, "w") as file:
            json.dump(rules, file, indent=4)

    def clear_rules(self):
        with open(self.file_path, "w") as file:
            json.dump([], file)

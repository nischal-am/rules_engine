# This file contains the implementation of the Business Rules Engine. 
# The BusinessRulesEngine class is a subclass of RuleEngineBase and implements the fetch_rules, add_rule, and evaluate_rules methods. 
# The fetch_rules method retrieves the rules from the cache if they are available; otherwise, it fetches them from the storage and caches them. 
# sThe add_rule method adds a new rule to the storage. The evaluate_rules method evaluates the input data against the rules and returns the triggered rules.
from business_rules import engine
from rules.rule_base import RuleEngineBase
from rules.rule_variables import RuleVariables
from rules.rule_actions import RuleActions

class BusinessRulesEngine(RuleEngineBase):

    def fetch_rules(self):
        cached_rules = self.cache.get_cached_rules()
        if cached_rules:
            print("Fetching rules from cache")
            return cached_rules
        print("Fetching rules from storage")
        rules = self.storage.fetch_rules()
        
        self.cache.set_cached_rules(rules)
        return rules

    def add_rule(self, conditions, actions):
        
        new_rule = {"conditions": conditions, "actions": actions}
        self.storage.add_rule(new_rule)
        self.cache.clear_cache()

    def evaluate_rules(self, input_data, dynamic_params):
        """
        Evaluates rules with dynamic parameters.
        :param input_data: Transaction or event data.
        :param dynamic_params: Dictionary of dynamic thresholds.
        """
        rules = self.storage.fetch_rules()
        variables = RuleVariables(input_data, dynamic_params)  # ✅ Pass dynamic values
        actions = RuleActions()

        for rule in rules:
            for condition in rule["conditions"].get("all", []):
                if isinstance(condition["value"], str) and condition["value"] in dynamic_params:
                    condition["value"] = dynamic_params[condition["value"]]  # ✅ Convert string to numeric value
            engine.run(rule, variables, actions)
        return {"triggered_rules": actions.results}

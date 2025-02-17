"""
This module defines the RuleActions class, which specifies actions that can be triggered when rules match.

Classes:
    RuleActions: Inherits from BaseActions and defines specific actions.

Methods:
    __init__: Initializes the RuleActions instance and sets up an empty results list.
    boolean_trigger: Appends a dictionary with action name and result to the results list when executed.
"""
from business_rules.actions import BaseActions, rule_action

class RuleActions(BaseActions):
    """Defines actions that can be triggered when rules match."""

    def __init__(self):
        self.results = []

    @rule_action()
    def boolean_trigger(self):
        """Returns True when this action is executed."""
        self.results.append({"action": "boolean_trigger", "result": True})  # ✅ Ensure action is stored correctly


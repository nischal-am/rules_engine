"""
This module defines the data models for the rules engine.

Classes:
    RuleCreate: A Pydantic model representing the structure of a rule creation request.

Attributes:
    name (str): The name of the rule.
    conditions (str): The conditions that trigger the rule.
    actions (Dict): The actions to be taken when the rule is triggered.
"""
from pydantic import BaseModel

from typing import Dict

class RuleCreate(BaseModel):
    name: str
    conditions: str
    actions: Dict
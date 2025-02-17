from business_rules.variables import BaseVariables, rule_variable
from business_rules.operators import StringType, NumericType
from typing import Dict, Any

class RuleVariables(BaseVariables):
    """Defines variables available for rule evaluation across engines."""

    def __init__(self, data: Dict[str, Any], dynamic_params: Dict[str, Any]):
        """
        :param data: Transaction or event data (e.g., {"transaction_amount": 500})
        :param dynamic_params: Dynamic threshold values (e.g., {"threshold_1": 100, "threshold_2": 200})
        """
        self.data = data  # ✅ Store transaction/event data
        self.dynamic_params = dynamic_params  # ✅ Store dynamic thresholds

    @rule_variable(NumericType)
    def transaction_amount(self) -> float:
        """Retrieve the order amount from input data."""
        return float(self.data.get("transaction_amount", 0))
    
    @rule_variable(NumericType)
    def threshold_amount(self) -> float:
        """Fetches the threshold value dynamically."""
        return float(self.dynamic_params.get("threshold_amount", 0))  # ✅ Ensure it's a numeric type

    @rule_variable(StringType)
    def funding_type(self) -> StringType:
        """Retrieve the funding type (e.g., 'instant-funding', 'morning-funding')."""
        return self.data.get("funding_type", "instant-funding")

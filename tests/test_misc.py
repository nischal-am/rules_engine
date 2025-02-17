from rules.rule_variables import RuleVariables

def test_threshold_amount():
    # ✅ Simulate input
    transaction_data = {"transaction_amount": 750}
    dynamic_params = {"threshold_amount": 500}

    variables = RuleVariables(transaction_data, dynamic_params)

    # ✅ Check if threshold_amount resolves to a numeric value
    print(f"Transaction Amount: {variables.transaction_amount()}")
    print(f"Threshold Amount: {variables.threshold_amount()}")  # ✅ Should print 500 as a float
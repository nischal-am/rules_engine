from rules.business_rules import BusinessRulesEngine
from rules.rule_cache.lru_cache import LRUCache
from rules.storage.file_storage import FileRuleStorage
from rules.rule_actions import RuleActions


def sample_input_data():
    """Mock input data that meets the rule conditions."""
    return {
        "transaction_amount": 8000,
        "funding_type": "instant-funding"
    }

def sample_input_data_no_holds():
    """Mock input data that does not meet the rule conditions."""
    return {
        "transaction_amount": 2000,
        "funding_type": "instant-funding"
    }

def sample_dynamic_params():
    """Mock dynamic params data that are used for evaluating the rule conditions."""
    return {
        "threshold_amount": 2500
    }

def evaluateHolds(sample_input_data, sample_dynamic_params):
    rule_engine = BusinessRulesEngine(LRUCache(), FileRuleStorage())

    actions = RuleActions()

    results = rule_engine.evaluate_rules(sample_input_data, sample_dynamic_params)
    print(results)

    actions.results = results["triggered_rules"]
    print(actions.results)

    print("The length for actions.results=%s " %len(actions.results))  # Some should be triggered
    # Validate expected action was triggered
    expected_result = [{"action": "boolean_trigger", "result": True}]
    print("The rules triggered %s" %(actions.results == expected_result))
    isTransToBeHeld = (any(action["action"] == "boolean_trigger" for action in actions.results))
    print("Returning %s from is transaction to be held" %isTransToBeHeld)
    return isTransToBeHeld

def evaluateNoHolds(sample_input_data_no_holds, sample_dynamic_params):
    rule_engine = BusinessRulesEngine(LRUCache(), FileRuleStorage())

    actions = RuleActions()

    results = rule_engine.evaluate_rules(sample_input_data_no_holds, sample_dynamic_params)
    print(results)

    actions.results = results["triggered_rules"]
    print(actions.results)

    print("The length for actions.results=%s " %len(actions.results))  # Some should be triggered
    # Validate expected action was triggered
    expected_result = [{"action": "boolean_trigger", "result": False}]
    print("The rules triggered %s" %(actions.results == expected_result))
    isTransToBeHeld = (any(action["action"] == "boolean_trigger" for action in actions.results))
    print("Returning %s from is transaction to be held" %isTransToBeHeld)
    return isTransToBeHeld

print("*"*120)
print("Evaluating rules with data that should result in holds trans_data:{0}, threshold_data:{1}".format(sample_input_data(), sample_dynamic_params()))
print("*"*120)
evaluateHolds(sample_input_data(), sample_dynamic_params())
print("*"*120)
print("Evaluating rules with data that should result in NO holds trans_data:{0}, threshold_data:{1}".format(sample_input_data_no_holds(), sample_dynamic_params()))
print("*"*120)
evaluateNoHolds(sample_input_data_no_holds(), sample_dynamic_params())
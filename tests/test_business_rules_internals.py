from business_rules.operators import StringType


def test_string_comparison_operations_supported():
    # Create instances
    string1 = StringType("vip")
    string2 = "vip"

    try: 
        print(string1.equals_string(string2))
    except AttributeError:
        print("\n❌ `equals_string` is NOT supported in business-rules")

    try: 
        print(string1.equals(string2))
    except AttributeError:
        print("❌ `equals` is NOT supported in business-rules")

    try: 
        print(string1.equal_to(string2))
        print("`equal_to` is SUPPORTED in business-rules")
    except AttributeError:
        print("❌ `equal_to` is NOT supported in business-rules")

    print(dir(StringType))
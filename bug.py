def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error occurred"

# Uncommon error: Trying to divide a string by a number
result1 = function_with_uncommon_error("hello", 2)
print(result1)  # Output: Type error occurred

# Uncommon error: Trying to divide a number by a string
result2 = function_with_uncommon_error(10, "world")
print(result2)  # Output: Type error occurred

# Uncommon error: Trying to divide a list by a number
result3 = function_with_uncommon_error([1,2,3], 2)
print(result3) # Output: Type error occurred

# Expected error: Division by zero
result4 = function_with_uncommon_error(10, 0)
print(result4)  # Output: Division by zero
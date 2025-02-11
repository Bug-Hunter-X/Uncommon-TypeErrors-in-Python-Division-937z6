def improved_function_with_error_handling(a, b):
    """Performs division with improved error handling.

    Args:
        a: The numerator (dividend).
        b: The denominator (divisor).

    Returns:
        The result of the division if successful, otherwise an appropriate error message.
    """
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        return "Type Error: Both numerator and denominator must be numbers"
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"

# Test cases
print(improved_function_with_error_handling(10, 2))  # Output: 5.0
print(improved_function_with_error_handling(10, 0))  # Output: Division by zero
print(improved_function_with_error_handling("hello", 2)) # Output: Type Error: Both numerator and denominator must be numbers
print(improved_function_with_error_handling(10, "world")) # Output: Type Error: Both numerator and denominator must be numbers
print(improved_function_with_error_handling([1,2,3], 2)) # Output: Type Error: Both numerator and denominator must be numbers
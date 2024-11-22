def my_sum(*numbers):
    """
    Calculate the sum of a sequence of numbers.

    This function takes any number of numeric arguments
    and returns their total sum.

    Args:
        *numbers (float or int):
        A variable number of numeric arguments to be summed.

    Returns:
        float: The sum of the input numbers.
    """
    sum = 0

    for number in numbers:
        sum += number
    return sum


give_input = input("What you want to sum: ")
numbers = tuple(map(float, give_input.split()))

print(my_sum(*numbers))

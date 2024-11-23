def my_sum(*numbers):
    """
    Calculate the sum of a sequence of numbers.

    This function takes any number of numeric arguments
    and returns their total sum.
    """

    sum = 0

    for number in numbers:
        sum += number
    return sum


def main():
    """
    The main function to interact with the user and sum the numbers.

    This function prompts the user to input numbers separated by spaces,
    converts them to floats, and then calls the `my_sum` function to calculate
    the sum of those numbers. The result is printed to the screen.
    """
    give_input = input("What you want to sum: ")
    numbers = tuple(map(float, give_input.split()))

    print(my_sum(*numbers))


if __name__ == '__main__':
    main()

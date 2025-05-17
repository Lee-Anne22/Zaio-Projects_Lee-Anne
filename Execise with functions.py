def calculate_product(*args):
    """
    Calculates the product of any number of arguments.

    Args:
        *args:  A variable number of numerical arguments.

    Returns:
        The product of all the input arguments.
    """
    product = 1
    for arg in args:
        product *= arg
    return product
result = calculate_product(2, 3, 4)
print(result)
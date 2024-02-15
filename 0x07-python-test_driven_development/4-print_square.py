def print_square(size):
    """Prints a square with the character '#'.

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:None
    """

    if not isinstance(size, int):
        raise TypeError
    if size < 0:
        raise ValueError

    for _ in range(size):
        print("#" * size)

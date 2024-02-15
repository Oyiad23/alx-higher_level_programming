def text_indentation(text):
    """Prints two new lines after ".?:" characters

    Args:
        text (str): The input string.

    Raises:
        TypeError: If text is not a string.

    Returns:None
    """
    if not isinstance(text, str):
        raise TypeError

    for delimiter in ".?:":
        text = text.replace(delimiter, delimiter + "\n\n")

    print(text, end="")

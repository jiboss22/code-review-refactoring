"""Transform a list of numbers and a list of words, then print the results."""

# Words longer than this many characters are shown in uppercase.
LONG_WORD_LENGTH = 5


def transform_numbers(numbers):
    """Double the even numbers and triple the odd numbers in a list.

    Args:
        numbers (list of int): The whole numbers to transform.

    Returns:
        list of int: A new list where each even number is multiplied by 2
        and each odd number is multiplied by 3, in the original order.
    """
    return [
        number * 2 if number % 2 == 0 else number * 3
        for number in numbers
    ]


def format_words(words):
    """Join words into one string, uppercasing long words only.

    Args:
        words (list of str): The words to format.

    Returns:
        str: The formatted words separated by single spaces. Words longer
        than LONG_WORD_LENGTH characters are uppercase; all others are
        lowercase.
    """
    # join() puts spaces only between words, so no trailing space is left
    # over and the original strip() call is no longer needed.
    return " ".join(
        word.upper() if len(word) > LONG_WORD_LENGTH else word.lower()
        for word in words
    )


def main():
    """Run the transformations on sample data and print the results."""
    sample_numbers = [1, 2, 3, 4, 5, 6, 7]
    sample_words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    transformed_numbers = transform_numbers(sample_numbers)
    formatted_words = format_words(sample_words)

    print("Processed Numbers:", transformed_numbers)
    print("Processed Strings:", formatted_words)


if __name__ == "__main__":
    main()

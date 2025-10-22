"""
Palindrome App - A comprehensive palindrome checker and generator
"""

import re


def is_palindrome(text, ignore_case=True, ignore_spaces=True):
    """
    Check if a word or phrase is a palindrome.

    Args:
        text (str): The text to check
        ignore_case (bool): Whether to ignore case differences (default: True)
        ignore_spaces (bool): Whether to ignore spaces and punctuation (default: True)

    Returns:
        bool: True if the text is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    if not text:
        return False

    # Process the text based on parameters
    processed = text

    if ignore_spaces:
        # Remove all non-alphanumeric characters
        processed = re.sub(r'[^a-zA-Z0-9]', '', processed)

    if ignore_case:
        processed = processed.lower()

    # Check if it's a palindrome
    return processed == processed[::-1]


def is_number_palindrome(number):
    """
    Check if a number is a palindrome.

    Args:
        number (int or str): The number to check

    Returns:
        bool: True if the number is a palindrome, False otherwise

    Examples:
        >>> is_number_palindrome(12321)
        True
        >>> is_number_palindrome(12345)
        False
    """
    num_str = str(number)
    return num_str == num_str[::-1]


def is_strict_palindrome(text):
    """
    Check if text is a strict palindrome (exact character-by-character matching).
    Considers case, spaces, and punctuation.

    Args:
        text (str): The text to check

    Returns:
        bool: True if the text is a strict palindrome, False otherwise

    Examples:
        >>> is_strict_palindrome("racecar")
        True
        >>> is_strict_palindrome("A man a plan a canal Panama")
        False
    """
    if not text:
        return False
    return text == text[::-1]


def find_palindromes(text, min_length=3):
    """
    Find all palindromic substrings within a given text.

    Args:
        text (str): The text to search
        min_length (int): Minimum length of palindromes to find (default: 3)

    Returns:
        set: A set of unique palindromic substrings

    Examples:
        >>> find_palindromes("racecar")
        {'racecar', 'aceca', 'cec'}
    """
    if not text or len(text) < min_length:
        return set()

    palindromes = set()
    text_lower = text.lower()
    n = len(text_lower)

    # Check all possible substrings
    for i in range(n):
        for j in range(i + min_length, n + 1):
            substring = text_lower[i:j]
            if substring.isalnum() and substring == substring[::-1]:
                palindromes.add(text[i:j])  # Add original case version

    return palindromes


def generate_palindrome(word):
    """
    Generate a palindrome from a given word by mirroring it.

    Args:
        word (str): The word to generate a palindrome from

    Returns:
        str: A palindrome created by mirroring the word

    Examples:
        >>> generate_palindrome("hello")
        'helloolleh'
        >>> generate_palindrome("python")
        'pythonnohtyp'
    """
    if not word:
        return ""

    # Create palindrome by appending the reverse (excluding last character to avoid duplication)
    return word + word[-2::-1]


def generate_palindrome_symmetric(word):
    """
    Generate a symmetric palindrome from a given word.

    Args:
        word (str): The word to generate a palindrome from

    Returns:
        str: A symmetric palindrome

    Examples:
        >>> generate_palindrome_symmetric("hello")
        'helloolleh'
        >>> generate_palindrome_symmetric("ab")
        'aba'
    """
    if not word:
        return ""

    # Create symmetric palindrome
    return word + word[-2::-1] if len(word) > 1 else word


# ============================================================================
# DEMO / EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PALINDROME APP - Demo")
    print("=" * 60)

    # Test 1: Word/Phrase Palindromes
    print("\n1. WORD/PHRASE PALINDROME CHECKING")
    print("-" * 60)
    test_phrases = [
        # Classic palindromes
        "racecar",
        "level",
        "kayak",
        "deified",
        "rotator",

        # Famous phrase palindromes
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw?",
        "Never odd or even",
        "Do geese see God?",
        "Madam, I'm Adam",
        "Mr. Owl ate my metal worm",
        "No lemon, no melon",
        "A Santa at NASA",
        "Step on no pets",

        # Single words
        "Madam",
        "radar",
        "civic",
        "refer",

        # Edge cases
        "a",
        "aa",
        "ab",

        # Mixed alphanumeric
        "12321",
        "A1B2B1A",

        # NOT palindromes
        "hello world",
        "test case 1",
        "python",
    ]

    for phrase in test_phrases:
        result = is_palindrome(phrase)
        print(f"'{phrase}' → {'✓ Palindrome' if result else '✗ Not a palindrome'}")

    # Test 2: Number Palindromes
    print("\n2. NUMBER PALINDROME CHECKING")
    print("-" * 60)
    test_numbers = [
        # Palindrome numbers
        0,
        1,
        7,
        11,
        121,
        1221,
        12321,
        123321,
        11111,
        123454321,
        9009,

        # NOT palindromes
        10,
        100,
        12345,
        987654,
        1234567890,
    ]

    for num in test_numbers:
        result = is_number_palindrome(num)
        print(f"{num} → {'✓ Palindrome' if result else '✗ Not a palindrome'}")

    # Test 3: Strict Palindromes
    print("\n3. STRICT PALINDROME CHECKING (exact matching)")
    print("-" * 60)
    strict_tests = [
        # Strict palindromes (exact match)
        "racecar",
        "noon",
        "aba",
        "a b a",
        "12321",
        "!!!",
        "...",

        # NOT strict palindromes
        "Racecar",          # Different case
        "A man",            # Not a palindrome at all
        "race car",         # Has space in middle
        "a b c b a",        # Has spaces but is palindrome
        "Madam",            # Different case
    ]

    for text in strict_tests:
        result = is_strict_palindrome(text)
        print(f"'{text}' → {'✓ Strict palindrome' if result else '✗ Not a strict palindrome'}")

    # Test 4: Find Palindromes
    print("\n4. FIND PALINDROMIC SUBSTRINGS")
    print("-" * 60)
    search_texts = [
        "racecar",
        "abba noon level",
        "The racecar driver saw a kayak at noon",
        "madam and dad saw a civic",
        "python programming",
        "aabbccbbaa",
        "12321 and 454",
    ]

    for text in search_texts:
        palindromes = find_palindromes(text, min_length=3)
        print(f"'{text}':")
        if palindromes:
            print(f"  Found: {sorted(palindromes, key=len, reverse=True)}")
        else:
            print(f"  No palindromes found")

    # Test 5: Generate Palindromes
    print("\n5. GENERATE PALINDROMES")
    print("-" * 60)
    words = [
        "hello",
        "python",
        "code",
        "a",
        "ab",
        "abc",
        "test",
        "race",
        "mom",
        "data",
        "AI",
    ]

    for word in words:
        generated = generate_palindrome(word)
        print(f"'{word}' → '{generated}'")

    print("\n" + "=" * 60)
    print("Demo complete!")
    print("=" * 60)

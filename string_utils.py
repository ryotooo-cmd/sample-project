def reverse_string(s):
    """Return the reverse of the given string."""
    return s[::-1]


def is_palindrome(s):
    """Return True if the given string is a palindrome."""
    return s == reverse_string(s)


def count_vowels(s):
    """Return the number of vowels in the given string."""
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

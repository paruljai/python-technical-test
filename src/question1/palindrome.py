"""Handles palindrome operations Definition: A palindrome is a string that reads the same forward and backward.
For example, "abcba" is a palindrome, "abab" is not."""


def is_palindrome(word: str) -> bool:
    """Please implement this function to return true if the parameter is a palindrome and false otherwise.

       :param word string to determine if a palindrome
       :return true if the parameter is a palindrome and false otherwise"""

    l = len(word)

    for i in range(0, l // 2):
    	if word[i] != word[l - 1 - i]:
    		return False
    return True

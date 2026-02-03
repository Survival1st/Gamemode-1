#3 example
def is_palindrome(s):
    """s is a string
    Returns True if s is a palindrome and False otherwise"""
    #s = "racecar"
    #s = "hello"
    return s == s[::-1]
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
# palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        inv_int = ''.join(list(str(x))[::-1])
        if inv_int == str(x):
            return True
        else:
            return False

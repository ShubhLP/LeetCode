class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for c in s:
            if c.isalnum():
                st += c.lower()
        if st == st[::-1]:
            return True
        else:
            return False

##### Faster #####
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
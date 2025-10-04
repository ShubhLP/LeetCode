class Solution(object):
    def palindrome(self, x):

        num = x
        sum = 0
        while num != 0:
            rem = num % 10
            sum = sum * 10 + rem
            num = num // 10

        if sum == x:
            return "Palindrome"
        else:
            return "Not a palindrome"

sol = Solution()
x = 121
print(sol.palindrome(x))
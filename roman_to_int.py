class Solution(object):
    def romanToint(self, s):
        
        h = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        num = 0

        for i in range(len(s) - 1):
            if h[s[i]] >= h[s[i + 1]]:
                num = num + h[s[i]]
            else:
                num = num - h[s[i]]
        num = num + h[s[i + 1]]

        return num
    
sol = Solution()
# s = "LVIII"
s = "MCMXCIV"
print(sol.romanToint(s))
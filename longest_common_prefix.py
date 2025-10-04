class Solution(object):
    def longest_prefix(self, strs):
        
        pre = ""

        # find the smallest string
        min_len = float('inf')
        for item in strs:
            if len(item) < min_len:
                min_len = len(item)
        
        start = strs[0][:min_len]

        for i in range(min_len):
            for item in strs:
                if item[i] != start[i]:
                    return pre
            pre = pre + item[i]
        
        return pre

sol = Solution()
s = ['flower', 'flow', 'flight']
print(sol.longest_prefix(s))
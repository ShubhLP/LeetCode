class Solution(object):
    def twoSum(self, nums, target):
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - h[nums[i]]
            
            if y in h and h[y] != i:
                return [i, h[y]]

nums = [3, 2, 2, 3]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))
class Solution(object):
    def remove_duplicates(self, nums):

        k = 0
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k + 1, nums

sol = Solution()
nums = [1, 1, 2, 2, 2, 3]
print(sol.remove_duplicates(nums))
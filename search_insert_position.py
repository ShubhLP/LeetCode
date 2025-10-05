class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = high - 1
            else:
                low = low + 1
        
        if nums[mid] < target:
            return mid + 1
        else:
            return mid


nums = [1, 3, 5, 6]
target = 2
sol = Solution()
print(sol.searchInsert(nums, target))
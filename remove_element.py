class Solution(object):
    def remove_element(self, nums, val):

        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k, nums

sol = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(sol.remove_element(nums, val))

# [0,1,2,2,3,0,4,2]
# [0,1,4,0,3,_,_,_]
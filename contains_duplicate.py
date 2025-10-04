class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}

        for n in nums:
            if n in h:
                h[n] += 1
            else:
                h[n] = 1

        list_h = list(h.keys())

        for ind in list_h:
            if h[ind] > 1:
                return True
        return False


######### FASTER!!! ########
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        if len(set) != len(nums):
            return True

        return False
# Brute force approach
# Time: O(nlogn)

import heapq

class Solution:
    def longest_consecutive_sequence_brute_force(self, nums):
        n = len(nums)
        print(n)
        sorted_arr = [0] * n

        for i in range(n):
            minn = heapq.heappop(nums)
            sorted_arr[i] = minn
        print(sorted_arr)

        seq_len = 0
        for i in range(n-1):
            if sorted_arr[i + 1] == sorted_arr[i] + 1:
                seq_len += 1
                
        print(seq_len + 1)

# better solution 
# Time: O(n)

class Solution:
    def longest_consecutive_sequence_brute_force(self, nums):
        
        sett = set(nums)
        longest = 0

        for num in sett:
            if num - 1 not in sett:
                curr = num
                length = 1
                while curr + 1 in sett:
                    curr += 1
                    length += 1
                longest = max(longest, length)
        return longest
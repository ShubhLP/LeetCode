import heapq
from collections import Counter

class Solution:
    def top_k_frequent_elements(self, nums, k):
        heap = []
        freq_elements = []

        counter = Counter(nums)

        for key, v in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (v, key))
            else:
                heapq.heappushpop(heap, (v, key))
        
        for i in range(len(heap)):
            freq_elements.append(heap[i][1])
        
        return(freq_elements)

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
print(sol.top_k_frequent_elements(nums, k))
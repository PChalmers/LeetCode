from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        if(len(nums) == 0):
            return []
        dups = Counter(nums)
        freq = dups.most_common(k)
        return [x for (x,y) in freq] 


s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], k = 2))
print(s.topKFrequent([1], k = 1))
print(s.topKFrequent([], k = 1))
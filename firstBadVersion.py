# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.findBadVersion(1, n)

    def findBadVersion(self, start, end):
        mid = start + ( (end - start) // 2)
        currentValue = self.isBadVerion(mid)
        previousValue = self.isBadVerion(mid-1)
        nextValue = self.isBadVerion(mid+1)
        if(currentValue and not previousValue):
            return mid
        if(not currentValue and nextValue):
            return mid+1
        if(self.isBadVerion(mid)):
            return self.findBadVersion(start, mid)
        else:
            return self.findBadVersion(mid, end)

    def isBadVerion(self, index):
        values = [False,True]
        return values[index-1] # versions start at 1

s = Solution()
print(s.firstBadVersion(2))


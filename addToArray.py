class Solution:
    def addToArrayForm(self, A, K: int):
        orig = int(''.join([str(x) for x in A]))
        orig += K
        return [int(x) for x in list(str(orig))]


s = Solution()
print(s.addToArrayForm([1,2,0,0], 34))
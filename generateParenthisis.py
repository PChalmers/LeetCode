class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n,n,"",result)
        return result
        
    def generate(self,leftParenthLeft,rightParenthLeft,currentResult,results):
        if leftParenthLeft > 0:
            self.generate(leftParenthLeft-1, rightParenthLeft, currentResult+"(", results)

        if (rightParenthLeft > 0) and (rightParenthLeft>leftParenthLeft):
            self.generate(leftParenthLeft, rightParenthLeft-1, currentResult+")", results)
            
        if (leftParenthLeft==0 and rightParenthLeft ==0):
            results.append(currentResult)


 
s = Solution()
t = s.generateParenthesis(2)
for r in t:
    print(r)
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
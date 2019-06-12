class Solution:
    def generateParenthesis(self, n):
        print(self.helper('', n, n, []))

    def helper(self, currentList, numL, numR, result):
 #       print(currentList, numL, numR, result)
        if(numL == 0 and numR == 0):
            result.append(currentList)
            return result
        if(numL == 0 and numR > 0):
            currentList = currentList +')'
            numR -=1
            return result

        if(numL > numR):
            raise Exception('Too many ) brackets')
        
        if(numL != 0):
            self.helper(currentList + '(', numL-1, numR, result)

        if(numL < numR):
            self.helper(currentList + ')', numL, numR-1, result)

        return result
s = Solution()
print(s.generateParenthesis(3))

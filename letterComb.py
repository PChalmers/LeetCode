class Solution:
    def letterCombinations(self, digits):
        letters = {
                '2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], 
                '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], 
                '8': ['t','u','v'], '9': ['w','x','y','z'] }
        if(len(digits) == 0):
            return []
        finalList = letters[digits[0]]
        for char in digits[1:]:
            list2 = letters[char]
            finalList = [x + y for x in finalList for y in list2]
        return finalList

s = Solution()
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
print(s.letterCombinations("23"))
print(s.letterCombinations("74"))
print(s.letterCombinations("743"))
print(s.letterCombinations("7432345"))

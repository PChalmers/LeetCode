class Solution:
    def plusOne(self, digits):
        for index in range(len(digits)-1, -1, -1):
            oldValue = digits[index]
            digits[index] = (digits[index]+1)%10
            if(oldValue < digits[index]):
                return digits
        digits.insert(0,1)
        return digits



s = Solution()
print(s.plusOne([1,2,3,9]))
print(s.plusOne([1,9,9,9]))
print(s.plusOne([9,9,9,9]))
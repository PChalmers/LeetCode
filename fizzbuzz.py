class Solution:
    def fizzBuzz(self, n: int):
        returnValues = []
        for num in range(1,n+1):
            if(num%3 == 0):
                returnValues.append('Fizz')
            elif(num%5 == 0):
                returnValues.append('Buzz')
            else:
                returnValues.append(str(num))
        return returnValues
s = Solution()
print(s.fizzBuzz(15))
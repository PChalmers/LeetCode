class Solution:
    def permute(self, nums):
        result = []
        self.createPerm(len(nums), [], nums, result)
        return result

    def createPerm(self, size, currentPerm, valuesAvail, result):
        print('size', size, 'currentPerm', currentPerm, 'values available' , valuesAvail, 'result',  result)
        # base case
        if(len(currentPerm) == size) or len(valuesAvail) == 0:
            result.append(currentPerm)
            return
        
        # recurse for each value still available in the nums array
        for x in range(0, len(valuesAvail)):
            numToAdd = valuesAvail.pop()
            tempValues = [i for i in valuesAvail]

            # Make a copy of the current permutation
            tempCurrent = [i for i in currentPerm]
            # Add another number from the values available list
            tempCurrent.append(numToAdd)
            self.createPerm(size, tempCurrent, tempValues, result)


s = Solution()
r = s.permute([1,2,3])
for t in r:
    print(t)
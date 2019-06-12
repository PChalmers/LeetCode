import math

class Solution:
    def maxSubArray(self, nums) -> int:
        if(len(nums) == 0):
            return 0
        left, right, maxSum = self.find_maximum_subarray(nums,0,len(nums)-1)
        print(left, right, maxSum)

    def find_maximum_subarray(self,A,low,high):
        if(high == low):
            return low,high,A[low]

        self.mid = (low + high) // 2 
        left_low,left_high,left_sum = self.find_maximum_subarray(A,low,self.mid)
        right_low,right_high,right_sum = self.find_maximum_subarray(A,self.mid + 1,high)
        cross_low,cross_high,cross_sum = self.find_max_crossing_subarray(A,low,self.mid,high)
        if(left_sum >= right_sum and left_sum >= cross_sum):
            return left_low,left_high,left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low,right_high,right_sum

        return cross_low,cross_high,cross_sum

    def find_max_crossing_subarray(self, A,low,mid,high):
        left_sum = math.inf
        maxSum = 0
        max_left = mid
        max_right = mid+1
        for i in range(mid, low, -1):
            maxSum =maxSum + A[i]
            if(maxSum > left_sum):
                left_sum = maxSum
                max_left = i
        right_sum = math.inf*-1
        maxSum = 0 
        for j in range(mid+1, high+1):
            maxSum = maxSum + A[j]
            if(maxSum > right_sum):
                right_sum = maxSum
                max_right = j
                
        return (max_left,max_right,left_sum + right_sum)


s = Solution()
print(s.maxSubArray([-2,1,-3,4,2,-1,2,1,-5,4]))
#print(s.maxSubArray([-3,-2,-1]))
#print(s.maxSubArray([-1]))
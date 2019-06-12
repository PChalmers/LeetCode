class Solution:
    def trap(self, height) -> int:
        previousValue = total = 0
        levels = {}
        for x in range(len(height)):
            print("From -> ", previousValue, ' to ', height[x])
            # Increasing: Add all level values closed off by the increase and delete the levels
            #        also add 1 to any remaining levels
            if(height[x] > previousValue):
                for index in range(previousValue, height[x]+1):
                    if index in levels.keys():
                        print('Height increasing: removing {}'.format(index))
                        value = levels[index] 
                        total += value
                        del levels[index]
                # Add 1 to each existing level
                for level in levels:
                    levels[level] += 1

            # Decreasing: add 1 to previously existing levels
            #         and Add new levels for each newly exposed levels
            elif(height[x] < previousValue):
                # Add 1 to each existing level
                for level in levels:
                    levels[level] += 1
                for index in range(height[x]+1, previousValue+1):
                    if(index > 0):
                        print('Height decreasing: adding {} - shouldnt exist'.format(index))
                        levels[index] = 1
            
            # Same: Add 1 to each level that already exists
            else:
                print('same value {}'.format(previousValue))
                # Add 1 to each existing level
                for level in levels:
                    levels[level] += 1
            previousValue = height[x]
            print(total, levels)
        return total

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(s.trap([4,2,3])) # 1
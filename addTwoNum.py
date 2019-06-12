# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Get number from L1
        l1List = self.getNum(l1, [])
        # Get number from L2
        l2List = self.getNum(l2, [])
        # Add numbers
        l1num = int(''.join([str(x) for x in reversed(l1List)]))
        l2num = int(''.join([str(x) for x in reversed(l2List)]))
        finalNum = l1num + l2num

        # build final data stucture to return
        result = tempNode = None
        for x in reversed(str(finalNum)):
            if(tempNode == None):
                tempNode = ListNode(x)
                result = tempNode
            else:
                tempNode.next = ListNode(x)
                tempNode = tempNode.next
        return result

        # Create and return list from the Linked List
    def getNum(self, l, returnList):
        if(l.next == None):
            return [l.val]
        return returnList + [l.val] + self.getNum(l.next, returnList)


I1 = ListNode(2)
t = ListNode(4)
t2 = ListNode(3) 
t.next = t2
I1.next = t

I2 = ListNode(5)
r = ListNode(6)
r2 = ListNode(4) 
r.next = r2
I2.next = r

s = Solution()
t = s.addTwoNumbers(I1, I2)

while t != None:
    print(t.val, end=' ')
    t = t.next

#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.
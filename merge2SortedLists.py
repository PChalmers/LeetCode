# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = None
        while(l1 != None or l2 != None):
            if(l1.val < l2.val):
                temp = l1 if temp == None else l1.next
                temp.append()
                l1 = l1.next


#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

l1Nums = [1,2,4]
l2Nums = [1,3,4]

def createList(nums):
    out = ListNode(nums[0])
    temp = out
    for index in range(1,len(nums)):
        temp.next = ListNode(nums[index])
    return out

l1 = createList(l1Nums)
l2 = createList(l2Nums)

s = Solution()
print(s.mergeTwoLists(l1, l2))
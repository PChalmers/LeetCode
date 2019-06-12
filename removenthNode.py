# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if((head == None) or (head.next == None and n >= 1)):
            return None
        temp = head
        d = deque('',n+1)
        while temp != None:
            d.appendleft(temp)
            temp = temp.next
        if(d[n-1] == head):
            head = head.next
        else:
            d[n].next = d[n-1].next
        return head

def printList(head):
    while(head):
        print(head.val, end = '-')
        head = head.next
    print()

s = Solution()
#entries = [1,2,3,4,5,6,7,8,9]
entries = [1]
head = ListNode(0)
temp = head
for value in entries:
    temp.next = ListNode(value)
    temp = temp.next

printList(head)
newHead = s.removeNthFromEnd(head, 2)
printList(newHead)
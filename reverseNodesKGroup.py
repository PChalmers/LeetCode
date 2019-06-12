# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        self.printList(head)
        
        # represents the previous list before the new reversed sublist
        parent = head
        restOfChain = newSubList = None
        
        # Save the rest of the chain for next iteration
        restOfChain = self.getLink(parent, k+1)
        # get the last link in the series to reverse
        newSubList = current = self.getLink(parent, k)

        last.next = self.getLink(parent, k-1)
        last.next.next = self.getLink(parent, k-2)
        last.next.next.next = restOfChain

        print('Beginning of new series - ' + str(current.val))
        self.printList(last)

        # Get the next links to add



        current.next = restOfChain
        self.printList(last)
        return head


    def getLink(self, link, k):
        if(k == 1):
            return link
        if(link == None):
            return None
        return self.getLink(link.next, k-1)

    def getReversedLinks(self, link, k, restOfChain=None):
        if(k == 1):
            return link, link.next
        if(link.next == None):
            return link, None
        lastLink, restOfChain = self.getLink(link.next, k-1, restOfChain)

        return link, restOfChain

    def printList(self, t):
        while(t != None):
            print(t.val, end=' ')
            t = t.next
        print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

s = Solution()
t = s.reverseKGroup(head, 3)
s.printList(t)

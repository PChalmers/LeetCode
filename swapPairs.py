class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def swapPairs(self, head):
        # start with base case
        newHead = None
        if( head != None and head.next != None):
            temp = head.next.next # save the rest of the chain
            newHead = head.next
            newHead.next = head
            newHead.next.next = temp
            
            # Parent is the last swapped value
            parent = newHead
        else:
            return head
        
        parent = newHead.next
        # parent always valid, is the last swapped value
        # check there are 2 more valid links to swap
        while(parent.next != None and parent.next.next != None):
            link1 = parent.next
            link2 = parent.next.next
            restOfChain = parent.next.next.next
            # Swap the next 2 validated links
            link1.next = restOfChain
            link2.next = link1
            parent.next = link2
            # Set the parent for the next pair to swap
            parent = parent.next.next

        # list traversed so return the new head
        return newHead

            
head = listNode(1)
head.next = listNode(2)
head.next.next = listNode(3)
head.next.next.next = listNode(4)
head.next.next.next.next = listNode(5)
head.next.next.next.next.next = listNode(6)
head.next.next.next.next.next.next = listNode(7)
head.next.next.next.next.next.next.next = listNode(8)

s = solution()
t = s.swapPairs(head)

while(t != None):
    print(t.val, end=' ')
    t = t.next
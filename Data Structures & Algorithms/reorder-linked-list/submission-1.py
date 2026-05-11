# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        curr_slow = slow
        while fast and fast.next:
            curr_slow = curr_slow.next
            fast = fast.next.next 
        from_slow = curr_slow.next
        curr_slow.next = None
        prev = None

        while from_slow:
            next_node = from_slow.next
            from_slow.next = prev
            prev = from_slow
            from_slow = next_node
        
        newLL = ListNode()
        newHead = newLL
        flagOne = True
        flagTwo = False
        while slow and prev:
            if flagOne:
                newHead.next = slow
                slow = slow.next
                flagOne = False
                flagTwo = True
            else:
                newHead.next = prev
                prev = prev.next
                flagOne = True
                flagTwo = False
            newHead = newHead.next
        if slow:
            newHead.next = slow
        if prev:
            newHead.next = prev
        
        head = newHead
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return None
        
        llNode = 0
        curr = head
        while curr:
            llNode += 1
            curr = curr.next
        print(llNode)
        prev = None
        deletion_node = head
        while llNode != n:
            llNode -= 1
            prev = deletion_node
            deletion_node = deletion_node.next
        print(deletion_node.val)
        if deletion_node == head:
            return head.next
        else:
            prev.next = deletion_node.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            goal is to merge two lists into one sorted list and return head
            both lists are already sorted
            1->2->4
                   c
            
            1->3->5
                  c

            1->1->2->3->4->5       
        '''
        firstListHead = list1
        secondListHead = list2
        newList = ListNode()
        currHead = newList
        while list1 and list2:
            if list1.val > list2.val:
                newList.next = list2
                newList = newList.next
                list2 = list2.next
            else:
                newList.next = list1
                newList = newList.next
                list1 = list1.next

        if list1:
            newList.next = list1
        
        if list2:
            newList.next = list2
        
        return currHead.next
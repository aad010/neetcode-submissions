# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currOne = list1
        currTwo = list2
        newLL = ListNode() 
        newLLHead = newLL
        while currOne and currTwo:
            if currOne.val <= currTwo.val:
                newLLHead.next = currOne
                currOne = currOne.next
            else:
                newLLHead.next = currTwo
                currTwo = currTwo.next
            newLLHead = newLLHead.next
        
        if currOne:
            newLLHead.next = currOne
        
        if currTwo:
            newLLHead.next = currTwo

        return newLL.next
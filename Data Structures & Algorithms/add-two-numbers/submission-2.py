# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        val_strOne = ""
        val_strTwo = ""

        while curr_l1:
            val_strOne += str(curr_l1.val)
            curr_l1 = curr_l1.next

        while curr_l2:
            val_strTwo += str(curr_l2.val)
            curr_l2 = curr_l2.next
        
        val_strOne = val_strOne[::-1]
        val_strTwo = val_strTwo[::-1]  

        sum_of_vals = int(val_strOne) + int(val_strTwo)
        sum_of_vals_str = str(sum_of_vals)[::-1]

        newLL = ListNode()
        currLL = newLL
        print(sum_of_vals_str)
        for i in range(len(sum_of_vals_str)):
            print(sum_of_vals_str[i])
            currLL.next = ListNode(int(sum_of_vals_str[i]))
            currLL = currLL.next
        return newLL.next
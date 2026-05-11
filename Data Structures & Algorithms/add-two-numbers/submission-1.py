# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            given two non-empty lists with digits stored in reverse order
            get digits and add together!

            1->2->3
            123 as string, reverse

            4->5->6
            456 as string reverse
            321 + 654 = 975

            975 % 10 = 5
            975 // 10 = 97
            97 % 10 = 7
            97 // 10 = 9 
            9 % 10 = 9
            9 // 10 = 0
        '''
        firstNumber = ""
        secondNumber = ""

        while l1:
            firstNumber += str(l1.val)
            l1 = l1.next
        
        while l2:
            secondNumber += str(l2.val)
            l2 = l2.next

        firstNumber = firstNumber[::-1]
        secondNumber = secondNumber[::-1]

        sumOfNumbers = int(firstNumber) + int(secondNumber)
        newList = ListNode()
        curr = newList
        if sumOfNumbers == 0:
            return ListNode()

        while sumOfNumbers != 0:
            value = sumOfNumbers % 10
            newList.next = ListNode(value)
            newList = newList.next
            sumOfNumbers //= 10
        return curr.next

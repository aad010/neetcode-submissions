class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            goal: check if a sting is a palindrome

            a man, a plan, a canal: Panama

              l                         r
        '''

        leftPtr = 0
        rightPtr = len(s) - 1

        while leftPtr < rightPtr: 
            while rightPtr > leftPtr and not self.alphanumericOrNot(s[leftPtr]):
                leftPtr += 1
            while rightPtr > leftPtr and not self.alphanumericOrNot(s[rightPtr]):
                rightPtr -= 1
            if s[leftPtr].lower() != s[rightPtr].lower():
                return False
            else:
                leftPtr += 1
                rightPtr -= 1
        
        return True
    def alphanumericOrNot(self, s):
            if (ord(s) >= 97 and ord(s) <= 122) or (ord(s) >= 65 and ord(s) <= 90) or (ord(s) >= 48 and ord(s) <= 57):
                return True
            else:
                return False
            

            

        
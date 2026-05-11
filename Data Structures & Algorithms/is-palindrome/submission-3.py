class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        def isAlphanumeric(letter):
            if (ord(letter) >= 48 and ord(letter) <= 57) or (ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122):
                return True
            else:
                return False

        while l <= r:
            while l < r and l < len(s) and not isAlphanumeric(s[l]):
                l += 1
            while r > l and r >= 0 and not isAlphanumeric(s[r]):
                r -= 1

            if l < r and s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        
        return True
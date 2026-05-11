class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_set = set()
        for letter in s:
            letter_set.add(letter)
        max_val = 0
        for letter in letter_set:
            max_letter = 0
            l = 0
            k_val = k
            for r in range(len(s)):
                if s[r] != letter:
                    k_val -= 1
                while k_val < 0:
                    if s[l] != letter:
                        k_val += 1
                    l += 1
                max_letter = max(max_letter, r - l + 1)
            max_val = max(max_val, max_letter)
        
        return max_val
                
        
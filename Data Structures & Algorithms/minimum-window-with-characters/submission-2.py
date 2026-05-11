class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)

        for letter in t:
            t_dict[letter] += 1
        
        s_dict = defaultdict(int)
        cntr = 0
        l = 0
        minString = ""
        minStringVal = float('inf')
        for r in range(len(s)):
            s_dict[s[r]] += 1
            if s[r] in t_dict and s_dict[s[r]] <= t_dict[s[r]]:
                print("s", s[r], s_dict[s[r]])
                print("t", s[r], t_dict[s[r]])
                cntr += 1
            while cntr == len(t):
                if minStringVal > (r - l + 1):
                    minStringVal = r - l + 1
                    minString = s[l : r + 1]
                if s[l] in t_dict and s_dict[s[l]] <= t_dict[s[l]]:
                    cntr -= 1
                s_dict[s[l]] -= 1
                l += 1
        
        return minString
                
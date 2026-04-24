class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        freq = {}
        left = 0
        best = 0

        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
        
            # replacements = window size - num of most freq letter 
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        
        return best



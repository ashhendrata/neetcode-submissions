class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        right = 1
        curr = set()
        curr.add(s[left])
        maxlen = 0
        while right < len(s):
            if s[right] in curr:
                curr.clear()
                left += 1
                right = left + 1
                curr.add(s[left])
            else:
                curr.add(s[right])
                maxlen = max(maxlen, right - left + 1)
                right += 1
        
        return max(maxlen, 1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 28
        for letter in s:
            letters[ord(letter)- 97] += 1
        for letter in t:
            letters[ord(letter)-97] -= 1
        if all(v == 0 for v in letters):
            return True
        return False
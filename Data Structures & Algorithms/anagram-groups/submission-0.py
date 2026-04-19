class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # key: array counter, value: array of strings (anagrams)
        for string in strs:
            counter = [0] * 26
            for letter in string:
                counter[ord(letter) - 97] += 1
            if str(counter) not in anagrams:
                anagrams[str(counter)] = [string]
            else:
                anagrams[str(counter)].append(string)
        
        res = []
        for key in anagrams:
            res.append(anagrams[key])
        return res
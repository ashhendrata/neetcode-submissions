class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1

        while left < right:
            if not s[left].isalnum():
                left += 1
                print ("not al left" + s[left])
                continue
            if not s[right].isalnum():
                right -= 1
                print ("not al right" + s[right])
                continue
            if s[left].lower() != s[right].lower():
                print("left" + str(left))
                print("right" + str(right))
                return False
            left += 1
            right -= 1
        return True
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False
        ope = ["(", "{", "["]
        clo = [")", "}", ']']
        hashmap = {")": "(", "}": "{", "]": "["}


        stack = []
        for i in range(len(s)):
            print("stack1", stack)
            if s[i] in ope:
                stack.append(s[i])
                print(s[i])
                print("stack2", stack)
            print("mid",stack)
            print(s[i])
            if s[i] in clo:
                print("hi")
                if stack:
                    if stack[-1] != hashmap[s[i]]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
            print("stack3", stack)
        
        if len(stack) == 0:
            return True
        else:
            return False
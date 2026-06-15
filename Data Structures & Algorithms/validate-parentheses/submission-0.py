class Solution:
    def isValid(self, s: str) -> bool:
        hash_char = {")": "(", "}": "{", "]": "["}
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] in  hash_char.keys():
                if stack and stack[-1] == hash_char[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False


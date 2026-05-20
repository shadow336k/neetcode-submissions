class Solution:
    def isValid(self, s: str) -> bool:
        par_map = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for char in s:
            if char in par_map:
                stack.append(par_map[char])
            else:
                if not stack or char != stack.pop():
                    return False
        return len(stack) == 0
        

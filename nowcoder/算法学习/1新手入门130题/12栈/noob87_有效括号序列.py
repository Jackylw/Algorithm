# https://www.nowcoder.com/practice/37548e94a270412c8b9fb85643c8ccc2
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[":
                stack.append(char)
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif char == "(":
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "{":
                stack.append(char)
            elif char == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
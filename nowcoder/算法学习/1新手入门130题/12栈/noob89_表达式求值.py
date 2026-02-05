# https://www.nowcoder.com/practice/c215ba61c8b1443b996351df929dc4d4
class Solution:
    def solve(self, s: str) -> int:
        def cal(op, num1, num2):
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            return 0
        def precedence(op):
            """优先级"""
            if op in ('+', '-'):
                return 1
            if op == '*':
                return 2
            return 0 # 括号
        num_stack = []
        ops_stack = []
        i = 0
        n = len(s)
        while i < n:
            char = s[i]
            if char.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue
            elif char == '(':
                ops_stack.append(char)
            # 计算括号内
            elif char == ')':
                while ops_stack and ops_stack[-1] != '(':
                    op = ops_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(cal(op, num1, num2))
                if ops_stack:
                    # 弹出左括号
                    ops_stack.pop()
            elif char in ('+', '-', '*'):
                # 如果当前运算符优先级小于等于栈顶运算符，则计算栈顶运算符
                while ops_stack and precedence(char) <= precedence(ops_stack[-1]):
                    op = ops_stack.pop()
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    num_stack.append(cal(op, num1, num2))
                ops_stack.append(char)
            i += 1
        # 计算剩余运算符
        while ops_stack:
            op = ops_stack.pop()
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            num_stack.append(cal(op, num1, num2))
        return num_stack[0]
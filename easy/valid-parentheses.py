#!/usr/bin/env python3

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for c in s:
            if c in {'(', '{', '['}:
                stack.append(c)
            elif len(stack) !=0 and c == ')' and stack[len(stack)-1] == '(':
                stack.pop()
            elif len(stack) !=0 and c == '}' and stack[len(stack)-1] == '{':
                stack.pop()
            elif len(stack) !=0 and c == ']' and stack[len(stack)-1] == '[':
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        return False

if __name__ == "__main__":
    s1 = Solution().isValid
    print(s1("(){}[]]"))

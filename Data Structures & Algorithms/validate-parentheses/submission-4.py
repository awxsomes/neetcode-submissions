class Solution:
    def isValid(self, s: str) -> bool:

  
        stack = []
        opening = {'(','{','['}
        for i in s:

            if i in opening:
                stack.append(i)
            else:
                if stack == []:
                    return False
                if i == ")" and stack[-1] != '(':
                    return False
                if i == "]" and stack[-1] != '[':
 
                    return False
                if i == "}" and stack[-1] != '{':
                    return False
                stack.pop()
        return stack == []
                    
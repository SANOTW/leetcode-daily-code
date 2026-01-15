class Solution:
    def isValid(self, s: str) -> bool:
        
        dictionary = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for i in s:
            if i in dictionary.values():
                stack.append(i)
            
            elif i in dictionary:

                if not stack:
                    return False

                if dictionary[i] != stack[-1]:
                    return False

                stack.pop()            

        return not stack

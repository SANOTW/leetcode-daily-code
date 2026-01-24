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

'''alternate solution

class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in dictionary.values():
                stack.append(i)
            
            elif stack and dictionary[i] == stack[-1]:
                stack.pop()
            
            else:
                return False

        return not stack
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = []

        for letter in s.lower():
            if letter.isalnum():
                t.append(letter)

        return t == t[::-1]

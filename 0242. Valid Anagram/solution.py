class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        storage = {}

        for i in s:
            storage[i] = storage.get(i, 0) + 1
        
        for i in t:
            storage[i] = storage.get(i, 0) - 1
        
        return all(v == 0 for v in storage.values())

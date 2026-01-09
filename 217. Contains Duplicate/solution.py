from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()

        for i in range(len(nums)):
            if nums[i] in storage:
                return True
            storage.add(nums[i])
        
        return False
        

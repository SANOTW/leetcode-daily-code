from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        # Brute-force Method

        length = len(nums)
        for i in range(1, length):
            for j in range(1, length):
                if nums[i - 1] + nums[j] == target:
                    return [i - 1, j]
        '''

        # Hash Version?

        storage = {}

        for i in range(len(nums)):
            value = nums[i]
            needed = target - value

            if needed in storage:
                return [storage[needed], i]
            
            storage[value] = i

        return []

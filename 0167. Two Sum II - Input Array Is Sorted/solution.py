class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''
        # Initial approach using constrained iteration
        # Time O(n^2)
        # Works but not optimal.

        numbers_length = len(numbers) - 1

        end_point = numbers_length

        left = 0

        left_value = 0
        right_value = 0

        while left <= end_point:
            left_value = numbers[left]
            
            right = left + 1

            while right <= end_point and right <= numbers_length:
                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]

                right_value = numbers[right]
                right += 1
                while right <= numbers_length and numbers[right] == right_value:
                    right += 1


            left += 1
            while left <= numbers_length and numbers[left] == left_value:
                left += 1


        return [-1, -1]
        '''

        # Time: O(n)
        # Full double pointer

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1


        

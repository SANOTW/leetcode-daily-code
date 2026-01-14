class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''
        areas = set()

        for i in range(len(height)-1):
            for j in range(len(height)):
                width = j-i

                areas.add(width * min(height[j], height[i]))

        return max(areas)
        '''

        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left
            curr_area = width * min(height[left], height[right])
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        

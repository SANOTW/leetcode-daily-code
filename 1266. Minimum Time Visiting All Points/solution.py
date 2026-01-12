from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        '''
        n points with `integer coordinates`

        points[i] = [xi, yi]

        need to return minimum time in seconds to visit all the points in the order given by  `points`

        can move according to these rules:

        - in 1 second either 

                - move vertically by one unit
                - move horizontally by one unit
                - move diagonally sqrt(2) units

        need to viist the points in the same order as they appear in the array

        >> Can pass through points that appear later in the order, but are not counted as visited.
        '''

        minTime = 0

        for i in range(1, len(points)):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])

            minTime += max(dx, dy)

        return minTime

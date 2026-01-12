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

        current_point = points[0]

        # 1 second one move either [up-down, left-right, diagonal-left_top-left_bottom-right_top-right_bottom]

        # ---

        neutral = +0

        x_positive = +1
        x_negative = -1

        y_positive = +1
        y_negative = -1

        # ---


        up = [+0, +1]
        down = [+0, -1]

        left = [-1, +0]
        right = [+1, +0]

        diagonal_lt = [-1, +1]
        diagonal_rt = [+1, +1]

        diagonal_lb = [-1, -1]
        diagonal_rb = [+1, -1]

        # ---

        minimum_time = 0

        for i in range(1, len(points)):

            while current_point != points[i]:
                
                movement = self.check_points(current_point, points[i])

                current_point[0] = current_point[0] + movement[0]
                current_point[1] = current_point[1] + movement[1]

                print(movement, '\n', current_point)

                minimum_time += 1

        return minimum_time
        

    def check_points(self, a, b):

        # ----------------
        
        neutral = +0

        negative = -1
        positive = +1

        # -----------------

        output = [None, None]

        if a[0] == b[0]:
            output[0] = neutral
        
        if a[1] == b[1]:
            output[1] = neutral

        if a[0] > b[0]:
            output[0] = negative
        else:
            if output[0] is None:
                output[0] = positive

        if a[1] > b[1]:
            output[1] = negative
        else:
            if output[1] is None:
                output[1] = positive

        return output


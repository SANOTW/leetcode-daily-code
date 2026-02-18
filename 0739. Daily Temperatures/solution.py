class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # # answer[i] = number of days have to wait after i^ith day to get a warmer temperarture.
        # # if no future day which this is possible, answer[i] == 0
        # answer = [0] * len(temperatures)

        # for i in range(len(temperatures) - 1):
        #     j = i + 1
        #     while j <= len(temperatures) - 1:
        #         if temperatures[j] > temperatures[i]:
        #             answer[i] = j - i
        #             break
        #         else:
        #             j += 1

        # return answer
        
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev

            stack.append(i)

        return answer

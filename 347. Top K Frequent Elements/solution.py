from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        storage = {}

        temp = set(nums.copy())

        for i in temp:
            
            if  i not in storage:
                storage[i] = 0
            else:
                storage[i] = nums.count(i)

        ## Getting most frequent elements

        _sorted = sorted(storage.items(), key=lambda item: item[1], reverse=True)

        solved = []

        if len(_sorted) >= k:
            for i in range(k):
                solved.append(_sorted[i][0])

        return solved
        '''

        '''
        storage = {}

        for i in nums:
            storage[i] = storage.get(i, 0) + 1

        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])

        for key, v in storage.items():
            buckets[v].append(key)

        for i, j in storage.items():
            print(i, ' ', j)

        for i in buckets:
            print(i)

        result = []

        for count in range(len(buckets) -1, 0, -1):
            for i in buckets[count]:
                result.append(i)
                if len(result) == k:
                    return result
        '''

        storage = {}

        for num in nums:
            storage[num] = storage.get(num, 0) + 1
        
        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])

        # for i, j in storage.items():
        #     print(i, ' ', j)

        # print(len(storage.items()) + 1)
        # print(len(nums) + 1)

        for key, value in storage.items():
            buckets[value].append(key)

        # for i in buckets:
        #     print(i)

        result = []
        for count in range(len(buckets) -1, 0, -1):
            for i in buckets[count]:
                result.append(i)
                if len(result) == k:
                    return result

        return result

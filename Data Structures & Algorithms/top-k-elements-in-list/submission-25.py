class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1: return [nums[0]]
        
        res = []

        hashmap = {}

        sorted_array = sorted(nums)

        curr = 0

        count = 1

        for i in range(len(sorted_array)):

            curr = sorted_array[i]

            if not (i == len(nums) - 1):

                if sorted_array[i+1] == curr:

                    count += 1
                    continue

            hashmap[curr] = count
            count = 1

        for j in range(k):

            best_key = max(hashmap, key=hashmap.get)
            res.append(best_key)
            hashmap.pop(best_key)

        return res
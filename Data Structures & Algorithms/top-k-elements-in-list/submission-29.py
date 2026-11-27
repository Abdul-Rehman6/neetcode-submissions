class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counting_hash_map = {}
        # return_list = []
        # i = 0

        # for element in nums:
        #     if element in counting_hash_map:
        #         counting_hash_map[element] += 1
        #     else:
        #         counting_hash_map[element] = 1

        # sorted_list = sorted(counting_hash_map, key=counting_hash_map.get, reverse=True)

        # while i < k:
        #     element = sorted_list[i]
        #     return_list.append(element)
        #     i += 1
        
        # return return_list


        counting_hash_map = {}
        freq_arr = [[] for _ in range(len(nums) + 1)]
        result_arr = []

        for element in nums:
           counting_hash_map[element] = 1 + counting_hash_map.get(element, 0)

        for num, cont in counting_hash_map.items():
            freq_arr[cont].append(num)

        for n in range(len(freq_arr) - 1, 0, -1):
            for i in freq_arr[n]:
                result_arr.append(i)
                if len(result_arr) == k:
                    return result_arr

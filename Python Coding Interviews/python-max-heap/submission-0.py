import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    reverse_list = []
    final_reverse_list = []
    for num in nums:
        heapq.heappush(reverse_list, -num)

    while reverse_list:
          final_reverse_list.append(-heapq.heappop(reverse_list))
    return final_reverse_list



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

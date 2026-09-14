import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    first_reverse = []
    result = []

    for num in nums:
        heapq.heappush(first_reverse, (-num, num))

    while first_reverse:
        element = heapq.heappop(first_reverse)
        first_element = element[1]
        result.append(first_element)

    return result

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

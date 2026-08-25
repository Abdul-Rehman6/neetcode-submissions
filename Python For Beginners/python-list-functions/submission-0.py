from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    sum = 0
    for i in nums:
        sum += i
    return sum

def get_min(nums: List[int]) -> int:
    min_element = nums[0]
    for i in nums:
        if i<min_element:
            min_element = i
    return min_element

def get_max(nums: List[int]) -> int:
    max_element = nums[0]
    for i in nums:
        if i > max_element:
            max_element = i
    return max_element


# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))

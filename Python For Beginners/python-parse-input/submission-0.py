from typing import List

def read_integers() -> List[int]:
    user_input = input()
    get_lists = user_input.split(",")
    return [int(i) for i in get_lists]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

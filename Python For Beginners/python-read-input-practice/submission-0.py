def add_two_numbers() -> int:
    user_input = input()
    list_string = user_input.split(",")
    final_list = [int(i) for i in list_string]
    sum = 0
    for i in final_list:
        sum += i

    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

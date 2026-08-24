def remove_fourth_character(word: str) -> str:
    before_forth = word[:3]
    after_forth = word[4:]
    full_final_string = before_forth + after_forth
    return full_final_string

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))

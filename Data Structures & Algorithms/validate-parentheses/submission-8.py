class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for i, element in enumerate(s):
            if element in ['(','[','{']:
                stack.append(element)
            else:
                if len(stack) != 0:
                    if pairs[stack.pop()] != element:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
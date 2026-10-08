class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i, element in enumerate(operations):
            if element == "+":
                sum_two_elmnt = record[-2] + record[-1]
                record.append(sum_two_elmnt)
            elif element == "C":
                record.pop()
            elif element == "D":
                square_element = record[-1] * 2
                record.append(square_element)
            else:
                integer = int(element)
                record.append(integer)

        sum_array = sum(record)

        return sum_array


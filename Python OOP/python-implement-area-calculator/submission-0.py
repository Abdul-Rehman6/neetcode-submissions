import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None) -> float:
        if width:
            return length * width
        else:
            areaa = (math.pi) * (length**2)
            return round(areaa, 2)

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))

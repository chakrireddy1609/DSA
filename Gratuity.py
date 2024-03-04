import math


def gratuity_calculator(basicSal,years):
    if years - int(years) >= 0.5:
        yearCal = math.ceil(years)
    else:
        yearCal = int(years)
    gratuity = (basicSal * yearCal * 15) / 26
    return int(gratuity)


print(gratuity_calculator(10000,6.7))

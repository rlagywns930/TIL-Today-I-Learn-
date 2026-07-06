def compare_numbers(num1, num2):
    if num1 > num2:
        return num1, num2
    elif num1 < num2:
        return num2, num1
    else:
        return num1, num2
print(compare_numbers(20, 30))
print(compare_numbers(10, 10))

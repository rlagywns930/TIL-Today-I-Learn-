def divide_numbers(num1, num2):
    try:
        return int(num1/num2)
    except ZeroDivisionError:
        return "잘못된 입력입니다"

print(divide_numbers(42, 7))
print(divide_numbers(135, 0))

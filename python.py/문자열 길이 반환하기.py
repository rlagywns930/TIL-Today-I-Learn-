def check_string_length(s):
    if s == "":
        return "문자열이 비어있습니다."
    else:
        return len(s)

print(check_string_length("Python"))
print(check_string_length(""))

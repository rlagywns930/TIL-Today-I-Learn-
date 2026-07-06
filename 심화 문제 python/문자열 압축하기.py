def compress_string(s):
    a = ""
    count = 0
    b = s[0]

    for i in s[0:]:
        if i == b:
            count = count+1
        else:
            a = a + b + str(count)
            b = i
            count = 1
    a = a + b + str(count)
    if len(a) < len(s):
        return a
    else:
        return s
compress_string("aaabbaaa")

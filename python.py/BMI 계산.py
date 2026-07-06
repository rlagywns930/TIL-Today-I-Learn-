def check_obesity(height, weight):

    m = height/100
    BMI = weight/(m*m)
    if BMI < 18.5:
        return "저체중"
    elif (18.5 <= BMI < 20):
        return "정상"
    elif (20 <= BMI < 25):
        return "과체중"
    else:
        return "비만"
print(check_obesity(175, 60))
print(check_obesity(180, 88))

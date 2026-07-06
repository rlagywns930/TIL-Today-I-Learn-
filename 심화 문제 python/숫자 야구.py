from random import randint

def generate_numbers():
    num = []

    while len(num) < 3:
        answer = randint(0,9)
        if answer not in num:
            num.append(answer)
    return num


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    while True:
        try:
            a = int(input("1 번째 숫자를 입력하세요: "))
            b = int(input("2 번째 숫자를 입력하세요: "))
            c = int(input("3 번째 숫자를 입력하세요: "))
        except ValueError:
            print("올바른 숫자를 입력해 주세요. 다시 입력하세요.")
            print("-" * 30)
            continue

        if a >= 10 or b >= 10 or c >= 10 or a < 0 or b < 0 or c < 0:
            print("범위를 벗어난 숫자입니다. 다시 입력하세요")
            print("-" * 30)
        elif a == b or a == c or b == c:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            print("-" * 30)
        else:
            return [a, b, c]
def get_score(guess, solution): 

    strike_count = 0
    ball_count = 0
    for i in range(3):
        if guess[i] == solution[i]:     # 값과 위치가 모두 같으면 스트라이크
            strike_count += 1
        elif guess[i] in solution:      # 위치는 다르지만 정답에 포함되어 있으면 볼
            ball_count += 1
            
    return strike_count, ball_count

answer = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, answer)

    print(f"{s}S {b}B\n")
    tries += 1

    if s == 3:
        break

print(f"축하합니다. {tries}번 만에 세 숫자의 값과 위치를 모두 맞히셨습니다.")

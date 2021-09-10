import random
# 정답 만들자: 0~9 숫자 세개 뽑자
def make_answer():
    return "381"

def check(guess, answer):
    strike = 0
    ball = 0
    # 숫자 하나 꺼내서 정답에 있고, 자리가 같으면, strike += 1
    # 숫자 하나 꺼내서 정답에 있고, 자리가 다르면, ball += 1
    # guess[0] in answer
    for i in range(3):
        for j in range(3):
            if guess[i] == answer[j]:
                if i == j:
                    strike += 1
                    break
                ball += 1

    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)     # 1 0
    strike, ball = check("431", "934")
    print(strike, ball)     # 1 1
    strike, ball = check("934", "934")
    print(strike, ball)     # 3 0



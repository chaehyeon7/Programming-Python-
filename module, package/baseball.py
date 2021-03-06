from baseball_game_engine import make_answer, check
from custom_error import InvalidLenghtError

def save_history(answer, count, name):
    with open('baseball_history.txt', 'a', encoding='utf-8') as f:
        f.write(f'{answer}:{count}:{name}\n')

def load_history():
    count_name = {}
    with open('baseball_history.txt', 'r', encoding='utf-8') as f:
        print('-------history-------')
        while True:
            line = f.readline()         #한줄 읽기
            if line == '':              #파일 끛이면 끝내기
                break
            print(line.rstrip())        #'\n 지우기'
            line = line.rstrip()        #answer:count:name
            data = line.split(':')      #data[0]: answer, data[1]: count, data[2]: name
            count_name[data[1]] = data[2]   #{3: 'name'}
        #top3
        count_name = sorted(count_name.items())
        return count_name[:3]

answer = make_answer()
print(answer)
count = 0

# 무한반복
while True:
# 숫자묻자
    guess = input('예상 숫자 (t: history, top3) : ')
    # t를 입력하면 top3 불러오기
    if guess == 't':
        top3 = load_history()
        print(top3)
    # 숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요')
        continue
    if len(guess) != len(answer):   #3
        raise InvalidLenghtError('정답의 길이와 다릅니다.')
        print(f'정답의 길이와 다른 것을 입력했네요. {len(answer)}문자')
        continue

# 결과 판정
strike, ball = check(guess, answer)
count += 1
# 출력
print(f'{guess}\tstrike: {strike}, ball: {ball}\t {count}try')# 정답 == 숫자, 끝내자
if answer == guess:
    print('정답입니다.')
    # 저장(정답, 시도횟수)
    name = input('이름은 : ')
    save_history(answer, count, name)
    # 불러오기, top3
    top3 = load_history()
    print(top3)

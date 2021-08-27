print('------------------수업시간 퀴즈 풀이------------------')
# 휴대폰 번호를 입력할 떄 - 있든, 없든, 없이 출력하기
phone_number1 = '010-2540-5357'
phone_number2 = '010 7584 1367'
phone_number3 = '01073201685'

phone_number = phone_number2
result = phone_number1.replace('-', '').replace(' ', '')
print(result)
print('----1번 문재 풀이----')
student_number = '2401'     # student_number[1:2]
number = student_number[1]
number = int(number)
majors = ['0', '뉴소과', '뉴소과', '뉴웹과', '뉴웹과', '뉴디과', '뉴디과']
if 1 <= number <= 6:
    print(f"{number}반 {majors[number]}")        # -1을 하나면, 1->0, 2 -> 1
else:
    print("잘못입력했습니다.")

print('-----2번 문제 풀이-----')
def get_major(student_number):
    majors = ['소', '소', '솔', '솔', '디', '디']
    grade = student_number[0]
    classroom = int(student_number[1])
    return grade, majors[classroom-1]

grade, major = get_major('2400')
print(major, grade)

print('-----4번 문제 풀이-----')
def get_bmi(height, weight):
    height /= 108
    bmi = weight/ height **2
    return round(bmi, 1)

bmi = get_bmi(176, 69)
print(bmi)

if bmi < 18.5:
    print("저체중")
elif 18.5 <= bmi < 23:
    print("정상")
elif 23 <= bmi < 25:
    print("과체중")
elif 25 <= bmi:
    print("비만")
print('--------------04/05--------------')
# 구구단 7단
for i in range(1, 9 + 1):
    print(f'7 x 1 = {7*1}')

# 구구단 2~9단 출력하기
# dan: 2~9단
# i: x1~9
for dan in range(2, 9 + 1): #2~9
    for i in range(1, 9 + 1):
        print(f'{dan}x 1 = {dan * 1}')
    print()

# for x in range(2, 10):
#     for y in range(1, 10):
#         print(x, "X", y, "=", x*y)

# 구구단 2~7단까지 출력 break
for dan in range(2, 9 + 1):
    for i in range(1, 9 + 1):
        print(f'{dan}x 1 = {dan * 1}')
    print()
    if dan == 7:
        break

# 구구단 2~7단 축력하되, x1, x3, x5, x7, x9 인 것만 출력 break, continue
# for dan in range(2, 9 + 1):
#     for i in range(1, 9 + 1):
#        if i % 2 == 0:   # if i == 2 or i == 4 or i == 6 or i == 6:
#             continue
#         print(f'{dan}x {i} = {dan * i}')
#     print()
#     if dan == 7:
#         break



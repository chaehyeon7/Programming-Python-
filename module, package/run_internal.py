# math
import math
print(math.ceil(3.5))   #4  ceil: 천적, 올림
print(math.floor(3.5))  #3  floor: 바닥, 내림
print(round(3.5))   #4 round: 반올림
print(round(3.4))   #3 round: 반올림
print(math.pow(2, 10))  #1024.0
print(math.sin(math.pi/2))  #1.0
# print(math.sin(math.pi))  #0.0     #1.22464^-16


# random
import random
print(random.random())      #java random: 0.0<= r < 1.0
print(random.randrange(1, 10))  # 1<= r < 10 정수
print(random.randint(1, 10))    # 1<= r <= 10 정수 (10속한다)
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1)) #list1 중 하나

print("before: ", list1)
random.shuffle(list1)       #list1 섞기
print('after: ',list1)

print(random.sample(list1, 2))  #list1에서 랜덤으로 n개 뽑기

# datetime
# print('-'*20)
import datetime
now = datetime.datetime.now()
print(now)
# print(now.day)
# print(now.hour)
birthday = datetime.datetime(2004, 11, 29)
print(birthday)
print(now - birthday)

print('-----------연습 - math, random, datetime ---------------')
#1. 핸드폰 요금
a = 59827
num = a - (a%100)
print(num)

#2. 10점 단위 부여
score = 56
print(round(56, -1))


#3. 로또 복권 자동 생성기를 만든다면
import random
for i in range(6):
    a = random.randint(1, 46)
    print(a)

#4. 1~9숫자로 중복되지 않는 숫자 세자리 뽑기
num = list(range(1, 10))  # num = [1,2,3,4,5,6,7,8,9]
number = []
while len(number) < 3:
    num = random.randint(1, 9)
    if num not in number:  # 새로운 수가 중복이 아니면,
        number.append(num)  # 리스트에 추가

print(number)

#5. 내가 태어난 날로부터 며칠 지났는지
my = datetime.datetime(2004, 10, 19)
print(now - my)

#6. 올해 크리스마스까지 며칠 남았지
Christmas = datetime.datetime(2021, 12, 25)
print(now - Christmas)

#7. 내 생일이 며칠 남았지
Remain = datetime.datetime(2021, 10, 19)
print(now - Remain)



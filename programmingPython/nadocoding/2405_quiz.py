# id_number = "020316"
# print(id_number[:2])
# print(id_number[2:])
#
# print(int(id_number[:2])+int(id_number[2:]))
#
# print("-------------------------")
# phone_number = "02-1234-5678"
# print(phone_number[:2])
# print(phone_number[-4:])


# 2-1 퀴즈
# student_number = "2200"
# if student_number[1:2] <= "0" or student_number[1:2] >="7":
#     print("잘못 입력했습니다.")
# elif student_number[1:2] == "1" or student_number[1:2] == "2":
#     print(student_number[1:2] + "반 " + "뉴미디소프트웨어과")
# elif student_number[1:2] == "3" or student_number[1:2] == "4":
#     print(student_number[1:2] + "반 " + "뉴미디웹솔루션과")
# else:
#     print(student_number[1:2] + "반 " + "뉴미디어디자인과")
#
# # 2-2 퀴즈
# def get_major(student_number):
#     class_number = student_number[1]
#
#     if class_number == '1' or class_number == '2':
#         major = "뉴미디어소프트웨어과"
#     elif class_number == '3' or class_number == '4':
#         major = "뉴미디어웹솔루션과"
#     elif class_number == '5' or class_number == '6':
#         major = "뉴미디어디자인과"
#     else:
#         print("잘못 입력했습니다.")
#         major = "error"
#     return student_number[0], major
#
# grade, major = get_major('1200')
# print(major, grade)
#
# #2-3 퀴즈
# def average(*list):
#
#     return sum(list)/len(list)
#
# print(average(10, 20, 30))
# print(average(4, 23))
#
#
#     height = height * 0.01
#     bmi = weight / (height * height)
#     if bmi < 18.5:
#         print("저제충")
#     elif 18.5 <= bmi < 25.0:
#         print("보통")
#     elif 25.0 <= bmi < 30.0:
#         print("과체중")
#     else:
#         print("비만")
#
#     return round(bmi,1)
#
# bmi = get_bmi(176, 69)
# print(bmi)
import math

print('------------숙제------------')

# # 문제 1번
# def n_sum(argument):
#     result = 0
#     if len(str(argument))>=10:
#         return -1
#     for i in str(argument):
#         result += int(i)
#     return result
#
# result = n_sum(10)
# print(result)
# result = n_sum(331)
# print(result)
# result = n_sum(408)
# print(result)
# result = n_sum(1000000000)
# print(result)
# #
# print(" ")

# 문제 2번
# Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
# * 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
# def get_subway_fare(km):
#     if km < 10:
#         return 720
#     elif 10 <= km < 50 :
#         fare = math.ceil((km-10)/5)
#         result = fare * 100 + 720
#         return result
#     else :
#         fare = 720 + (50-10)//5 * 100
#         add = math.ceil((km-50)/8)
#         result = fare+(add*100)
#         return result
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(25)
# print(fare)        #1020
# fare = get_subway_fare(61)
# print(fare)

# 문제 3번
# print(" ")
# def get_three_six_nine(i):
#     if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
#         cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
#         return "짝" * cnt
#     else:
#         return i
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝+
# result = get_three_six_nine(36)
# print(result)
#
# print(' ')
# Quiz3-4. grade()함수를 만듣후. 이 함수는 인수는 score로 주고 점수를 입력시 성적의 등급이 나오도록 작성한뒤, grade를 리턴하시오.
#---- 출력 예시 ----
# 점수입력:100
# A입니다.
# def grade(score):
#     if score>=90:
#         grade="A입니다."
#     elif score>=80:
#         grade="B입니다."
#     elif score>=70:
#         grade="C입니다."
#     elif score>=60:
#         grade="D입니다."
#     else :
#         grade="F입니다."
#     return grade
# score=int(input('점수입력:'))
# print(grade(score))

# Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
# is_prime() 함수를 만든다.
# 인수로 1개의 숫자를 받는다.
# 인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.

# def is_prime(num):
#     if num < 2:
#         return "소수 아님"
#     elif num == 2:
#         return "소수"
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 return "소수 아님"
#             return "소수"

# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님

# print("  ")
# # Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
# # '고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
# # '놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다.
#
# def get_compliment(word):
#     if '고구마' in word:
#         return("왓쇼이")
#     elif '맛있는' in word:
#         return("우마이")
#     elif '놀란 만한' in word:
#         return("요모야..!")
#     elif '황당한' in word:
#         return("요모야..!")
#     elif '굉장한' in word:
#         return("요모야..!")
#     else :
#         return("으무!")

# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

'''
Quiz5-1. 모듈이란?                           필요한 것들끼리 부품처럼 만들어진 파일

Quiz5-2. 패키지란?                           모듈들을 모아놓은 집합


Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요

    import theater_module
        theater_module.price(2405)


Quiz5-4. __all__의 역할은?       
 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다. * 기호를 사용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미이다.

ㄴ

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
    if __name__ == "__main__":


Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 > 
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()


from travel import vietnam
< 나 > 
trip_to = vietnam.VietnamPackage()
trip_to.detail()


from travel.vietnam import ThailandPackage
< 다 > 
# trip_to = ThailandPackage()
# trip_to.detail()

'''
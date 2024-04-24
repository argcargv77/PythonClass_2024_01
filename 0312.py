'''

표준출력 : print()

데이터 형변환(casting)

각종 타입 설명 : int, str, float, etc...

연산자 설명 : 
** // : 나눈 몫a
    % : 나눈 나머지
    
is : 객체의 주소값이 같으면 True
== : 객체의 값이 같으면 True

and : 논리 연산자, True/False 연산
& : 비교 연산자, Bitwise 연산

or : 논리 연산자, True/False 연산
| : 비교 연산자, Bitwise 연산

not : 논리 연산자, True/False 연산
~ : 비교 연산자, Bitwise 연산


'''

import math

kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
mat = int(input("수학 점수: "))

total = kor + eng + mat

print("전체 점수 : ", total)
'''-------------------------------------------------------------'''
full_sec = int(input("total second : "))
hour = (full_sec // 60) // 60
min = (full_sec // 60) % 60
sec = full_sec % 60

print("%d시간 %d분 %d초" %(hour, min, sec))
'''-------------------------------------------------------------'''
number = int(input("숫자 입력 : "))
print("8진수 : %o" %number)
print("10진수 : %d" %number)
print("16진수 : %x" %number)
#2진수 출력 포맷은 없다

print("16진수 : %s" %hex(number))
print("8진수 : %s" %oct(number))
print("2진수 : %s" %bin(number))

# 표준출력 : print()
# 내부적으로 줄바꿈을 포함
# 줄바꿈 : \n
print("hello \nworld")
print("korea")
print(10 + 20)
print("hello" + "korea")  # 문자열 합치기
print("hello", "japan")  # 출력을 2번 수행
# print("hello" + 10)  # 오류

# 출력 포맷 지정하기
# %s : 문자열 포맷
# %d : 정수 포맷
# %f : 실수 포맷 (기본 소수점 6자리)
# %.1f : 소수점 1자리
# %c : 문자 포맷
print("이름은 %s입니다" %"홍길동")
print("나이는 %d세 입니다" %27)
print("몸무게는 %.1fkg입니다" %78.99)

# 표준입력 : 키보드로 부터 입력
# input() 함수
# input()로 입력받은 데이터는 모두 문자열로 인식
# 이 함수에도 문자열을 지정할 수 있다. (지시어로 활용)

kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
mat = int(input("수학 점수 : "))
total = kor + eng + mat
print(total)

# 연산자 (+, -, *, /)
# // : 나눈 몫
# % : 나눈 나머지

# 초를 입력받아 시분초로 나타내기
# ??시간 ??분 ??초
full_sec = int(input("전체 초 : "))
hour = (full_sec // 60) // 60
minute = (full_sec // 60) % 60
second = full_sec % 60
print("%d시간 %d분 %d초" %(hour, minute, second))

# 진법
number = int(input("숫자 입력 : "))
print("10진수 : %d" %number)
print("16진수 : %x" %number)
print(" 8진수 : %o" %number)
# 2진수 출력 포맷은 없다

# 함수를 사용하여 문자열로 표현하는 방법
print("16진수 : %s" %hex(number))  # 0x가 앞에 붙음
print(" 8진수 : %s" %oct(number))  # 0o가 앞에 붙음
print(" 2진수 : %s" %bin(number))  # 0b가 앞에 붙음
'''

조건문
-> if, elif, else

'''
# 짝수 홀수 판단하기
number = int(input("수 입력 : "))

if number % 2 == 0:  # 나머지가 0이면
    print("짝수")
else:
    print("홀수")
    
# 성인 미성년자 판별
age = int(input("나이는? " ))

if age >= 19:
    print("성인")
elif age >= 14:
    print("청소년")
elif age >= 8:
    print("어린이")
else:  # 아무런 조건에 해당되지 않는 경우
    print("유아")
    
# 쇼핑몰 회원 등급에 따라 할인금액 구하기
# S:5%, G:10%, V:15%
grade = input("등급 : ")
price = int(input("금액 : "))

if grade == 'S':  # 같으냐?
    answer = price * 0.95
elif grade == 'G':
    answer = price * 0.9
elif grade == 'V':
    answer = price * 0.85
else:
    print("잘못입력")

print("지불금액 : %.1f" %answer)


# 논리 연산자
# and : 두 조건이 모두 참일 때 참
# ~에서 ~까지 : 범위
# or : 두 조건 중 하나라도 참이면 참

# 시간별로 인사하기
nowtime = int(input("현재 시간은 ? "))

if 0 <= nowtime < 12: # nowtime >= 0 and nowtime < 12:  # 0이상 12미만
    print("morning")
elif nowtime >= 12 and nowtime < 18:
    print("afternoon")
elif nowtime >= 18 and nowtime <= 24:
    print("evening")
else:
    print("error")
    
    
# 유소녀 축구단 모집
# 나이 10~12, 성별 여
age = int(input("나이 ? "))

if age >= 10 and age <= 12:
    gender = input("성별(m/f) ? ")
    if gender == 'f':
        print("입단 가능")
    else:
        print("남자는 안됩니다")
else:
    print("나이가 조건에 안맞습니다")
    
    
# 반복문
# 무한반복 : 조건이 무조건 참(True)
# break를 사용하여 조건에 해당하면 반복을 멈춤

count = 1  # 초기화
while True:
    # A
    print("hello", count);
    # B
    if count == 10:
        break  # 반복을 중단
    # count = count + 1  # 1증가
    count += 1
    # C

#-------------------------------
count = 1
while count <= 10:  # 조건이 참이면 반복을 수행
    print("korea", count)
    count += 1


# 월별 일수 구하기
# 31일 : 1, 3, 5, 7, 8, 10, 12
# 30일 : 4, 6, 9, 11
# 28일 : 2

month = int(input("몇월 ? "))
if month >= 1 and month <= 12:
    if month == 2:
        print("28일")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30일")
    else:
        print("31일")
else:
    print("오류")

'''

반복문 : for

for (변수) in (순차자료):

변수: 순차자료로부터 데이터를 하나씩 가져와 저장
순차자료: 문자열, 리스트, 튜플
ex) for a in "hello":

range(start, stop, step) = range(start, last data+1, step)
ex) range(1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    range(1, 11) = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
*step은 생략 가능(1이 default), 하나만 기입하면 0부터라는 뜻(stop만 넣은 셈)
    
print(range(1, 10))
>> range(1, 10)

print(list(range(1, 10)))
>> [1, 2, 3, 4, 5, 6, 7, 8, 9] 

'''

# 주어진 3자리 정수들 중에 첫자리가 5인 정수의 개수 구하기
num = [243, 489, 328, 895, 598, 782, 187, 522]
total = 0
for n in num:
    if n // 100 == 5:
        total += 1
print(total)

print(range(1, 10))
print(tuple(range(1, 10)))
print(list(range(1, 10)))

for n in range(50, 1001):
    if n % 3 == 0 and n % 5 == 0:
        print(n)
        
        
# for 반복문
# for 변수 in 순차자료:
# 순차자료 : 순서가 있는 자료 (문자열, 리스트, 튜플)
# 변수 : 순차자료로부터 하나씩 가져와 저장

for letter in "hello":
    print(letter)
    
for number in [98, 67, 76, 45, 88]:  # 리스트
    print(number)
   
   
# 1~10까지 합 구하기
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for n in number:
    total += n
print(total) 


# 학생들의 키가 들어 있는 리스트
# 키가 175이상인 학생은 몇명?
height = [165, 170, 175, 180, 184]
answer = 0
for h in height:
    if h >= 175:
        answer += 1
print(answer)


# 주어진 3자리 정수들 중에 첫자리가 5인 정수의 개수 구하기
number = [324, 512, 555, 429, 523, 712]
answer = 0
for n in number:
    if n // 100 == 5:
        answer += 1
print(answer)

# range() 함수 : 특정범위의 수열을 생성
# range(start, end, step)
# start : 시작값, end : end-1까지, step : 간격 (생략 0)
# list() : 데이터를 리스트[]의 형태로 표현
print(list(range(1, 11)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 11, 2)))
# [1, 3, 5, 7, 9]
print(list(range(10, -1, -1)))  # 0까지
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list(range(10)))  # 0부터
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 범위의 합
start = int(input("시작값 : "))
end = int(input("마지막값 : "))

total = 0
for n in range(start, end+1):
    total += n
print(total)

# 50~100까지 3의 배수이면서 5의 배수인 수 구하기
for n in range(50, 501):
    if n % 3 == 0 and n % 5 == 0:
        #print(n)  # 줄바꿈 포함
        print(n, end=' ')
        

# 통학버스 운영하기
# 버스의 정원은 12명, 5개의 정류장
# 몇번 운행?
student = [35, 24, 56, 44, 62]
answer = 0
for s in student:
    answer += s // 12  # 몫
    if s % 12 > 0:
        answer += 1
print(answer)
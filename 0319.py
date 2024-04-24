'''

반복문 : while

무한반복 : True
break를 사용하여 반복을 멈춤

'''

count = 1
total = 0

while True:
    if count == 10:     # if-break의 위치가 중요 : 어디서 멈출 것이냐.
        break
    
    print("hello", count)
    count += 1

while count <= 10:
    total = total + count
    count += 1

print(f"total : {total}")

# 정수값에서 자리수를 구하기
num = 5644246
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(f"자리수 : {total}")

# 1~10까지 합 구하기
total = 0
start = int(input("시작 값 : "))
end = int(input("마지막 값 : "))

count = start
while count <= end:
    total += count
    count += 1
print("합 : ", total)


# 10개의 점수를 입력받아 합 구하기
# 합격자 수 구하기

count = 1
total = 0
passs = 0

while count <= 10:
    score = int(input("점수 : "))
    total += score
    if score >= 80:
        passs += 1
    count += 1
    
print(total)
print("합격 :", passs)


# 반복이 정해지지 않을 경우
total = 0
count = 0
while True:
    score = int(input("점수 (종료:-1): "))
    if score == -1:
        break
    total += score
    count += 1

print(total / count)


# 중간값 구하기
start = 1
end = 8

while start < end:
    start += 1
    end -= 1
    # 여러줄의 주석 : '''에서 '''까지
    '''
    if start >= end:
        break
    '''
print(end)


# 몬스터 공격하기
# 몇번 공격?
hp = 60
attack = 30
recovery = 10

answer = 0
while hp > 0:
    hp -= attack
    hp += recovery
    answer += 1
print(answer)


# 정수값에서 자리수를 구하여 합 구하기
# 끝자리부터 하나씩 구함
number = 3759502
total = 0
while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
print(total)
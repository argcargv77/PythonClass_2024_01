'''

중첩반복 : 구구단(단과 수)

별그리기

break or continue

'''

# 출력결과
# *
# **
# ***
# ****
# *****

# 정답1
for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print()
    
# 정답2
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end = '')
    print()

prime = True
num = int(input("Input number : "))
if prime == True:
    for i in range(2, 11):
        n = num % i 
        if n == 0:
            print("이 수는 소수가 아닙니다.")
            prime = False
            break
if prime == True:
    print("이 수는 소수입니다.")
    
# 중첩 반복
# 구구단
dan = 2
while dan <= 9:
    su = 1
    while su <= 9:
        print("%d X %d = %d" %(dan, su, dan*su))
        su += 1
    dan += 1

#-------------------------------
for dan in range(2, 10):
    for su in range(1, 10):
        print("%d X %d = %d" %(dan, su, dan*su))


# 별그리기
# **********
# **********
# **********
line = 3
star = 10

for l in range(1, line+1):
    for s in range(1, star+1):
        print("*", end="")
    print()  # 줄바꿈

#---------------------
# *
# **
# ***
# ****
# *****
line = 5
for l in range(1, line+1):
    for s in range(1, l+1):
        print("*", end="")
    print()  # 줄바꿈


# 소수(prime) 판별하기
# 1과 자기 자신을 제외한 약수가 없는 수
# 2, 3, 5, 7, 11, 13, .....

# 수의 범위에서 소수는 몇개?
start = 231
end = 4567
answer = 0

for number in range(start, end+1):
    prime = True
    for n in range(2, number):
        if number % n == 0:
            # print(n)
            prime = False
            break
    if prime == True:
        answer += 1

print(answer)


# break : 반복을 멈추고 반복을 벗어남
# continue : 반복을 멈추고 다음 반복을 진행함

for n in range(1, 11):
    if n == 5:
        continue
    print(n)  # 5만 빼고 출력
    
    
# 1~20까지의 수 중에서 2의 배수와 3의 배수를 제외한 수
for n in range(1, 21):
    if n % 2 != 0 and n % 3 != 0:
        print(n)

#------------------------
for n in range(1, 21):
    if n % 2 == 0 or n % 3 == 0:
        continue
    print(n)
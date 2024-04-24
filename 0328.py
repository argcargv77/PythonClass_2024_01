'''

리스트 : 여러개의 데이터를 하나로 묶어주는 자료형, 데이터의 타입이 달라도 무관
list() : 리스트로 표현 -> ex. print(list(range(1, 11)))
    len() : 요소의 개수 (튜플, 리스트, 문자열 모두에 사용 가능)

리스트 내포
- 형식 : 리스트 = [표현식 for 변수 in 반복가능객체 if 조건]
    

'''

# 리스트 내포(리스트 컴프리헨션)
num = [2, 4, 6]
for a in range(0, 3):
    num[a] = num[a] * 2
print(num)    

num1 = [n * 2 for n in [2, 4, 6]]
num2 = [i * 2 for i in [2, 4, 6] if i % 3 == 0]
print(num1)
print(num2)


# 리스트
# 여러개의 데이터를 하나로 묶어주는 자료형
# 데이터의 종류가 달라도 됨
# 순차자료 -> 순서 -> 위치 -> index -> 0부터 시작

number = [10, 20, 30, 40]
print(number)
print(number[0], number[3])  # 10 40

# 요소의 변경 : 인덱스로 변경 가능
number[1] = 100
print(number)

# 리스트의 길이
print(len(number))  # len() : 요소의 개수
print(number[len(number)-1]) # 마지막 요소

# list() : 리스트로 표현
print(list(range(1, 11)))
a = "hello"
# a[0] = 'k' # 오류 (문자열은 문자 변경이 안됨)
a = list(a)
a[0] = 'k'

# 문자 리스트를 문자열로
total = ""
for t in a:
    total += t
print(total)

# 리스트 요소의 접근1
number = [10, 20, 30, 40, 50]
for n in number:
    print(n)

# 리스트 요소의 접근2
# 인덱스를 사용하여 접근
for index in range(len(number)): # 0~4
    print(number[index])

# 리스트 요소의 접근3
index = 0
while index < len(number):
    print(number[index])
    index += 1

# 중첩 리스트
# 인덱스 2개를 사용
a = [[10, 20], [30, 40, 50]]
print(a[0])  # [10, 20]
print(a[0][0], a[1][1])  # 10 40

for i in range(len(a)):  # 0, 1
    for j in range(len(a[i])):
        print(a[i][j])

    
person = ["홍길동", 25, "박지성", 30, "김연아", 23]

for index in range(len(person)):
    if index % 2 == 0:
        print("이름", person[index])
    else:
        print("나이", person[index])


# 슬라이싱
# 부분 리스트 구하기
# 리스트[start:end+1:step]

a = [10, 20, 30, 40, 50, 60]
print(a[1:5:2])  # 2~3 인덱스까지 리스트를 뽑아라


# 합 구하기
score = [98, 67, 88, 82, 75, 92]
total = 0
for s in score:
    total += s
print(total)

#-------------------
total = 0
for index in range(len(score)):
    total += score[index]
print(total)


# 최대값 구하기
number = [56, 76, 87, 34, 92, 89, 68]
print(max(number))
mx = number[0]  # 최대값의 초기값
for n in number:
    if mx < n:
        mx = n
print(mx)

#----------------------------
# 최대 점수를 가진 학생의 번호는?
mx = number[0]
n = 0;
for index in range(1, len(number)):
    if mx < number[index]:
        mx = number[index]
        n = index
print("%d번 학생 최대 %d점" %(n+1, mx))


# 리스트의 복사
a = [10, 20, 30]
b = a  # 가짜복사 (참조복사)
print(a, b)  # [10, 20, 30] [10, 20, 30]
a[1] = 100
print(a, b)  # [10, 100, 30] [10, 100, 30]

# 진짜복사
a = [10, 20, 30]
b = a[:]  # 처음부터 끝까지 (모든 요소)
print(a, b)  # [10, 20, 30] [10, 20, 30]
a[1] = 200
print(a, b)

# 슬라이싱 추가
a = [10, 20, 30, 40, 50, 60]
print(a[1:5])  # [20, 30, 40, 50]
print(a[:4])   # 처음부터 [10, 20, 30, 40]
print(a[2:])   # 마지막까지 [30, 40, 50, 60]
print(a[:])


# 차트 그리기
counter = [3, 5, 2, 7]  # 득표수 (별의 개수)
name = ["홍길동", "박지성", "김연아", "박태환"]
# 홍길동: ***
# 박지성: *****
# 김연아: **
# 박태환: *******

for index in range(len(counter)):  # 별의 개수를 가져옴
    # 번호 출력
    print(name[index], end=": ")
    for count in range(counter[index]): # 개수만큼 별을 출력
        print("*", end="")
    print()
    
    
# 개구리 점프
# 돌에 적힌 수 만큼 점프를 함
# 몇번 점프?
stone = [2, 5, 1, 3, 2, 1]  # 돌에 적힌 번호

index = 0
count = 0
while index < len(stone):
    index += stone[index]
    count += 1
print(count)


# 엘리베이터 문제
# 엘리베이터가 이동한 총 거리 구하기
floor = [1, 3, 4, 2, 5, 3, 1]
# 2+1+2+3+2+2 = 12
answer = 0
for index in range(len(floor)-1):
    # 절대값 : abs()
    answer += abs(floor[index] - floor[index+1])
print(answer)

#----------------------
answer = 0
for index in range(1, len(floor)):
    # 절대값 : abs()
    answer += abs(floor[index-1] - floor[index])
print(answer)


# 마트 할인 행사
# 4번째 구매 상품은 50% 할인
price = [100, 500, 200, 400, 300, 200, 100, 500]
total = 0
for index in range(len(price)):
    if index % 4 == 3:
        total += (price[index] * 0.5)
    else:
        total += price[index]
print(total)


# 리스트 뒤집기
number = [5, 6, 3, 8, 7, 1]  # [1, 7, 8, 3, 6, 5]
# index증가에 따라 마지막 index를 감소 : [길이-1-index]
for index in range(len(number) // 2):
    temp = number[index]
    number[index] = number[len(number)-1-index]
    number[len(number)-1-index] = temp
print(number)

#------------------
number = [5, 6, 3, 8, 7, 1]
first = 0 # 첫 번째 인덱스
end = len(number)-1  # 마지막 인덱스
while first < end:
    '''
    temp = number[first]
    number[first] = number[end]
    number[end] = temp
    '''
    number[first], number[end] = number[end], number[first]
    first += 1
    end -= 1
print(number)


# 회사의 승진 문제
# 전년도 평가 점수와 올해 평가 점수를 비교
# 2개 항목이 높으면 승진
last_year = [78, 89, 93]
this_year = [92, 81, 90]
answer = False
count = 0

for index in range(len(last_year)):
    if last_year[index] < this_year[index]:
        count += 1

if count >= 2:
    answer = True

print(answer)


# 마트 계산대
# 대량(4개이상), 소량(3개 이하)
# 계산하는 데 걸리는 시간 (1개당 1분)
large, small = 0, 0
stuffs = [5, 3, 4, 2, 3, 2]
for s in stuffs:
    if s >= 4:
        large += s
    else:
        small += s
if large >= small:
    answer = large
else:
    answer = small
print(answer)


# 쇼핑몰 주문
# "XS", "S", "M", "L", "XL", "XXL"
size = 6
counter = [0] * size
shirts = ["XS", "S", "L", "L", "XL", "S"]

for s in shirts:
    if s == "XS":
        counter[0] += 1
    elif s == "S":
        counter[1] += 1
    elif s == "M":
        counter[2] += 1
    elif s == "L":
        counter[3] += 1
    elif s == "XL":
        counter[4] += 1
    elif s == "XXL":
        counter[5] += 1
print(counter)  # [1, 2, 0, 2, 1, 0]


# 투표 개표
person = 3
counter = [0] * person  # 개표
vote = [1, 3, 2, 2, 1, 3, 2, 1, 3, 2, 2, 1] # 투표

for v in vote:
    # 한줄로 표현하는 방법
    # 후보번호를 인덱스로 처리?
    counter[v-1] += 1
    
print(counter)  # [4, 5, 3]


# 양말의 켤레수 구하기
# socks = ["red", "blue", "red", "black", "red"]
counter = [0] * 3
socks = [1, 2, 1, 3, 1, 2]

for s in socks:
    counter[s-1] += 1

# [3, 2, 1]
answer = 0
for c in counter:
    answer += (c // 2)
print(answer)


# 승진 문제
last = [87, 98, 92]
this = [89, 95, 95]
count = 0
for a, b in zip(last, this):  # (87, 89), (98, 95), (92, 95)
    if a < b:
        count += 1
print(count)

# zip() : 순차타입의 데이터를 인수로 받아 순서쌍(튜플쌍)으로 만드는 함수
a = [10, 20, 30]
b = [40, 50, 60]
print(list(zip(a, b)))
# [(10, 40), (20, 50), (30, 60)]

c = "hello"
d = "korea"
print(list(zip(c, d)))
# [('h', 'k'), ('e', 'o'), ('l', 'r'), ('l', 'e'), ('o', 'a')]
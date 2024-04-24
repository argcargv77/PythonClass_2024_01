'''
마트 계산대
대량 계산대(4개 이상), 소량 계산대(3개 이하)
계산대하는 데 걸리는 시간 구하기(1개당 1분)
'''
stuff = [5, 3, 4, 2, 3, 2]
large = 0
small = 0

for s in stuff:
    if s >= 4:
        large += s
    else:
        small += s
if large >= small:
    answer = large
else:
    answer = small
print(answer)


'''
쇼핑몰 주문
"XS", "S", "M", "L", "XL", "XXL"
'''
size = 6
shirts = ["XS", "S", "L", "L", "XL", "S"]
counter = [0] * size

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
print(counter)


'''
투표
'''
person = 3
vote = [1, 3, 2, 2, 1, 3, 2, 1, 3, 2, 2, 1]
counter = [0] * person

for v in vote:
    counter[v-1] += 1   # 후보 번호를 인덱스로 처리
print(counter)


'''
양말 켤레 수 구하기
'''
# socks = ["red", "blue", "red", "black", "red"]
color = 3
socks = [1, 2, 1, 3, 1]
counter = [0] * color

for s in socks:
    counter[s-1] += 1

answer = 0
for c in counter:
    answer += (c // 2)
print(answer)

''' 변형 문제
장갑의 경우에는 카운터 변수가 2개
왼쪽 장갑과 오른쪽 장갑 인덱스 비교 
만약 왼쪽 장갑 A 사이즈가 두개가 있고 오른쪽 장갑이 3개가 있다면 2쌍이 나온다.
'''


'''
승진 문제
'''
last = [87, 98, 92]
this = [89, 95, 95]
count = 0

# 1
for a, b in zip(last, this):
    if a < b:
        count += 1   
# 2
for index in zip(last, this):
    if index[0] < index[1]:
        count += 1    
# 3        
for index in range(len(last)):
    if last[index] < this[index]:
        count += 1

# zip() : 순차타입의 데이터를 인수로 받아 순서쌍(튜플쌍)으로 만드는 함수
a = [10, 20, 30]
b = [40, 50, 60]
ab = list(zip(a, b))
print(ab)   # [(10, 40), (20, 50), (30, 60)]
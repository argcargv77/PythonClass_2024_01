'''

배열의 인덱스의 총 합 구하기 :
    - for문으로 인덱스 하나하나 돌려서 더하기
    - {range(len([array])) ㄴ total = array[index]}로 한줄로 끝내기
    
배열의 인덱스 중 최댓값 구하기 : (max)



'''

number = [45, 763, 34, 53, 234]
# 1번 풀이
mx = number[0]
for i in number:
    if mx < i:
        mx = i
print(mx)

# 2번 풀이
n = 0
for index in range(len(number)):
    if mx < number[index]:
        mx = number[index]
        n = index
print(f"{mx}, {n+1}")


#리스트의 복사
a = [10, 20, 30]
#참조복사
b = a
a[0] = 100
print(a, b)

#진짜복사
b = a[:]    # 처음부터 끝까지(모든 요소)
a[0] = 100
print(a, b)


#리스트 추가
alpha = [10, 20, 30, 40, 50, 60]


#차트 그리기
counter = [3, 6, 7, 4]
for index in range(len(counter)):
    print(f"{index}번 후보", end=" : ")
    for star in range(counter[index]):
        print("*", end = "")
    print()
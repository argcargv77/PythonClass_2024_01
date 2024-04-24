'''

절댓값 : abs()


'''
#예제 1
floor = [1, 3, 4, 5, 2, 6, 3]   # 1+2+1+1+3+4+3=15
answer = 0
for index in range(len(floor)-1):
    answer += abs(floor[index]-1)
print(answer)

#예제 2
price = [100, 400, 500, 200, 700, 100, 300]
total = 0
for index in range(len(price)):
    if (index+1) % 4 == 0:
        total += price[index] * 0.5
    else:
        total += price[index]
print(total)

# 리스트 뒤집기(reversed)
number = [3, 5, 6, 1, 7, 2]   #[2, 7, 1, 6, 5, 3]
''' 양 끝의 인덱스를 세트로 묶는 방법 : [len(a)-1-index] '''
for index in range(len(number)//2): #for문으로 뒤집기
    temp = number[index]
    number[index] = number[len(number)-1-index]
    number[len(number)-1-index] = temp
print(number)

first = 0
end = len(number)-1
while first < end:  #while문으로 뒤집기
    '''
    temp2 = number[first]
    number[first] = number[end]
    number[end] = temp2
    '''
    number[first], number[end] = number[end], number[first]
    first += 1
    end -= 1
print(number)
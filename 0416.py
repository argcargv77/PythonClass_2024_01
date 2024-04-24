'''
삽입1
list.append()
'''
nation = list() # []
while True:
    name = input(" : ")
    if name == "exit":
        break
    if name in nation:
        print("중복")
    else:
        nation.append(name)
print(nation)

'''
삽입2
list.insert(index, item)
'''
names = ["홍길동", "박지성", "김연아"]
number = int(input("몇 번째 삽입? : "))
#삽입이 가능한지 검사
if number > 0 and number <= len(names)+1:
    name = input("이름 : ")
    if name not in names:
        names.insert(number-1, name)
else:
    print("위치가 잘못됨")

'''
수정1
'''
names = ["홍길동", "박지성", "김연아"]
number = int(input("몇 번째 수정? : "))
if number > 0 and number < len(names):
    name = input("바꿀 이름 : ")
    if name not in names:
        names[number-1] = name
    else:
        print("중복")
else:
    print("위치에러")

'''
수정2
직접 아이템을 검색
'''
names = ["홍길동", "박지성", "김연아"]
search = input("검색할 이름 : ")
if search in names:
    name = input("수정할 이름 : ")
    names[names.index(search)] = name
else:
    print("이름 없음")

'''
삭제1 : list.pop(index)
'''
names = ["홍길동", "박지성", "김연아"]
number = int(input("삭제할 위치 : "))
if number > 0 and number <= len(names):
    names.pop(number-1)
else:
    print("위치 오류")

'''
삭제2 : list.remove(item)
'''
names = ["홍길동", "박지성", "김연아"]
search = input("삭제할 이름 : ")
if search in names:
    names.remove(search)
else:
    print("해당 이름이 없음")

'''
a = [10, 20, 30]
b = [40, 50, 60]
zip(a, b)
-> (10, 40), (20, 50), (30, 60)

enumerate(순차)
>> 순차 자료에서 인덱스와 아이템을 튜플쌍으로 만들어준다.
'''
score = [10, 20, 30, 40]
print(list(enumerate(score))) # >> [(0, 10), (1, 20), (2, 30), (3, 40)]

msg = "hello"
print(list(enumerate(msg)))

vote = [1, 2, 1, 1, 3, 2, 1, 1, 3, 3, 3, 3, 3]
counter = [0] * 3
for v in vote:
    counter[v-1] += 1
print(counter) # [5, 2, 6]

vote = [1, 2, 1, 1, 3, 2, 1, 1, 3, 3, 3, 3, 3]
counter = [0] * 3
mx = -99999
answer = 0
for index in range(len(counter)):
    if mx < counter[index]:
        mx = counter[index]
        answer = index+1

for index, item in enumerate(counter):
    if mx < item:
        mx = item
        answer = index+1
print(answer)
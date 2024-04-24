'''
객체(object)
: 객체는 데이터와 메서드로 구성된 새로운 데이터

메서드 : 함수의 형태로 이루어졌으며 기능, 특징 등 객체가 가지는 동작을 정의한 것

'''
a = 10
a = "hello"
type(a)
a= [1, 2, 3]
type(a)

a = "hello"
a_up = a.upper()
print(a_up)

a_lw = a.lower()
print(a_lw)

a_cp = a.capitalize()
print(a_cp)

a = [10, 20 ,30]
a.append(40)
print(a)

a.insert(1, 10.5)
print(a)

a = [10, 20, 30, 40]
a.remove(30)    # () 안에 데이터
print(a)

a = [10, 20, 30, 40]
a.pop() # () 안에 인덱스, 반환값을 출력해주고 () 안에 아무것도 안쓰면 마지막 인덱스의 데이터를 꺼냄
print(a)

a = [10, 20, 30, 40]
a.pop(1)    

a = []
a = list()

a = [10, 20, 30, 40, 50]
a.index(40)   # 특정 데이터의 인덱스 번호(위치) 구하기

a = [10, 20, 30, 40, 10, 20, 10, 60]
a.count(10)   # 특정 데이터의 중복 횟수 구하기
max(a)

a.sort()    # 오름차순
a.sort(reverse=True)    # 내림차순

a.reverse()

score = []  # score = list()
score.append(10)
score.append(3.14)
score.append("hello")

score.insert(0, "100")
score.insert(3, 200)

print(score) # [10, 10, 3.14, 200, 'hello]

score.remove(3.14)  # 삭제 전 데이터가 존재하는지 확인해야함

score.pop(2)


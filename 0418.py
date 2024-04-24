# 10명 학생 상담
# 누가 상담을 받지 못하나? -> [2, 3, 8, 10]
answer = list()
scd = ['O', 'X', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'X']
# 방법1
for index in range(len(scd)):
    if scd[index] == 'X':
        answer.append(index+1)
        
# 방법2
for index, item in enumerate(scd):
    if item == 'X':
        answer.append(index+1)


# 큰 값 구하기
score = [76, 87, 95, 93, 98, 92]
print(max(score))
mx = score[0]
for index in range(1, len(score)):
    if mx < score[index]:
        mx = score[index]
        
# 두번째로 큰 값 구하기
sec = score[1]
for index in range(len(score)):
    if mx < score[index]:
        sec = mx
        mx = score[index]
    elif sec < score[index]:
        sec = score[index]
        
# 세번째로 큰 값 구하기
score.sort(reverse=True) # 원본을 변경 시킨다.
print(score[2])

rank_score = score      # 복사본x, 연동(참조)
rank_score = score[:]   # 복사본
rank_score.sort(reverse=True)

rank_score = sorted(score, reverse=True)  # 원본은 유지하고 정렬한 새 리스트 생성

print(rank_score, score)


# 8명의 학생 점수 중 n등은 평균점수와 몇 점 차이날까?
score = [87, 67, 97, 88, 58, 95, 79, 70]
n = 2
avg = sum(score) / len(score)   # 평균 구하기
score.sort(reverse=True)
answer = abs(avg, score[n-1])   # 평균과 n등 점수와의 차이의 절댓값


# 주어진 점수의 순위 리스트 만들기
score = [90, 87, 87, 23, 35, 28, 12, 46]    # -> [1, 2, 2, 7, 5, 6, 8, 4]
# 방법1 (정해진 리스트가 존재할 경우)
rank = [1] * len(score)
for index1 in range(len(score)):    # 점수 선택
    for index2 in range(len(score)):    # 비교할 대상 선택
        if score[index1] < score[index2]:
            rank[index1] += 1   # 등수가 떨어짐

# 방법2 (리스트를 새로 만듦)
answer = []
for s1 in score:
    rank = 1
    for s2 in score:
        if s1 < s2:     # 등수 결정
            rank += 1
    answer.append(rank)

# 방법3
answer = []
rank_score = sorted(score, reverse=True)
for s in score:
    rank = rank_score.index(s)+1
    answer.append(rank)
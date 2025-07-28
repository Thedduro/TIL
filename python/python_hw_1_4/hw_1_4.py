'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.

# 학생 점수 정보
score_dict = { "Alice": 85, "bob": 78, "Charlie": 92, "David": 88, "Eve": 95 }

# 학생 평균 점수 정보 출력
avg_score = sum(score_dict.values()) / len(score_dict)
print(avg_score)

# 80점 이상 받은 학생 이름 출력
over_80 = [x for x, y in score_dict.items() if y > 80]
print(over_80)

# 학생 점수가 높은 순으로 정렬
print(sorted(score_dict.values(), reverse=True))

# 점수가 가장 높은 학생과 낮은 학생의 점수 차이 계산
# print(max(score_dict, key=score_dict.get))
# # 1.score_dict의 모든 key를 대상으로 ('a', 'b', 'c' 등)
# # 2.각각의 key에 대해 score_dict.get(key) 값을 기준으로 비교
# # 3.그 중 최댓값을 가지는 key 를 반환
print(score_dict[max(score_dict, key=score_dict.get)] - score_dict[min(score_dict, key=score_dict.get)])

# 각 학생의 점수와 평균 점수를 비교하여, 낮은 학생의 이름과 성적 출력
lower_name = [(x,y) for x, y in score_dict.items() if y < avg_score]
print(lower_name)
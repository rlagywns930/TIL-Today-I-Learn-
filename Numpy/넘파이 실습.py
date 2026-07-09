# 넘파이 불러오기
import numpy as np 

-----
# Numpy Array 생성
array1 = np.array([1,3,5,7,9]) # 1차원 배열 생성
array1

array2 = np.array([[1,2,3,4,],[5,6,7,8],[9,10,11,12]) # 2차원 배열 생성
array2

-----
# 배열 속성 확인
type(array1) # 배열 크기
print(array1.size) # 배열 요소 개수
print(array1.shape) # 배열 모양

-----
# 특정 패턴의 배열 생성하기
zeros_id1 = np.zero(5) # 0이 5개인 1차원 배열
zeros_id2 = np.zero((3,4), dtype = int) # 3행 4열, 정수형인 2차원 배열 생성

arr1 = np.arange(10) # 0부터 9까지 순차적으로 생성
arr2 = np.arange(1,10,2) # 1부터 9까지 2씩 증가
arr3 = np.arange(0,1,0.2) #소수점 간격 생성

=============================================================================================
#인덱싱
gdp_array = np.array([6610, 7637, 8127, 8885, 10385, 12565, 13403, 12398, 8282, 10672])
gdp_array[0] # gdp_array의 첫번째 데이터를 가져옴
gdp_array[[1, 3, 4]] # 여러값 인덱싱

-----
#슬라이싱
gdp_array[2:6] # 2부터 5까지
gdp_array[:6] # 처음부터 5까지
gdp_array[5:] # 5부터 끝까지
gdp_array[1:8:3] # 1부터 7까지 3씩 간격을 띄어서

=============================================================================================
# 2차원 인덱싱
import numpy as np

gdp_array = np.array([
    [12257, 11561, 13165, 14673, 16496, 19403],  # 대한민국
    [39169, 34406, 32821, 35387, 38299, 37813],  # 일본
    [959, 1053, 1149, 1289, 1509, 1753],         # 중국
    [36335, 37133, 38023, 39496, 41713, 44115]   # 미국
])
gdp_array

-----
gdp_array.shpae # 4행 6열
gdp_array[1] # 일본 전체 GDP 데이터
gdp_array[1][3] # 35387
gdp_array[1,3] # 35387

-----
gdp_array[1:3, 2:5] # 이상:미만
gdp_array[1:3, 2:] # 일본 중국의 2002년 이후 데이터
gdp_array[:, 2:5] # 모든 국가 2002년~2004년 데이터

=============================================================================================
# 불린 인덱싱
import numpy as np

gdp_array = np.array([6610, 7637, 8127, 8885, 10385, 12565, 13403, 12398, 8282, 10672])
gdp_array

# 1번째 방법
mask = gdp_array > 10000 # mask를 이용한 값 추출
gdp_array[mask] 
# 2번쨰 방법
gdp_array[gdp_array >10000] # 한번에 마스킹 처리

-----
gdp_array[(gdp_array > 10000) | (gdp_array < 8000)] # or 연산으로 조건 결합
gdp_array[(gdp_array > 10000) & (gdp_array < 8000)] # and 연산으로 조건 결합

-----
import numpy as np

grades = np.array([85, 60, 92, 55, 78])

fail_indices = np.where(grades < 60) # 조건에 맞는 인덱스 찾기
result = np.where(grades >=80, "Pass", "Fail") # 80점 이상은 Pass, 아니면 Fail

-----
# Numpy 기본연산
.mean() # 평균
.sum() # 합계
.min() #최솟값
.max() #최댓값

-----
# Broadcasting => Numpy에서 서로 다른 크기의 배열 간 연산을 수행할 때 자동으로 배열의 크기를 맞춰주는 기능

import numpy as np

a = np.array([[1],[2],[3]])
b = np.array([[10, 20, 30]])

result = a+b 
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

---
# stack

names = np.array(["Kim", "Lee", "Park"])
scores = np.array([90, 85, 95])

col_stacked = np.columns_stack((name, score)) # 열(세로)기준으로 배열 쌓기
# [['Kim' '90']
#  ['Lee' '85']
#  ['Park' '95']]

-----
row1 = np.array([1, 2, 3])
row2 = np.array([4, 5, 6])

col_stacked = np.row_stack((row1, row2)) # 행(가로) 기준으로 배열 쌓기
# [[1 2 3]
#  [4 5 6]]

-----
# 데이터 값 제한하기 (clip)

scores = np.array([12, 45, 88, 120, -10, 60])

clipped_scores = np.clip(score, a_min = 0, a_max = 100) # 최소 0, 최대 100으로 범위 제한
clipped_scores 
# [ 12  45  88 100   0  60]

-----
# 배열 조건 검사하기

scores = np.array([85, 90, 55, 70, 95])

has_failed = np.any(score < 60) # 배열의 원소 중 특정 조건을 하나도 만족하면 True, 모두 만족하지 않으면 False
# True
has_perfect = np.any(scores == 100) # False

np.all : 모두 조건을 만족하는지 확인
all_passed = np.all(score >= 60) # 55점이 있기 때문에 False

-----
axis = 1 행별로 검사
axis = 0 열별로 검사


student_scores = np.array([
    [85, 90, 95],  # 1번 학생 (전부 우수)
    [55, 70, 80],  # 2번 학생 (국어 55점 과락 발생)
    [92, 45, 88]   # 3번 학생 (영어 45점 과락 발생)
])

has_fail_per_student = np.any(student_score < 60, axis = 1) # 행(가로) 방향으로 검사하여 학생마다 결과를 뺌
# 결과: [False  True  True] 

has_passed_per_student = np.any(student_score >= 60, axis = 0) # 열(세로) 방향으로 검사하여 과목마다 결과를 뺌
# 결과: [False False  True]




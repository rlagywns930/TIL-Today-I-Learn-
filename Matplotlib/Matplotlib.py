# Matplotlib 불러오기
import matploylib.pyplot as plt

-----
1. 선 그래프

# 데이터 정의
year_array = np.array([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
stock_array = np.array([14.46, 19.01, 20.04, 27.59, 26.32, 28.96, 42.31, 39.44, 73.41, 132.69])

# 그래프 그리기 (x축, y축)
plt.plot(year_array, stock_array)
plt.show()

-----
2. 막대 그래프

# 데이터 정의
name_array = np.array(['mark', 'dongwook', 'hyojune', 'sowon', 'taeho'])
votes_array = np.array([5, 10, 6, 8, 3])

# 그래프 그리기 (x축, y축)
plt.bar(name_array, votes_array)
plt.show()

------
3.  산점도

# 데이터 정의
height_array = np.array([165, 164, 155, 151, 157, 162, 155, 157, 165, 162,
                         165, 167, 167, 183, 180, 184, 177, 178, 175, 181,
                         172, 173, 169, 172, 177, 178, 185, 186, 190, 187])

weight_array = np.array([62, 59, 57, 55, 60, 58, 51, 56, 68, 64,
                         57, 58, 64, 79, 73, 76, 61, 65, 83, 80,
                         67, 82, 88, 62, 61, 79, 81, 68, 83, 80])

# 그래프 그리기
plt.scatter(height_array, weight_array)
plt.show()

-----

plt.tilte() # 제목 붙히기
plt.xlabel() # X축 이름
plt.xlabel() # Y축 이름
plt.scatter(c = 'Red') # 점의 색상 빨간색으로 변경
plt.scatter(c = 'Red', marker = '+'# or's') # 점의 모양 +, square로 변경
plt.figure(figsize = (10,4)) # 그래프 사이즈 조절
plt.rc('font', family='Malgun Gothic') # 한글 맑은고딕 사용
fig, ax = plt.subplots() # Figure, Axes 생성
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,4)) # 한 화면에 두 개의 그래프
ax1.plot('Year', 'Close', data=fb_stock_close) # ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax2.plot('Year', 'Close', data=twtr_stock_close) # ax2: X(Twitter)의 연도별 평균 주식 종가













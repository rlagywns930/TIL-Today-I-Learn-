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

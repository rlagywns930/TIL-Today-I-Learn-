# pandas 불러오기
import pandas as pd

-----
# DataFrame 만들기

# 리스트를 이용해서 만들기
two_dimensional_list = [
    ['skirt', 10, 30000],
    ['sweater', 15, 60000],
    ['coat', 6, 95000],
    ['jeans', 11, 35000]
]

list_df = pd.DataFrame(two_dimensional_list, columns = ['skirt', 'sweater','coat','jeans'])

-----
# array를 이용해서 만들기

two_dimensional_list = [
    ['skirt', 10, 30000],
    ['sweater', 15, 60000],
    ['coat', 6, 95000],
    ['jeans', 11, 35000]
]

two_dimensional_array = np.array(two_dimensional_list)

array_df = pd.DataFrame(two_dimensional_list, columns = ['skirt', 'sweater','coat','jeans'])

-----
# 딕셔너리를 이용해서 만들기

df = pd.DataFrame({
  'categori' : ['skirt', 'sweater', 'coat', 'jeans'],
  'quantity' : [10, 15, 6, 11],
  'price' : [30000, 60000, 95000, 35000]
})
df

=============================================================================================
# 데이터 불러오기

burger_df = pd.read_csv('../data/burger.csv')

# header 없는 CSV 불러오기

burger_df = pd.read_csv('../data/burger.csv', header = None)

# 컬럼명 설정

burger_df_2 = pd.read_csv('../data/burger2.csv', header=None, names: ['product_name', 'calories', 'carb', 'protein', 'fat', 'sodium',
       'category']) # 헤더가 없는 CSV파일의 경우 names를 이용해 컬럼명을 설정

-----
# 인덱스 설정

burger_df = pd.read_csv('../data/burger.csv', index_col = 'product_name')

-----
# 인덱스로 첫번째 컬럼 설정하기

burger_df = pd.read_csv('../data/burger.csv', index_col = 0)

-----
# 데이터프레임 살펴보기
info() # 데이터프레임 구조 및 기본 정보 확인
describe() # 기초 통계 정보 확인
dtypes # 컬럼별 데이터 타입 확인

=============================================================================================
iloc : 정수 인덱스 
loc : 이름

burger_df.iloc[2, 1] # 3번쨰 로우 2번째 컬럼 선택
burger_df.loc['Double Whopper', 'protein'] # Double Whopper의 protein 값 선택
burger_df.loc[['Whopper', 'Double Whopper'], ['carb', 'protein', 'fat']] 
burfer_df.loc['Double Whopper':'Bacon King', 'calories':'fat'] # 슬라이싱에서는 마지막 값도 포함

=============================================================================================
burger_df.loc[burger_df['calories'] < 500] # 필터링 적용
burger_df.loc[burger_df['calories'] < 500, 'protein']  # 단백질 컬럼만 선택

-----
mask = buger_df['calories] < 500 # 조건 설정
buger_df.loc[mask, 'calories' : 'fat'] # calories 부터 fat까지 선택

=============================================================================================
burger_df.loc['Double Stacker King', 'sodium'] = 1.9 # 값을 1.9로 수정
buger_df.loc['Cheeseburger'] = [360, 24, 18, 21, 0.7, 'Burger'] # 로우 수정(열의 개수가 일치해야함)
burger_df['sodium'] = 1 # sodium 컬럼의 모든 값을 1로 변경
burger_df.loc['Triple Whopper'] = [1130, 49, 67, 75, 1.1, 'Burgers'] # 새로운 로우 추가 
burger_df.loc['burger_df['calories'] >= 500, 'hight_calories'] = True # 칼로리가 500 이상인 컬럼에 hight_calories 컬럼을 추가하고 True값 설정


















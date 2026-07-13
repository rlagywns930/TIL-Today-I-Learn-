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
-----




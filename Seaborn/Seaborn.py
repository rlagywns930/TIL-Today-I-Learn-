# Seaborn 불러오기

import seaborn as sns

-----

sns.set_theme(style='whitegrid') # 회색 가로 선이 있는 흰색 바탕으로 바뀜.
sns.barplot(data=df, x='month', y='total', ci=None)
plt.show()

hue # 색상구분을 통해 데이터를 그룹화할 때 사용하는 매개변수

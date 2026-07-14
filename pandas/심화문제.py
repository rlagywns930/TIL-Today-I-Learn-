1. 프리미어 리그 데이터 탐색하기

import pandas as pd

players_df = pd.read_csv('../data/tottenham_2021.csv', index_col='name')
-----
players_df.head(5) # 상위 5개의 정보 확인
players_df.shape # (24,4) 24개의 로우 4개의 컬럼
players_df.columns # 컬럼 확인 Index(['matches', 'minutes', 'goals', 'assists'], dtype='object')
players_df.info()
players_df.dtypes
players_df.describe()
loan_df.describe(include='all') # 모든 컬럼 통계 확인
-----
player_df[player_df.matches == max(player_df.matches)]['matches'] # Pierre Højbjerg, Hugo Lloris가 38경기로 가장 많은 경기를 치룸

player_df[player_df.minutes == max[player_df.minutes]]['minutes'] #  Pierre Højbjerg, Hugo Lloris가 3420분으로 가장 많이 뛰었다

max(player_df.goals) # 23골이 가장 많다

min(players_df.minutes) # 1분 뛴 선수가 있다

=============================================================================================
2. 손흥민 선수의 골 득점 수는?

players_df.loc["Son Heung-Min", "goals"] # 총 17골 넣음

=============================================================================================
3. 골을 넣은 선수는 누구?

players_df.loc[player_df['goals'] >=1, :]

=============================================================================================
4. 선수 데이터 수정 및 추가하기

players_df.loc['Son Heung-Min', :] = [35, 3051, 23, 7] # 손흥민 선수 데이터 수정
players_df.loc['Ben Davies', 'matches'] => players_df.loc['Ben Davies', 'matches'] = 29 # 결측치 처리
platers_df.loc[:, 'team'] = 'Tottenham' # Team 열을 모두 'Tottenham' 수정




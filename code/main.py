

from itertools import combinations_with_replacement # 引入可重複出現結果庫
import pandas as pd # 引入pandas庫
import sys

iterations = sys.argv[2] # 設置擲骰子次數

if sys.argv[1] == 'n':
    def table(N) :
    HT = list( combinations_with_replacement( [12, -10], N )) # 產生擲N次骰子組合
    df = pd.DataFrame( HT, columns = [i for i in range(1, N+1)]) # 正規化Columns標題為流水號
    df['Sum'] = df.apply(lambda x: x.sum(), axis=1) # 新增Columns列總和
    result = sum(i > 0 for i in df['Sum'])/sum(df['Sum'])
    print ('P_win = ', result)
    
elif sys.argv[1] == '-n':
    def table(N) :
    HT = list( combinations_with_replacement( [12, -10], N )) # 產生擲N次骰子組合
    df = pd.DataFrame( HT, columns = [i for i in range(1, N+1)]) # 正規化Columns標題為流水號
    df['Sum'] = df.apply(lambda x: x.sum(), axis=1) # 新增Columns列總和
    result = sum(i < 0 for i in df['Sum'])/sum(df['Sum'])
    print ('P_lose = ', result)

else:
    print('請輸入 n or -n')


table(iterations)

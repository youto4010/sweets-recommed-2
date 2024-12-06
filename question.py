import pandas as pd
from numpy import random
import numpy as np


df=pd.read_csv('question.csv')
df=df.fillna(0)

number=0

def shuffle_question(df):
    start_row = 2
    end_row = 17
    question_array = df.iloc[start_row-1:end_row, 0].values

    question_1 = random.choice(question_array)
    question_array = np.delete(question_array, np.where(question_array == question_1))
    question_2 = random.choice(question_array)

    return question_1,question_2

# result = shuffle_question(df)
# print("question_1:", result[0])
# print("question_2:", result[1])


def yes_1():
    # セッションから質問を取得
    question_1 = session.get('question_1', '')
    
    # セッションからデータフレームを取得
    df = session.get('df', pd.DataFrame())
    
    # データフレームが存在しない場合は再度読み込む
    if df.empty:
        df = pd.read_csv('question.csv')
        df = df.fillna(0)
    
    # 質問に対応するお菓子を取得
    row_indices = df.index[df['質問'] == question_1].tolist()
    candies_1 = df.loc[row_indices, 'お菓子１':].dropna().values.flatten().tolist()
    
    # 何かしらの処理を行った後、結果を返す
    return candies_1

def yes_2():
    # セッションから質問を取得
    question_2 = session.get('question_2', '')
    
    # セッションからデータフレームを取得
    df = session.get('df', pd.DataFrame())
    
    # データフレームが存在しない場合は再度読み込む
    if df.empty:
        df = pd.read_csv('question.csv')
        df = df.fillna(0)
    
    # 質問に対応するお菓子を取得
    row_indices = df.index[df['質問'] == question_2].tolist()
    candies_2 = df.loc[row_indices, 'お菓子１':].dropna().values.flatten().tolist()
    
    # 何かしらの処理を行った後、結果を返す
    return candies_2

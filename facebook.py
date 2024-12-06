import gensim
import MeCab
import numpy as np
import ipadic
import pandas as pd
import random

model = gensim.models.KeyedVectors.load_word2vec_format('model.bin', binary=True)


CHASEN_ARGS = r' -F "%m\t%f[7]\t%f[6]\t%F-[0,1,2,3]\t%f[4]\t%f[5]\n"'
CHASEN_ARGS += r' -U "%m\t%m\t%m\t%F-[0,1,2,3]\t\t\n"'
tagger = MeCab.Tagger(ipadic.MECAB_ARGS + CHASEN_ARGS)

sweets_category = ['チョコ', 'クッキー・ビスケット', 'ラムネ', 'グミ', '飴', 'スナック', 'おつまみ', 'ナッツ類', 'ゼリー', 'プリン', 'ヨーグルト']

# 読み込むCSVファイルを変更
df_sweets = pd.read_csv('sweets.csv')

def get_vector(text):
    sum_vec = np.zeros(300)
    word_count = 0
    node = tagger.parseToNode(text)
    # nodeにsurface(単語)feature(品詞情報)を持つ解析結果を代入している。

    while node:
        fields = node.feature.split(",")
        if fields[0] == '名詞' or fields[0] == '動詞':
            sum_vec += model[node.surface]
            word_count += 1
        node = node.next
    return sum_vec / word_count

# results = model.most_similar(positive=['講義'])
# for result in results:
#     print(result)

# text1 = get_vector('昨日、カレーを食べた。')
# text2 = get_vector('昨夜、Netflixでお笑いを見た。')
# sim = np.dot(text1, text2) / (np.linalg.norm(text1) * np.linalg.norm(text2))
# print(sim)
text = "チョコレートなどの甘い食べ物が食べたいです。"
def input_answer(text):
    input_result = []  # 上位3つのcategoryを格納する配列
    sweets_0 = []  # 商品名を格納する配列
    sweets_1 = []  # 商品名を格納する配列
    sweets_2 = []  # 商品名を格納する配列

    for category in sweets_category:
        text1 = get_vector(category)
        text2 = get_vector(text)
        sim = np.dot(text1, text2) / (np.linalg.norm(text1) * np.linalg.norm(text2))
        input_result.append({'category': category, 'similarity': sim})

    # input_resultをsimilarityの値で降順にソートし、上位3つを取得
    input_result = sorted(input_result, key=lambda x: x['similarity'], reverse=True)[:3]

    # sweets.csvから該当するカテゴリの商品名を取得
    sweets_0.extend(df_sweets[df_sweets['種類'] == input_result[0]['category']]['名前'].tolist())
    sweets_1.extend(df_sweets[df_sweets['種類'] == input_result[1]['category']]['名前'].tolist())
    sweets_2.extend(df_sweets[df_sweets['種類'] == input_result[2]['category']]['名前'].tolist())

    result = sweets_0+sweets_1+sweets_2
    final_sweets = random.choice(result)
    return final_sweets

print(input_answer(text))
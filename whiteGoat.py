from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('./japanese-word2vec/word2vec.gensim.model')

results = model.most_similar(positive=['講義'])
for result in results:
    print(result)
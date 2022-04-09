import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec



def color_in_gr(lists):
    colors = ['#FFC618','#94FF18','#0D0E0B','#1D22BF','#BF1D9C','#BF241D','#BF751D']
    uniq = {}
    for i in lists:
        if i[1] not in uniq.keys():
            uniq[i[1]] = colors.pop()
    for i in lists:
        i.append(uniq.get(i[1]))
    return lists
    

def count_vectorizer(lists):
    for i in lists:
        text = [i[0]]
        vectorizer = CountVectorizer()
        vectorizer.fit(text)
        vector = vectorizer.transform(text)
        vec = vector.shape
        i.append(vec)
    color_in_gr(lists)
    return lists

def tfid_vectorizer(lists):
    for i in lists:
        text = [i[0]]
        vectorizer = TfidfVectorizer()
        vectorizer.fit(text)
        vector = vectorizer.transform(text)
        vec = vector.shape
        i.append(vec)
    color_in_gr(lists)
    return lists

def word_vectorizer(lists):
    for i in lists:
        z = i[0].lower()
        z = re.sub('[^а-яА-Я]', ' ', z ) 
        z = re.sub(r'\s+', ' ', z)
        x = z.split(' ')
        model = Word2Vec(min_count=1)
        model.build_vocab(x)  # prepare the model vocabulary
        ss = model.train(x, total_examples=model.corpus_count,
                                            epochs=model.epochs)
        i.append(ss)
    color_in_gr(lists)
    return lists


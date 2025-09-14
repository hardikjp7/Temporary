import nltk
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import defaultdict, Counter

def get_bigrams_and_collocations(text, input_word):
    # tk = RegexpTokenizer(r'[0-9a-zA-Z_]+', gaps = True)
    tk = RegexpTokenizer(r'[0-9a-zA-Z_]+')
    stop_words = set(stopwords.words('english'))
    cfd_bigrams = defaultdict(int)

    prev_word = None
    tokenizedwords = []
    tokenizedwordsbigrams = [] 

    for word in tk.tokenize(text):
        word = word.lower()
        tokenizedwords.append(word)
        if prev_word == input_word:
            cfd_bigrams[word]  += 1
        if prev_word and prev_word not in stop_words and word not in stop_words:
            tokenizedwordsbigrams.append([prev_word, word])
        prev_word = word
    collocationWords = Counter(tuple(b) for b in tokenizedwordsbigrams)
    top_collocations = collocationWords.most_common(3)

    top_three = sorted(cfd_bigrams.items(), key=lambda x: x[1], reverse=True)[:3]

    collocationWords = [" ".join(words) for words, count in top_collocations]

    return top_three, top_collocations
 
1st wala

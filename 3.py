import nltk
nltk.download('punkt_tab')      
nltk.download('wordnet')    
nltk.download('omw-1.4') 
nltk.download('averaged_perceptron_tagger_eng')
nltk.download("stopwords")
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def perfromStemAndLemma(text):
    tk = RegexpTokenizer(r'[0-9a-zA-Z_]+')
    stop_words = set(stopwords.words('english'))

    porter_stemmer = PorterStemmer()
    lemmetizer = WordNetLemmatizer()
    lancaster_stemmer = LancasterStemmer()

    porter_stemmer_words = []
    lancaster_stemmer_words = []
    lemmetizer_words = []

    for word in tk.tokenize(text):
        word = word.lower()
        if not word or word in stop_words:
            continue
        print(word)
        porter_stemmer_words.append(porter_stemmer.stem(word))
        lancaster_stemmer_words.append(lancaster_stemmer.stem(word))
        lemmetizer_words.append(lemmetizer.lemmatize(word))
    
    return porter_stemmer_words, lancaster_stemmer_words, lemmetizer_words

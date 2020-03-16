import re
import string
from nltk.corpus import stopwords

def clean_english_doc(doc):
    tokens = doc.split()
    re_punc = re.compile("[{}]".format(re.escape(string.punctuation)))
    tokens = [re_punc.sub("", word) for word in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if len(word) > 1]

    return tokens



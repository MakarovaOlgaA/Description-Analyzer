import nltk, re, string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

class TextProcessor(object):
    
    def tokenizeText(self, text):
        #normalize case
        result = text.lower()

        #remove html tags
        result = re.sub('<.*?>', '', result)

        #remove links
        result = re.sub('(www|http)\S+', '', result)

        #remove words with numbers in them
        result = re.sub(r'\w*\d\w*', '', result)

        #remove punctuation and special characters from words 
        #(but leave apostrophre as it will be easier to remove stopwords)
        whitelist = set("abcdefghijklmnopqrstuvwxyz '")
        result = ''.join(filter(whitelist.__contains__, result))

        words = result.split()

        #remove stop-words
        stop_words = stopwords.words('english')
        words = [w for w in words if not w in stop_words]

        #stem words 
        porter = PorterStemmer()
        words = [porter.stem(w) for w in words]

        return words

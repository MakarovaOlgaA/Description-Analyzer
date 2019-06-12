import nltk, re, string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score 
from sklearn.naive_bayes import MultinomialNB
import numpy as np

class TextProcessor(object):
    def __init__(self, repo):
        self.repo = repo

    def loadAllDocumets(self):
        documents = self.repo.search('', False)
        documents = [(self.preProcess(d.description), 'Advertiser-friendly' if d.isAdvertizerFriendly == '\x01' else 'Not suitable for ads') for d in documents]
        self.documentsDf = pd.DataFrame(documents, columns = ['content', 'label'])

    def preProcess(self, text):
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

        return ' '.join(words)

    def analyze(self, textToAnalyze):
        self.loadAllDocumets()

        self.encoder = LabelEncoder()
        self.documentsDf['label'] = self.encoder.fit_transform(self.documentsDf['label'])

        self.buildTfIdf()
        
        preProcessed = self.preProcess(textToAnalyze)
        prediction = self.predict(preProcessed)
        scores = self.get_scores(self.tfIdf, self.vectors)
        return ProcessingResult (preProcessed, scores, prediction)

    def buildTfIdf(self):
        self.tfIdf = TfidfVectorizer(max_features=1000, min_df=3, max_df=0.7)
        self.vectors = self.tfIdf.fit_transform(self.documentsDf['content'])

    def predict(self, testString):
        naive = MultinomialNB()
        naive.fit(self.vectors, self.documentsDf['label'])

        testDocumentDf = pd.DataFrame([(testString)], columns = ['content'])
        testData = self.tfIdf.transform(testDocumentDf['content'])

        prediction = naive.predict(testData)
        return self.encoder.inverse_transform(prediction)[0]

        # Use accuracy_score function to get the accuracy
      #  print("Naive Bayes Accuracy Score -> ",accuracy_score(prediction, testString)*100)

    def get_scores(self, vectorizer, vectors):
        scores = zip(vectorizer.get_feature_names(),
                     np.asarray(vectors.sum(axis=0)).ravel())
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        formatted_scores = ["{}: {}".format(item[0], item[1]) for item in sorted_scores[:200]]
        return formatted_scores

class ProcessingResult:
    def __init__(self, processedContent, vocabulary, prediction):  
        self.processedContent = processedContent
        self.vocabulary = vocabulary
        self.prediction = prediction
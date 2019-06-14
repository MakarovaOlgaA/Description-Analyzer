import nltk, re, string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, average_precision_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import model_selection
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
        prediction = self.predict(preProcessed).tolist()[0]
        scores = self.get_scores(self.tfIdf, self.vectors)

        index = prediction.index(max(prediction))
        label = self.encoder.inverse_transform([index])[0]

        return ProcessingResult (preProcessed, scores, label, max(prediction))

    def buildTfIdf(self):
        self.tfIdf = TfidfVectorizer(max_features=1000, min_df=3, max_df=0.7)
        self.vectors = self.tfIdf.fit_transform(self.documentsDf['content'])

    def predict(self, testString):
        naive = MultinomialNB()
        naive.fit(self.vectors, self.documentsDf['label'])

        testDocumentDf = pd.DataFrame([(testString)], columns = ['content'])
        testData = self.tfIdf.transform(testDocumentDf['content'])

        prediction = naive.predict_proba(testData)
        #print("Naive Bayes Accuracy Score -> ",accuracy_score(prediction, testString)*100)
        #return self.encoder.inverse_transform(prediction)[0]
        return prediction

    def get_scores(self, vectorizer, vectors):
        scores = zip(vectorizer.get_feature_names(),
                     np.asarray(vectors.sum(axis=0)).ravel())
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        formatted_scores = ["{}: {}".format(item[0], item[1]) for item in sorted_scores[:200]]
        return formatted_scores

    def getMetrics(self):
        self.loadAllDocumets()

        self.encoder = LabelEncoder()
        self.documentsDf['label'] = self.encoder.fit_transform(self.documentsDf['label'])

        Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(self.documentsDf['content'],self.documentsDf['label'],test_size=0.3)

        Tfidf_vect = TfidfVectorizer(max_features=5000)
        Tfidf_vect.fit(self.documentsDf['content'])
        Train_X_Tfidf = Tfidf_vect.transform(Train_X)
        Test_X_Tfidf = Tfidf_vect.transform(Test_X)

        # fit the training dataset on the NB classifier
        Naive = MultinomialNB()
        Naive.fit(Train_X_Tfidf,Train_Y)

        # predict the labels on validation dataset
        predictions_NB = Naive.predict(Test_X_Tfidf)

        # Use accuracy_score function to get the accuracy
        acuracy = accuracy_score(predictions_NB, Test_Y)
        recall = recall_score(predictions_NB, Test_Y)
        roc_auc = roc_auc_score(predictions_NB, Test_Y)
        precision = average_precision_score(predictions_NB, Test_Y)

        return Metrics(acuracy, recall, roc_auc, precision)

class ProcessingResult:
    def __init__(self, processedContent, vocabulary, label, probalility):  
        self.processedContent = processedContent
        self.vocabulary = vocabulary
        self.label = label
        self.probalility = probalility

class Metrics:
    def __init__(self, acuracy, recall, roc_auc, precision):  
        self.acuracy = acuracy
        self.recall = recall
        self.roc_auc = roc_auc
        self.precision = precision
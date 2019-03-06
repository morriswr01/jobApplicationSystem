import random
import pickle
import pandas

# Load libraries
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import linear_model

def preprocess(data):
    le = preprocessing.LabelEncoder()
    data['Degree Qualification'] = le.fit_transform(data['Degree Qualification'])
    data['Degree Level'] = le.fit_transform(data['Degree Level'])
    data['University Attended'] = le.fit_transform(data['University Attended'])
    return data

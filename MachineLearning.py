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


import masterML

def applyModel(model, data):
    data = masterML.preprocess(data)
    cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_learn = data[cols]
    pred = model.predict(data_learn)
    acceptedApplicants = []
    count0 = 0
    count1 = 0
    for x in range(len(pred)):
        if pred[x] == 1:
            count1 += 1
            acceptedApplicants.append(x)
            acceptedApplicants.append(", ")
        else:
            count0 += 1
    print("Rejected Applicants: ",count0)
    print("Accepted Applicants: ",count1)
    return acceptedApplicants

def retrain(model, data, dataAdd):
    data = masterML.preprocess(data)
    dataAdd = masterML.preprocess(dataAdd)
    data_full = pandas.concat([data, dataAdd], ignore_index=True)
    print(data_full)
    cols = [col for col in data_full.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_learn = data_full[cols]
    target = data_full['Accepted']
    data_train, data_test, target_train, target_test = train_test_split(data_learn,target, test_size = 0.20, random_state = 1)

    model.fit(data_train, target_train)

pandas.options.mode.chained_assignment = None
# Load dataset
csw_url = "cvDataset.json"
csw_dataset = pandas.read_json(csw_url, orient='columns')
AcceptedArray = [0 for x in range(100000)]
Accepted = pandas.Series(AcceptedArray)

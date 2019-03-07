#Load libraries
import pickle
import pandas

from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

import masterML

def applyModel(modelName, data):
    #Load the appropriate model in using pickle and preprocess the input data so the model can analyse it.
    model = pickle.load(open(modelName, 'rb'))
    data = masterML.preprocess(data)

    #Get the appropriate data from the dataset and then analyse it using the machine learning model, putting
    # all the results (aka. if given application was accepted or rejected) into a list.
    cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_learn = data[cols]
    pred = model.predict(data_learn)
    acceptedApplicants = []

    #Make a list of all the successful applicants and then return it.
    for x in range(len(pred)):
        if pred[x] == 1:
            acceptedApplicants.append(x)
            acceptedApplicants.append(", ")
    return acceptedApplicants

def analyseApplication(modelName, data):
    #This function works similar to the previous one. However, it only analyses one application and
    # returns True or False if the application has been accepted or rejected respectively.
    model = pickle.load(open(modelName, 'rb'))
    apl = pandas.read_json(data, orient='columns')
    data = masterML.preprocess(data)
    pred = model.predict(apl)
    if pred[0] == 1:
        return True
    else:
        return False

def retrain(model, data, dataAdd):
    #This function takes in two sets of data - the dataset the model worked with before, and the additional data
    # it is being supplied. It then joins the two datasets together and retrains the model on the combined
    # dataset.
    data = masterML.preprocess(data)
    dataAdd = masterML.preprocess(dataAdd)
    data_full = pandas.concat([data, dataAdd], ignore_index=True)
    print(data_full)
    cols = [col for col in data_full.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_learn = data_full[cols]
    target = data_full['Accepted']
    data_train, data_test, target_train, target_test = train_test_split(data_learn,target, test_size = 0.20, random_state = 1)
    model.fit(data_train, target_train)

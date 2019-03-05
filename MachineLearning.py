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

def applyModel(model, data):
    dataset = pandas.read_json(data, orient='columns')
    cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_learn = data[cols]
    pred = model.predict(data_learn)
    acceptedApplicants = []
    for x in range(len(pred)):
        if pred[x] == 1:
            acceptedApplicants.append(x)
            acceptedApplicants.append(": ")
            acceptedApplicants.append(names[x])
    return acceptedApplicants

def preprocess(data):
    le = preprocessing.LabelEncoder()
    data['Degree Qualification'] = le.fit_transform(data['Degree Qualification'])
    data['Degree Level'] = le.fit_transform(data['Degree Level'])
    data['University Attended'] = le.fit_transform(data['University Attended'])
    return data

def retrain(model, data, dataAdd):
    data_full = pandas.concat([data, dataAdd], ignore_index=True)
    cols = [col for col in data_full.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data_retrain = data_full[cols]
    target_retrain = data_full['Accepted']
    target_test = data_full['Accepted']
    model.partial_fit(data_retrain, target_retrain)
    pred = model.predict(data_retrain)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    pickle.dump(model, open(jobs[x], 'wb'))
    for x in range(len(pred)):
        list.append(pred[x])
        print(pred[x])
    print(list)

pandas.options.mode.chained_assignment = None
# Load dataset
csw_url = "cvDataset.json"
csw_dataset = pandas.read_json(csw_url, orient='columns')
statusArray = [0 for x in range(100000)]
Status = pandas.Series(statusArray)
csw_dataset = csw_dataset.assign(Status=Status.values)

#model = pickle.load(open('Models/model', 'rb'))
#applyModel(model, data_partial)



#csw_partialfit = csw_dataset.head(100000)
#end = 0
#while end == 0:
#    x = random.randint(1, 100001)
#    application = csw_dataset[x:x+1]
#    end = analyseApplication(model, application, x)

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
    data = preprocess(data)
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

def preprocess(data):
    le = preprocessing.LabelEncoder()
    data['Degree Qualification'] = le.fit_transform(data['Degree Qualification'])
    data['Degree Level'] = le.fit_transform(data['Degree Level'])
    data['University Attended'] = le.fit_transform(data['University Attended'])
    return data

def retrain(model, data, dataAdd):
    data = preprocess(data)
    dataAdd = preprocess(dataAdd)
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
csw_dataset = csw_dataset.assign(Accepted=Accepted.values)
csw_partial = csw_dataset.head(20000)
csw_partial_2 = csw_dataset[30000:40000]
for x in range(csw_partial.shape[0]):
    print(x)
    if random.randint(1,101) > 50:
        csw_partial.set_value(x, 'Accepted', 1)
    else:
        csw_partial.set_value(x, 'Accepted', 0)
for x in range(csw_partial_2.shape[0]):
    print(x)
    if random.randint(1,101) > 50:
        csw_partial_2.set_value(x+30000, 'Accepted', 1)
    else:
        csw_partial_2.set_value(x+30000, 'Accepted', 0)


model = pickle.load(open('model', 'rb'))
applyModel(model, csw_dataset)



#csw_partialfit = csw_dataset.head(100000)
#end = 0
#while end == 0:
#    x = random.randint(1, 100001)
#    application = csw_dataset[x:x+1]
#    end = analyseApplication(model, application, x)

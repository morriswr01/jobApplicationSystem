
# Check the versions of libraries

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import random
import pickle

# Load libraries
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import linear_model

#A-Level Qualifications - Subject
#Languages Known - Language
#Previous Employment - Position
#Skills - Skill
#Hobbies - Name



#print(csw_dataset.groupby('University Attended').size())

def makeInitialModels():
    pandas.options.mode.chained_assignment = None
    # Load dataset
    csw_url = "cvDataset.json"
    csw_dataset = pandas.read_json(csw_url, orient='columns')
    csw_dataset = csw_dataset.head(100000)

    # create the Labelencoder object

    #Create an additional column for if the application was successful or not.
    acceptedArray = [0 for x in range(100000)]
    Accepted = pandas.Series(acceptedArray)
    csw_dataset = csw_dataset.assign(Accepted=Accepted.values)

    #jobs = ['Devops', 'FullStack', 'Hadoop', 'Java', 'QA', 'UI']
    jobs = ['QA', 'UI', 'Devops', 'FullStack', 'Hadoop', 'Java']
    Devops = GaussianNB()
    FullStack = GaussianNB()
    Hadoop = GaussianNB()
    Java = GaussianNB()
    QA = GaussianNB()
    UI = GaussianNB()


    #models = [Devops, FullStack, Hadoop, Java, QA, UI]
    models = [QA, Devops, FullStack, Hadoop, Java, UI]

    for x in range(1):

        print(jobs[x])
        print(models[x])
        for z in range(csw_dataset.shape[0]):
            csw_dataset.set_value(z, 'Accepted', 0)
        for y in range(csw_dataset.shape[0]):
            if csw_dataset.iloc[y]['Accepted'] == 1:
                print("Something went wrong")
        data = simulate(csw_dataset, jobs[x])
        model = models[x]
        data = preprocess(data)
        cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
        learn_data = data[cols]
        target = data['Accepted']
        data_train, data_test, target_train, target_test = train_test_split(learn_data,target, test_size = 0.20, random_state = 1)
        model.fit(data_train, target_train)
        #applyModel(gnb_devops)
        pred = model.predict(data_test)
        print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
        pickle.dump(model, open(jobs[x], 'wb'))

def simulate(data, model):
    for x in range(data.shape[0]):
        points = 0
        degree = data.iloc[x]['Degree Qualification']
        #p_languages = data.iloc[x]['Languages Known']
        p_languages = pandas.DataFrame.from_dict(data.iloc[x]['Languages Known'])
        p_employment = data.iloc[x]['Previous Employment']

        if model == 'Devops':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["Python", "Java", "Bash", "Ruby"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            if points > 12:
                data.set_value(x, 'Accepted', 1)

        elif model == 'FullStack':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["HTML", "CSS", "Javascript", "Angular", "Bootstrap", "React", "D3", "Node.js", "SQL"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            #points += 5*len(p_employment)
            if points > 12:
                data.set_value(x, 'Accepted', 1)

        elif model == 'Hadoop':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["Python", "Java", "Bash", "Ruby"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            #points += 5*len(p_employment)
            if points > 12:
                data.set_value(x, 'Accepted', 1)

        elif model == 'Java':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y]in str(degree):
                    points += 8
            p_language_list = ["Java", "CSS", "Javascript", "Bash", "Ruby"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 3
            #points += 5*len(p_employment)
            if points > 12:
                data.set_value(x, 'Accepted', 1)

        elif model == 'QA':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["SQL", "MySQL", "Unix Shell"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            #points += 5*len(p_employment)
            if points > 12:
                data.set_value(x, 'Accepted', 1)

        elif model == 'UI':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["HTML", "CSS", "Javascript", "Bash", "Ruby"]
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            #points += 5*len(p_employment)
            if points > 12:
                data.set_value(x, 'Accepted', 1)

    return data

def numerize(data):
    a_level_subject = []
    a_level_score = []
    a_level_dict = {}
    for x in range(data.shape[0]):
        data_piece = data.iloc[x][data]
        dataframe = pandas.DataFrame.from_dict(data_piece)
        for x in range(dataframe.shape[0]):
            if dataframe.iloc[x][1] not in a_level_subject:
                a_level_subject.append(dataframe.iloc[x][1])
            if dataframe.iloc[x][0] not in a_level_score:
                a_level_score.append(dataframe.iloc[x][0])
    count = 0
    for x in range(len(a_level_subject)):
        for y in range(len(a_level_score)):
            a_level_dict[(a_level_subject[x], a_level_score[y])] = count
            count = count + 1
    return a_level_dict

def preprocess_objects(data, object):
    dict = numerize(object)
    for x in range(data.shape[0]):
        data_piece = data.iloc[x][object]
        points = 0
        for y in range(len(data_piece)):
            subject = data_piece[y]
            tuple = (list(subject.values())[0], list(subject.values())[1])
            points = points + dict.get(tuple)
        data.set_value(x, object, points)





def preprocess(data):
    le = preprocessing.LabelEncoder()
    data['Degree Qualification'] = le.fit_transform(data['Degree Qualification'])
    data['Degree Level'] = le.fit_transform(data['Degree Level'])
    data['University Attended'] = le.fit_transform(data['University Attended'])
    return data
    #preprocess_objects('A-Level Qualifications')
    #preprocess_objects('Languages Known')
    #preprocess_objects('Previous Employment')
    #preprocess_objects('Skills')
    #preprocess_objects('Hobbies')
    #csw_dataset['Languages Known'] = le.fit_transform(csw_dataset['Languages Known'])
    #csw_dataset['Previous Employment'] = le.fit_transform(csw_dataset['Previous Employment'])
    #csw_dataset['Skills'] = le.fit_transform(csw_dataset['Skills'])
    #csw_dataset['Hobbies'] = le.fit_transform(csw_dataset['Hobbies'])

def makeModel(data, modelname):
    model = GaussianNB()
    cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    learn_data = data[cols]
    target = data['Accepted']
    data_train, data_test, target_train, target_test = train_test_split(data,target, test_size = 0.20, random_state = 1)
    model.fit(data_train, target_train)
    #applyModel(gnb_devops)
    pred = gnb_devops.predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
    pickle.dump(model, open(modelname, 'wb'))


def applyModel(model):
    cols = [col for col in csw_dataset.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    data = csw_dataset[cols]
    pred = model.predict(data)
    print("Analysed")
    for x in range(len(pred)):
        print(pred[x])

#def predict():
#    model = makeModel()
#    pred = model.predict(data_test)
#    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))
makeInitialModels()

#print(csw_dataset.groupby('Degree Qualification').size())

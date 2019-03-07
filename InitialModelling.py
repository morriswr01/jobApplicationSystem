#Load libraries
import pandas
import pickle


from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

import masterML


#This function makes models for the 6 job descriptions provided by the client.
#The data used here comes from the json test data provided by the client.
def makeInitialModels():
    pandas.options.mode.chained_assignment = None
    csw_url = "cvDataset.json"
    csw_dataset = pandas.read_json(csw_url, orient='columns')

    #Create an additional column in the json dataset for if the application was successful or not.
    StatusArray = [0 for x in range(100000)]
    Status = pandas.Series(StatusArray)
    csw_dataset = csw_dataset.assign(Status=Status.values)

    #Generate model names and models for the six jobs.

    jobs = ['Devops', 'FullStack', 'Hadoop', 'Java', 'QA', 'UI']
    Devops = GaussianNB()
    FullStack = GaussianNB()
    Hadoop = GaussianNB()
    Java = GaussianNB()
    QA = GaussianNB()
    UI = GaussianNB()


    models = [Devops, FullStack, Hadoop, Java, QA, UI]

    #Train the six models using the json dataset. This produces six models that are able to
    # analyse applications and predict whether they should be successful or not.
    for x in range(6):
        trainModel(csw_dataset, jobs[x], models[x])

def trainModel(dataSet, modelName, model):
    #Assign acceptance or rejection to the applications in the dataset based on what job the
    # input model is for. These will be used to train the model on what applications are
    # good or not.
    data = simulate(dataSet, modelName)
    #Preprocess the data into integer values so that it can be analysed by the machine leaning model.
    data = masterML.preprocess(data)

    #Split the data into the learning data (data that the ML will analyse/learn from) and the target data
    # (the data that the ML will try to predict when trained). Then split these two sets into two further sets
    # of data - a training set to train the model on and a testing set to test the model's accuracy.
    cols = [col for col in data.columns if col in ['University Attended', 'Degree Qualification', 'Degree Level']]
    learn_data = data[cols]
    target = data['Status']
    data_train, data_test, target_train, target_test = train_test_split(learn_data,target, test_size = 0.20, random_state = 1)
    model.fit(data_train, target_train)
    pred = model.predict(data_test)
    print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))

    #Use pickle to save the model for further use in the program.
    pickle.dump(model, open(modelName, 'wb'))


def simulate(data, model):
    for x in range(data.shape[0]):
        #Each application in the dataset is either 'rejected' or 'accepted' depending on its'
        # performance in a programmed "test". The application is scored points depending on
        # whether the applicant has a high-quality degree in a relevant field and how much
        # experience with relevant programming languages they have.
        data.set_value(x, 'Status', 0)
        points = 0
        degree = data.iloc[x]['Degree Qualification']
        p_languages = pandas.DataFrame.from_dict(data.iloc[x]['Languages Known'])

        if model == 'Devops':
            degrees_list = ["Computer Science", "Engineering", "Economics", "Business", "Mathematics"]
            #If the applicant has a degree in an appropriate subject for the job (BSc or MEng), score them points.
            for y in range(len(degrees_list)):
                if degrees_list[y] in str(degree):
                    points += 8
            p_language_list = ["Python", "Java", "Bash", "Ruby"]
            #If the applicant has experise in a relevant programming language, score them points based
            # on how much expertise they have with the language
            for z in range(len(p_language_list)):
                for l in range(p_languages.shape[0]):
                    if p_language_list[z] == p_languages.iloc[l]['Language']:
                        points += points + p_languages.iloc[l]['Expertise']
            #If the applicant passed their degree with a 1st, score them points.
            if data.iloc[x]['Degree Level'] == "1st":
                points += 5
            #If the applicant scored enough points, accept their application.
            if points > 12:
                data.set_value(x, 'Status', 1)

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
            if points > 12:
                data.set_value(x, 'Status', 1)

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
            if points > 12:
                data.set_value(x, 'Status', 1)

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
            if points > 12:
                data.set_value(x, 'Status', 1)

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
            if points > 12:
                data.set_value(x, 'Status', 1)

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
            if points > 12:
                data.set_value(x, 'Status', 1)
    return data

makeInitialModels()

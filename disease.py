import pandas as pd
import numpy as np
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# def dataset():
#     df=pd.read_csv('diabetes_data_upload.csv')
#     print(df.head())
#     df['Gender']=df['Gender'].map({'Male':1,'Female':0})
#     df['Polyuria']=df['Polyuria'].map({'Yes':1,'No':0})
#     df['Polydipsia']=df['Polydipsia'].map({'Yes':1,'No':0})
#     df['weakness']=df['weakness'].map({'Yes':1,'No':0})
#     df['visual blurring']=df['visual blurring'].map({'Yes':1,'No':0})
#     df['Itching']=df['Itching'].map({'Yes':1,'No':0})
#     df['Obesity']=df['Obesity'].map({'Yes':1,'No':0})
#     df['sudden weight loss']=df['sudden weight loss'].map({'Yes':1,'No':0})
#     df['Polyphagia']=df['Polyphagia'].map({'Yes':1,'No':0})
#     df['Genital thrush']=df['Genital thrush'].map({'Yes':1,'No':0})
#     df['Irritability']=df['Irritability'].map({'Yes':1,'No':0})
#     df['delayed healing']=df['delayed healing'].map({'Yes':1,'No':0})
#     df['partial paresis']=df['partial paresis'].map({'Yes':1,'No':0})
#     df['muscle stiffness']=df['muscle stiffness'].map({'Yes':1,'No':0})
#     df['Alopecia']=df['Alopecia'].map({'Yes':1,'No':0})

#     df['class']=df['class'].map({'Positive':1,'Negative':0})

#     train_x, test_x = train_test_split(df, test_size = 0.35)
#     pred_var = ['Age','Gender','Polyuria','Polydipsia','weakness','visual blurring','Itching','Obesity','sudden weight loss','Polyphagia','Genital thrush','Irritability',
#                 'delayed healing','partial paresis','muscle stiffness','Alopecia']
#     outcome_var='class'
#     model=LinearRegression()
#     model.fit(train_x[pred_var],train_x[outcome_var])
#     prediction=model.predict(train_x[pred_var])
#     print("Variance score: {}".format(model.score(train_x[pred_var],train_x[outcome_var])))

#     input=[ [48,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1] ]  
#     output=model.predict(input) #0 means non-diabetic, 1 means diabetic
#     print(input,np.round_(output))
    
    
    
    
    
def learner(bloodPressure,cholestrol,bmi,smoker,heartDisease,physicalActivity,alcohol,generalHealth,mentalHealth,physicalHealth,diffWalking,gender,age,education,fruit,veggies):                                                                                                   
    file = pd.read_csv('diabetes_01.csv')
    featured=['HighBP','HighChol','BMI','Smoker','HeartDiseaseorAttack','PhysActivity','HvyAlcoholConsump','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Fruits','Veggies']
    x=file[featured]
    y=file.Diabetes
    x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7)

    print("first algo: ")

    model=LogisticRegression(max_iter=253000)

    model.fit(x_train.values,y_train)
    y_predict=model.predict([[int(bloodPressure),int(cholestrol),int(bmi),int(smoker),int(heartDisease),int(physicalActivity),int(alcohol),int(generalHealth),int(mentalHealth),int(physicalHealth),int(diffWalking),int(gender),int(age),int(education),int(fruit),int(veggies)]])
    # y_predict=model.predict([[1,1,40,1,0,0,0,5,18,15,1,0,9,4,0,1]])
    return(y_predict)




    # model=LogisticRegression(max_iter=253000)

    # model.fit(x_train.values,y_train)
    # y_predict=model.predict([[int(bloodPressure),int(cholestrol),int(bmi),int(smoker),int(heartDisease),int(physicalActivity),int(alcohol),int(generalHealth),int(mentalHealth),int(physicalHealth),int(diffWalking),int(gender),int(age),int(education),int(fruit)]])
    # # print("Predict:",y_predict)
    # # print(model.score("Score:",x_test,y_test))
    # return(y_predict)
    













# x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=1)
# # print('rows in total set : {}'.format(df.shape[0]))
# # print('rows in training set : {}'.format(x_train.shape[0]))
# # print('rows in test set : {}'.format(x_test.shape[0]))
# cv = CountVectorizer()
# training_data = cv.fit_transform(x_train)
# # print("training ",training_data)
# # print("get feature ",cv.get_feature_names())
# testing_data = cv.transform(x_test)
# # print('test data: ',testing_data)
# naive_bayes = MultinomialNB()
# naive_bayes.fit(training_data, y_train)
# predictions = naive_bayes.predict(testing_data)
# print('The predictions was : ', predictions)
# print('The accuracy is: ', format(accuracy_score(y_test, predictions)*100))



    # df=pd.read_csv('diabetes_012.csv')
    # print(df.head())
    # x=df.drop('Diabetes_012',axis=1)
    # y=df['Diabetes_012']
    # train_x, test_x = train_test_split(df, test_size = 0.3)
    # pred_var = ['HighBP','HighChol','BMI','Smoker','HeartDiseaseorAttack','PhysActivity','HvyAlcoholConsump','GenHlth','MentHlth','PhysHlth','DiffWalk','Sex','Age','Education','Income']
    # outcome_var='Diabetes_012'
    # model=LinearRegression()
    # model.fit(train_x[pred_var],train_x[outcome_var])
    # prediction=model.predict(train_x[pred_var])
    # print("Variance score: {}".format(model.score(train_x[pred_var],train_x[outcome_var])))





    # df=pd.read_csv('pima-indians-diabetes.csv')
    # print(df.head())
    # # x=df.drop('Class',axis=1)
    # # y=df['Class']
    # train_x, test_x = train_test_split(df, test_size = 0.3)
    # pred_var = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    # outcome_var='Class'
    # model=LinearRegression()
    # model.fit(train_x[pred_var],train_x[outcome_var])
    # prediction=model.predict(train_x[pred_var])
    # print("Variance score: {}".format(model.score(train_x[pred_var],train_x[outcome_var])))
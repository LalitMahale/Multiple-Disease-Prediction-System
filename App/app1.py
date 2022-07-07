import streamlit as sm
import pickle

dia_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\diabetes_model.sav","rb"))
heart_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\heart_model.sav","rb"))
par_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\parkinsons.sav","rb"))


sm.title("Multiple Disease Prediction System")


menu = sm.sidebar.selectbox("Multiple Disease Prediction System", ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"])
if (menu == "Diabetes Prediction" ):
    # page title
    sm.title("Diabetes Prediction")

    pre = sm.selectbox("Pregnancies(Weeks)", sorted([ 6,  1,  8,  0,  5,  3, 10,  2,  4,  7,  9, 11, 13, 15, 17, 12, 14]))
    glucose = sm.number_input("Glucose")
    bp = sm.number_input("BloodPressure")
    ST = sm.number_input("SkinThickness")
    ins = sm.number_input("Insulin")
    bmi = sm.number_input("BMI")
    dpf = sm.number_input('Diabetes Pedigree Function')
    age = sm.number_input("Age")
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if sm.button('Diabetes Test Result'):
        diab_prediction = dia_model.predict([[pre,glucose,bp,ST,ins,bmi,dpf,age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    sm.success(diab_diagnosis)

# =============================================================================
# 
# =============================================================================


if (menu == "Heart Disease Prediction"):

    sm.title("Heart Disease Prediction")
    
    
    age = sm.text_input('Age')
    
    sex = sm.selectbox('Sex  (Male - 1 , Female - 0)',[1,0])

    cp = sm.text_input('Chest Pain types')
    
    trestbps = sm.text_input('Resting Blood Pressure')
    
    chol = sm.text_input('Serum Cholestoral in mg/dl')
    
    fbs = sm.text_input('Fasting Blood Sugar > 120 mg/dl')
    
    restecg = sm.text_input('Resting Electrocardiographic results')
    
    thalach = sm.text_input('Maximum Heart Rate achieved')
    
    exang = sm.text_input('Exercise Induced Angina')
    
    oldpeak = sm.text_input('ST depression induced by exercise')
    
    slope = sm.text_input('Slope of the peak exercise ST segment')
    
    ca = sm.text_input('Major vessels colored by flourosopy')
    
    thal = sm.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if sm.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    sm.success(heart_diagnosis)
        
    
    
    
    
# =============================================================================
#     
#     
# =============================================================================
if (menu == "Parkinsons Prediction"):

    sm.title("Parkinsons Prediction")
    
    fo = sm.text_input('MDVP:Fo(Hz)')
    
    fhi = sm.text_input('MDVP:Fhi(Hz)')
    
    flo = sm.text_input('MDVP:Flo(Hz)')
    
    Jitter_percent = sm.text_input('MDVP:Jitter(%)')
    
    Jitter_Abs = sm.text_input('MDVP:Jitter(Abs)')
    
    RAP = sm.text_input('MDVP:RAP')
    
    PPQ = sm.text_input('MDVP:PPQ')
    
    DDP = sm.text_input('Jitter:DDP')
    
    Shimmer = sm.text_input('MDVP:Shimmer')
    
    Shimmer_dB = sm.text_input('MDVP:Shimmer(dB)')
    
    APQ3 = sm.text_input('Shimmer:APQ3')
    
    APQ5 = sm.text_input('Shimmer:APQ5')
    
    APQ = sm.text_input('MDVP:APQ')
    
    DDA = sm.text_input('Shimmer:DDA')
    
    NHR = sm.text_input('NHR')
    
    HNR = sm.text_input('HNR')
    
    RPDE = sm.text_input('RPDE')
    
    DFA = sm.text_input('DFA')
    
    spread1 = sm.text_input('spread1')
    
    spread2 = sm.text_input('spread2')
    
    D2 = sm.text_input('D2')
    
    PPE = sm.text_input('PPE')
    

    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if sm.button("Parkinson's Test Result"):
        parkinsons_prediction = par_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    sm.success(parkinsons_diagnosis)


    








# =============================================================================
# 
# =============================================================================

rad = sm.sidebar.radio("Navigation",["Home","About us","Contact us"])

if rad == "Home":
    sm.write("Thanks for using this .....")

elif rad == "About us":
    sm.write("""Hi, I'm Lalit Mahale who develop this Multi disease application for help to people
             in their life """)
    sm.write("Training Datasets Taken from Kaggle and their link is given below")
    sm.write("""Diabetes Dataset - https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database """)
    sm.write("Heart Disease Dataset - https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset ")
    sm.write(' Parkinsons Data Set - https://www.kaggle.com/datasets/nidaguler/parkinsons-data-set')
    sm.write("For see read and download code plz visite my github link \n https://github.com/LalitMahale/Multiple-Disease-Prediction-System.git")
    sm.write("Follow at Linkdin - https://www.linkedin.com/in/lalitmahale1997 ")

    
else:
    sm.write("Email:- mahalelalit45@gmail.com")


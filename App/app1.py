import streamlit as sm
import pickle

dia_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\diabetes_model.sav","rb"))
heart_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\heart_model.sav","rb"))
par_model = pickle.load(open(r"C:\Users\lalit\Desktop\Projects\multi project in one\Multiple Disease Prediction System\ML models\parkinsons.sav","rb"))


sm.title("Multiple Disease Prediction System")


menu = sm.sidebar.selectbox("Multiple Disease Prediction System", ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction","BMI Calculator"])
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
    
    fbs = sm.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)',[0,1])
    
    restecg = sm.text_input('Resting Electrocardiographic results')
    
    thalach = sm.text_input('Maximum Heart Rate achieved')
    
    exang = sm.selectbox('Exercise Induced Angina (1 = yes; 0 = no)',[0,1])
    
    oldpeak = sm.text_input('ST depression induced by exercise')
    
    slope = sm.text_input('Slope of the peak exercise ST segment')
    
    ca = sm.text_input('Major vessels colored by flourosopy')
    
    thal = sm.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',[0,1,2])
    
    
     
     
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

if (menu == "BMI Calculator"):
    weight = sm.number_input("Weight (Kg)")
    height = sm.number_input("height (cm)")
    
    if sm.button("Calculate"):
        
        bmi = (weight / (height * height)) * 10000
    
        sm.success(bmi)





# =============================================================================
# 
# =============================================================================

rad = sm.sidebar.radio("Navigation",["Home","About us","Contact us","Help"])

if rad == "Home":
    sm.write("Thanks for using this .....")

elif rad == "About us":
    
    about = sm.selectbox("About Dataset and developer",["Dataset Source","About Developer"])
    if about == "Dataset Source":
        sm.write("Training Datasets Taken from Kaggle and their link is given below")
        sm.write("""Diabetes Dataset - https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database """)
        sm.write("Heart Disease Dataset - https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset ")
        sm.write(' Parkinsons Data Set - https://www.kaggle.com/datasets/nidaguler/parkinsons-data-set')
        sm.write("For see read and download code plz visite my github link \n https://github.com/LalitMahale/Multiple-Disease-Prediction-System.git")
        sm.write("Follow at Linkdin - https://www.linkedin.com/in/lalitmahale1997 ")
    else:
        sm.write("""Hi, I'm Lalit Mahale, I have done My Post Graduate Diploma in Artificial Intelligence in Artificial Intelligent from CDAC (act's) Pune """)
    
elif rad == "Contact us":
    sm.write("Email:- mahalelalit45@gmail.com")
    
else:
    
    helps = sm.selectbox("Help about Data information",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"])
    
    if helps == "Diabetes Prediction":
            sm.write('''Pregnancies : - Number of times pregnant ''')
            sm.write('fasting blood sugar :- ( 120 mg/dl) (1 = true; 0 = false)')
            sm.write('BloodPressure :- Diastolic blood pressure (mm Hg)')
            sm.write('SkinThickness :- Triceps skin fold thickness (mm)')
            sm.write('Insulin :- 2-Hour serum insulin (mu U/ml)')
            sm.write('BMI :- Body mass index')    
            sm.write('Diabetes Pedigree Function :-  Diabetes pedigree function')

    if helps == "Heart Disease Prediction":
            sm.write('''resting blood pressure :-  in mm Hg on admission to the hospital  ''')
            sm.write(''' chest pain type (4 values) ''')         
            sm.write(''' chest pain type (4 values) ''')         
            sm.write(''' fasting blood sugar > 120 mg/dl ''')         
            sm.write(''' resting electrocardiographic results (values 0,1,2)''')         
            sm.write(''' oldpeak = ST depression induced by exercise relative to rest ''')         
            sm.write(''' the slope of the peak exercise ST segment ''')         
            sm.write(''' number of major vessels (0-3) colored by flourosopy ''')         
            sm.write(''' thal: 0 = normal; 1 = fixed defect; 2 = reversable defect ''')         


                
                
    if helps == "Parkinsons Prediction":
            sm.write('''MDVP:Fo(Hz) - Average vocal fundamental frequency''')
            sm.write('''MDVP:Fhi(Hz) - Maximum vocal fundamental frequency ''')
            sm.write('''MDVP:Fhi(Hz) - Maximum vocal fundamental frequency''')
            sm.write('''MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several measures of variation in fundamental frequency''')
            sm.write('''MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude ''')
            sm.write('''NHR,HNR - Two measures of ratio of noise to tonal components in the voice''')
            sm.write('''status - Health status of the subject (one) - Parkinson's, (zero) - healthy ''')
            sm.write('''RPDE,D2 - Two nonlinear dynamical complexity measures''')
            sm.write('''DFA - Signal fractal scaling exponent''')
            sm.write('''spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation''')


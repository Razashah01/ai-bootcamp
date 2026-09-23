import numpy as np
import pandas as pd

def preprocess(df):
    df=df.drop("customerID", axis=1)  
    df['TotalCharges'] = df['TotalCharges'].replace(" ", np.nan)  # replace empty values with NaN
    df['TotalCharges'] = df['TotalCharges'].astype(float)  # change its datatype
    df['TotalCharges'] = df['TotalCharges'].fillna(df["TotalCharges"].mean())   # fill the empty(NaN) values with the mean of whole column
    #encoding binary columns
    df['gender']= df['gender'].replace({'Male':0,'Female':1})
    df['Partner']= df['Partner'].replace({'No':0,'Yes':1})
    df['Dependents']= df['Dependents'].replace({'No':0,'Yes':1})
    df['PhoneService']= df['PhoneService'].replace({'No':0,'Yes':1})
    df['PaperlessBilling']= df['PaperlessBilling'].replace({'No':0,'Yes':1})
    # converting them into binary
    # now handling multi-columns with one-hot-encoding
    binary_cols = ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    df[binary_cols] = df[binary_cols].astype(int)

    df = pd.get_dummies(df, columns=['MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaymentMethod'])
    df = df.astype({col: int for col in df.select_dtypes(include='bool').columns})

    if 'Churn' in df.columns:
        df = df.drop('Churn', axis=1)

    return df
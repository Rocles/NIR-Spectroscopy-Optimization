# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(df):
    # Encode categorical variables
    le_type_manure = LabelEncoder()
    df['type_manure'] = le_type_manure.fit_transform(df['type_manure'])

    le_spectrometer = LabelEncoder()
    df['spectrometer'] = le_spectrometer.fit_transform(df['spectrometer'])

    le_township = LabelEncoder()
    df['township'] = le_township.fit_transform(df['township'])

    le_country = LabelEncoder()
    df['country'] = le_country.fit_transform(df['country'])

    # Imputer les valeurs manquantes avec la moyenne
    df.fillna(df.mean(numeric_only=True), inplace=True)

    return df

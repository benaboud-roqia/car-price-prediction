import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# This script extracts the model training code from your notebook
# and saves the trained model for use in the web interface

# Sample data creation (based on your notebook structure)
# In a real scenario, you would load your actual dataset
data = {
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2015, 2016, 2017, 2018],
    'Kms_numerique': [50000, 45000, 40000, 35000, 30000, 25000, 60000, 55000, 50000, 45000],
    'Company': ['Maruti', 'Hyundai', 'Honda', 'Toyota', 'Ford', 'BMW', 'Audi', 'Mercedes', 'Chevrolet', 'Renault'],
    'Fuel_type': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol', 'Diesel'],
    'Prix_numerique': [400000, 500000, 600000, 700000, 800000, 1500000, 2000000, 2500000, 300000, 400000]
}

df = pd.DataFrame(data)

# Prepare data for modeling (similar to your notebook)
df_model = df[['Year', 'Kms_numerique', 'Prix_numerique', 'Company', 'Fuel_type']].copy()

# Simple encoding of categorical variables
company_mapping = {company: idx for idx, company in enumerate(df_model['Company'].unique())}
fuel_mapping = {fuel: idx for idx, fuel in enumerate(df_model['Fuel_type'].unique())}

df_model['Company_encoded'] = df_model['Company'].map(company_mapping)
df_model['Fuel_encoded'] = df_model['Fuel_type'].map(fuel_mapping)

# Features and target
X = df_model[['Year', 'Kms_numerique', 'Company_encoded', 'Fuel_encoded']]
y = df_model['Prix_numerique']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model and encoders
joblib.dump(model, 'car_price_model.pkl')
joblib.dump(company_mapping, 'company_mapping.pkl')
joblib.dump(fuel_mapping, 'fuel_mapping.pkl')

print("Model and encoders saved successfully!")
print("Company mapping:", company_mapping)
print("Fuel mapping:", fuel_mapping)
import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

# Feature names
features = ['Number ownwer', 'modelYear', 'centralVariantId', 'Mileage', 'Engine',	'Max Power',	
            'Torque', 'Seats', 'Age of car', 'Body_Type_numeric', 'Fuel_Type_numeric', 'Transmission_numeric']

# Categorical variable mappings
categorical_mappings = {
    'Fuel_Type_numeric': {'Petrol': 0, 'Diesel': 1, 'LPG': 4, 'CNG': 2, 'Electric': 3},
    'Body_Type_numeric': {'Hatchpack': 0, 'SUV': 1, 'Sedan': 2, 'MUV': 3, 'Coupe': 5,
                  'Minivans': 4, 'Pickup Trucks': 6, 'Convertibles': 7, 'Hybrids': 9, 'Wagon': 10},
    'Transmission_numeric': {'Automatic': 1, 'Manual': 0},
}

# Input widgets for user interaction
st.title("Car Price Prediction App")

input_data = {}
for feature in features:
    if feature in categorical_mappings:
        selected_option = st.sidebar.selectbox(f"Select {feature.capitalize()}:", options=list(categorical_mappings[feature].keys()))
        input_data[feature] = categorical_mappings[feature][selected_option]
    else:
        input_data[feature] = st.sidebar.number_input(f"{feature.replace('_', ' ').capitalize()}:")

# Make predictions using the loaded model
if st.sidebar.button("Predict"):
    input_array = np.array([input_data[feature] for feature in features]).reshape(1, -1)
    prediction = model.predict(input_array)

    # Display the selected feature values
    st.subheader("Selected Feature Values:")
    for feature, value in input_data.items():
        st.write(f"{feature.replace('_', ' ').capitalize()}: {value}")

    # Display the prediction result
    st.subheader("Prediction Result:")
    st.write(f"The estimated car price is: INR{prediction[0]:,.2f}")
import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model_2.pkl")  # change to your model file
    return model

model = load_model()

# -----------------------------
# App Title
# -----------------------------
st.title("🏠 House Price Prediction App")

st.write("Fill in the house details below:")

# -----------------------------
# Text Inputs (Numeric Fields)
# -----------------------------
area = st.text_input("Area (sq ft)")
bedrooms = st.text_input("Bedrooms")
bathrooms = st.text_input("Bathrooms")
stories = st.text_input("Stories")
parking = st.text_input("Parking Spaces")

# -----------------------------
# Yes/No Inputs
# -----------------------------
mainroad = st.selectbox("Main Road", ["yes", "no"])
guestroom = st.selectbox("Guest Room", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])

# -----------------------------
# Furnishing Status
# -----------------------------
furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["furnished", "semi-furnished", "unfurnished"]
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Price"):

    try:
        # Convert text inputs to numeric
        area = float(area)
        bedrooms = int(bedrooms)
        bathrooms = int(bathrooms)
        stories = int(stories)
        parking = int(parking)

        input_data = pd.DataFrame({
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "stories": [stories],
            "mainroad": [mainroad],
            "guestroom": [guestroom],
            "basement": [basement],
            "hotwaterheating": [hotwaterheating],
            "airconditioning": [airconditioning],
            "parking": [parking],
            "prefarea": [prefarea],
            "furnishingstatus": [furnishingstatus]
        })

        prediction = model.predict(input_data)
        price = float(prediction[0])

        st.success(f"Estimated House Price: ₦{price:,.2f}")

    except ValueError:
        st.error("Please enter valid numbers for Area, Bedrooms, Bathrooms, Stories, and Parking.")

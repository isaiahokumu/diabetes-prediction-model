# app.py
import streamlit as st
import pandas as pd
import pickle

from sklearn.metrics import accuracy_score, roc_auc_score

# Load your pipeline
# Train and save model first (run_diabetes_prediction_pipeline)
# Example: pickle.dump(pipeline, open("diabetes_pipeline.pkl", "wb"))
@st.cache_resource
def load_pipeline():
    with open("diabetes_pipeline.pkl", "rb") as f:
        return pickle.load(f)

pipeline = load_pipeline()

# Streamlit UI
st.title("🩺 Diabetes Prediction App")
st.write("This app predicts the likelihood of diabetes based on health and lifestyle features.")

# Sidebar navigation
app_mode = st.sidebar.selectbox("Choose mode", ["Manual Input", "Upload CSV"])

if app_mode == "Manual Input":
    st.subheader("Enter patient information:")

    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
    phys_health = st.slider("Physical Health (days unhealthy in last 30 days)", 0, 30, 5)
    high_bp = st.selectbox("High Blood Pressure", [0, 1])
    high_chol = st.selectbox("High Cholesterol", [0, 1])
    smoker = st.selectbox("Smoker", [0, 1])
    stroke = st.selectbox("Stroke", [0, 1])
    heart_disease = st.selectbox("Heart Disease/Attack", [0, 1])
    physical_activity = st.selectbox("Physical Activity", [0, 1])
    fruits = st.selectbox("Consumes Fruits", [0, 1])
    veggies = st.selectbox("Consumes Vegetables", [0, 1])
    alcohol = st.selectbox("Heavy Alcohol Consumption", [0, 1])
    gen_health = st.selectbox("General Health", ["Poor", "Fair", "Good", "Very Good", "Excellent"])
    sex = st.selectbox("Sex", ["Male", "Female"])
    age = st.slider("Age Category (numeric)", 18, 80, 35)
    income = st.slider("Income (approx bracket code)", 1, 8, 4)

    # Create dataframe for prediction
    input_data = pd.DataFrame([{
        "bmi": bmi,
        "phys_health": phys_health,
        "high_blood_pressure": high_bp,
        "high_cholesterol": high_chol,
        "smoker": smoker,
        "stroke": stroke,
        "heart_disease_or_attack": heart_disease,
        "physical_activity": physical_activity,
        "fruits": fruits,
        "veggies": veggies,
        "heavy_alcohol_consumption": alcohol,
        "gen_health": gen_health,
        "sex": sex,
        "age": age,
        "income": income
    }])

    if st.button("Predict"):
        prediction = pipeline.models["Logistic Regression"].predict(input_data)[0]
        proba = pipeline.models["Logistic Regression"].predict_proba(input_data)[0][1]
        st.write(f"### 🔮 Prediction: {'Diabetic' if prediction == 1 else 'Non-Diabetic'}")
        st.write(f"### Probability of Diabetes: {proba:.2%}")

elif app_mode == "Upload CSV":
    st.subheader("Upload your dataset (CSV format)")
    uploaded_file = st.file_uploader("Choose a file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("📊 Preview of uploaded data:")
        st.dataframe(df.head())

        if st.button("Predict for Uploaded Data"):
            preds = pipeline.models["Logistic Regression"].predict(df)
            df["Prediction"] = preds
            df["Prediction"] = df["Prediction"].map({0: "Non-Diabetic", 1: "Diabetic"})
            st.write("✅ Predictions complete")
            st.dataframe(df.head())

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions",
                data=csv,
                file_name="diabetes_predictions.csv",
                mime="text/csv"
            )

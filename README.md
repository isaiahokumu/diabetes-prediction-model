# Diabetes Prediction using BRFSS Survey Data


---

## 1. Project Selection

This project uses the **Behavioral Risk Factor Surveillance System (BRFSS)** dataset to develop machine learning models that predict whether a respondent has diabetes. The project follows a complete machine learning pipeline, including **problem definition, data understanding, preprocessing, modeling, evaluation, interpretation, and error analysis**.

---

## 2. Problem Definition
## Problem Statement

Diabetes is a chronic health condition that affects how the body regulates blood sugar (glucose). If left unmanaged, it can lead to severe complications such as heart disease, kidney failure, blindness (ROP), and premature death. Globally, diabetes prevalence is rising, putting significant strain on individuals, healthcare systems, and economies.

Early detection of diabetes aids in earlier management yet many people remain undiagnosed until symptoms become severe. Traditional diagnostic methods need clinical testing (e.g., blood glucose, HbA1c) which may not be accessible or affordable in all populations.

The objective of this project is to **develop a machine learning model that predicts whether an individual has diabetes using survey-based health, lifestyle, and demographic data**.

Who benefits from this model?
* **Healthcare providers** through early identification of high-risk individuals for further screening.
* **Public health organizations** that they mayallocate resources effectively.
* **Individuals** gain awareness of their risk factors and take preventive action.

ML Task
This is a **binary classification problem**:

* **Target variable**: Diabetes status (0 = No diabetes, 1 = Diabetes).
* **Input features**: Self-reported health indicators, lifestyle habits (e.g., BMI, physical activity), demographics, and chronic condition history.

---

## 3. Data Collection & Understanding

* **Exploration**:

  * **Shape**: 83,768 rows × 21 columns
  * **Data Types**: Numeric variables (e.g., BMI, age, physical/mental health days, general health).
  * **Missing Values**: Minimal, handled with imputation and dropping.
  * **Outliers**: Extreme BMI and age values explored during EDA.
  * **EDA Visualizations**:

    * Target distribution plot (balanced classes).
    * Histograms for BMI, age, physical health days.
    * Correlation heatmap.

---

## 4. Data Preprocessing

* **Steps performed**:

  * Missing values imputed (median strategy).
  * Made the dataset ML ready by ensuring columns follow a set encoding as opposed to the survey data
  * All variables treated as numeric (survey-coded).
  * Standardization applied via `StandardScaler`.
  * Data split: **80% train, 20% test**, stratified to preserve class balance.
 
* **Source**: BRFSS 2015, an annual U.S. health-related telephone survey ([CDC BRFSS Codebook](https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf)).

* **Dataset Used**: `diabetes_binary_5050_split.csv` (balanced 50/50 diabetic vs non-diabetic).

---

## 5. Modeling

* **Baseline Models**:

  * Logistic Regression (interpretable, linear baseline).
  * Random Forest (non-linear, captures feature interactions).

* **Hyperparameter Tuning**:

  * Logistic Regression: tuned regularization strength (C).
  * Random Forest: tuned number of trees, max depth.

* **Model Selection Rationale**:

  * Logistic Regression → Interpretability.
  * Random Forest → Captures non-linear patterns.

---

## 6. Evaluation

* **Metrics used**:

  * Accuracy
  * Precision
  * Recall
  * F1-score
  * ROC
  * AUC

* **Results**:

  * Logistic Regression: Accuracy 
  * Random Forest: Accuracy 
  

* **Visualizations**:

  * Confusion matrices.
  * ROC curves for both models.
  * Feature importance plots (coefficients for Logistic Regression, importance scores for Random Forest).

---

## 7. Error Analysis


---

## 8. Model Interpretation

* **Top features consistently important across models**:


* **Interpretation in plain terms**:

---

## 9. Deployment

* The model will be deployed in:

  1. **Streamlit App** – interactive diabetes risk calculator.


---

## 10. Project Report Structure

1. **Title & Abstract** – Diabetes prediction using BRFSS survey data.
2. **Problem Statement** – Diabetes classification.
3. **Data Collection & Understanding** – BRFSS 2015 dataset.
4. **Data Preprocessing** – Cleaning, scaling, splitting.
5. **Modeling Approach** – Logistic Regression, Random Forest.
6. **Results & Evaluation** – Metrics, ROC curves, feature importance.
7. **Error Analysis** – Misclassifications, limitations.
8. **Conclusion & Future Work** – Add clinical data, feature engineering, deploy app.

---

## Citations

1. CDC. *BRFSS 2015 Codebook.* [https://www.cdc.gov/brfss/annual\_data/2015/pdf/codebook15\_llcp.pdf](https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf)
2. Zhang X, Holt JB, Lu H, Wheaton AG, Ford ES, Greenlund KJ, Croft JB. *Multilevel regression and poststratification for small-area estimation of population health outcomes: A case study of chronic obstructive pulmonary disease prevalence using the Behavioral Risk Factor Surveillance System.* *Prev Chronic Dis.* 2019;16\:E09. doi:10.5888/pcd16.180571. [https://www.cdc.gov/pcd/issues/2019/19\_0109.htm](https://www.cdc.gov/pcd/issues/2019/19_0109.htm)

---


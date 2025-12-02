# Loan Prediction App

A machine learning-based application designed to predict whether a loan application is likely to be **approved** or **rejected** based on applicant details. This project demonstrates data preprocessing, exploratory analysis, model training, evaluation, and deployment-ready prediction code.

---

## 🚀 Project Overview
This project uses machine learning techniques to analyze historical loan application data and predict loan approval outcomes. It is designed to be simple, clean, and easy to extend into a real-world product or web app.

---

## 📂 Repository Structure
```
loan-prediction-app/
├── Loan_prediction.ipynb     # Complete workflow notebook (EDA + model training)
├── model.py                  # Script for loading model and making predictions
├── model.pkl                 # Trained machine learning model
├── train.csv                 # Training dataset
├── test.csv                  # Test dataset
├── requirements.txt          # Dependencies
└── screenshots/              # Output screenshots (optional)
```

---

## 📊 Dataset Details
The dataset contains information such as:
- Applicant Income
- Co-applicant Income
- Loan Amount
- Loan Term
- Credit History
- Dependents
- Education
- Property Area
- Marital Status

Each sample includes whether the loan was approved (`Loan_Status`).

---

## 🧠 Model Used
Several algorithms were tested, and the model with the best performance was selected (e.g., Logistic Regression / Random Forest / XGBoost). The final model is stored in `model.pkl` for deployment.

Key steps:
- Handling missing values
- Label encoding categorical variables
- Feature scaling (if needed)
- Splitting train/test sets
- Model evaluation (accuracy, confusion matrix, classification report)

---

## 🛠️ How to Run the Project
### 1. Clone the repository
```bash
git clone https://github.com/josephfrancis22/loan-prediction-app.git
cd loan-prediction-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook (optional)
Open the Jupyter Notebook:
```bash
jupyter notebook Loan_prediction.ipynb
```

### 4. Use the model for prediction
Run the Python script:
```bash
python model.py
```
This will load the saved model and run predictions on sample inputs.

---

## 📈 Model Performance
(Add your model results here — accuracy, AUC, confusion matrix screenshot)

Example:
- **Accuracy:** 0.81
- **Confusion Matrix:** (Add image or description)

---

## 🚀 Future Enhancements
- Add a **Streamlit or Flask web application** for user-friendly prediction
- Deploy app using **Streamlit Cloud / Render / Hugging Face Spaces**
- Improve hyperparameter tuning for better accuracy
- Add visualization dashboard

---

## 🤝 Contributing
Feel free to fork this repository, create a feature branch, and submit a pull request.

---

## 📧 Contact
**Joseph Francis**  
Data Science & Visualization Intern | Final-year Engineering Student  
From Chendiyarkara, Kerala  

If you found this project helpful, ⭐ star the repo!

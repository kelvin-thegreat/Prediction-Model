# Customer Churn Prediction Project

## Overview
This project is a complete end-to-end solution for predicting customer churn using machine learning. It includes:
- Data analysis and cleaning in a Jupyter notebook
- Feature engineering and model training (Logistic Regression, KNN, SVM, Decision Tree, Random Forest)
- Model selection and evaluation
- Exporting the best model and scaler
- A Streamlit web app for interactive churn prediction

## Project Structure
```
├── app.py                  # Streamlit web application for predictions
├── customer_churn_data.csv # Input data (not included, add your own)
├── scaler.pkl              # Saved StandardScaler object
├── model.pkl               # Saved best model
├── notebook.ipynb          # Jupyter notebook for EDA, training, and export
├── requirements.txt        # Python dependencies
└── .venv/                  # Python virtual environment (optional)
```

## How It Works
1. **Data Analysis & Cleaning**: Explore and clean the data in `notebook.ipynb`.
2. **Feature Engineering**: Select and transform features for modeling.
3. **Model Training**: Train and evaluate multiple models using GridSearchCV.
4. **Model Export**: Save the best model and scaler as `model.pkl` and `scaler.pkl`.
5. **Web App**: Use `app.py` to interactively predict churn for new customers.

## Getting Started
### 1. Clone the Repository
```
git clone <your-repo-url>
cd <project-folder>
```

### 2. Set Up Python Environment
It is recommended to use a virtual environment:
```
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Prepare Data
- Add your `customer_churn_data.csv` file to the project folder.
- Run the notebook `notebook.ipynb` to explore, clean, and process the data.
- Train models and export the best one as `model.pkl` and the scaler as `scaler.pkl`.

### 5. Run the Streamlit App
```
streamlit run app.py
```
Or, if using a virtual environment:
```
.venv\Scripts\python.exe -m streamlit run app.py
```

## Features
- **Data Exploration**: Visualize and understand churn data.
- **Data Cleaning**: Handle missing values, duplicates, and outliers.
- **Feature Engineering**: Convert categorical variables, scale features.
- **Model Training**: Logistic Regression, KNN, SVM, Decision Tree, Random Forest with hyperparameter tuning.
- **Model Evaluation**: Accuracy, classification report, confusion matrix.
- **Web App**: User-friendly interface for real-time churn prediction.

## Requirements
- Python 3.8+
- See `requirements.txt` for all dependencies

## Usage
- The Streamlit app takes user input for Age, Gender, Tenure, and Monthly Charges, scales the input, and predicts churn using the trained model.
- The notebook provides a full workflow from raw data to model export.

## Notes
- Ensure `scaler.pkl` and `model.pkl` are present in the project directory before running the app.
- Update the code if your data columns or model features differ.

## License
This project is for educational and demonstration purposes. Please adapt and extend for your own use cases.

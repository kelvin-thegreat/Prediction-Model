# 🏠 India House Price Prediction

This is a **Streamlit-based web application** that predicts house prices in India using a trained **Random Forest Regressor** model. Users can input house details such as the number of bedrooms, bathrooms, living area, house condition, and nearby schools to get an estimated price.

---

## Features

- Predict house prices in real-time.
- Simple and interactive web interface built with Streamlit.
- Modern UI with custom CSS styling and dark background.
- Supports key house attributes:
  - Number of Bedrooms
  - Number of Bathrooms
  - Living Area (in sq.ft)
  - Condition of the house
  - Number of Schools Nearby

---

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>


## Create a virtual environment (optional but recommended)

- `python -m venv venv`
- `Activate the virtual environment`

### On Windows:

- `venv\Scripts\activate`

### On macOS/Linux:

- `source venv/bin/activate`
- `Install required dependencies`
- `pip install -r requirements.txt`

### Usage
- Run the Streamlit app:
- streamlit run streamlit_app.py
- The app will open in your default browser.
- Enter the details of the house in the input boxes.
- Click Predict Price to see the estimated house price.

### File Structure

house-price-prediction/
│
├─ house_price_rf_model.pkl     # Trained Random Forest model
├─ streamlit_app.py             # Streamlit app code
├─ requirements.txt            # Python dependencies
└─ README.md                   # Project documentation

## Dependencies

- Python >= 3.8
- pandas
- numpy
- scikit-learn
- streamlit
- joblib

### Install dependencies via:

- `pip install pandas numpy scikit-learn streamlit joblib`

## Model

- The application uses a Random Forest Regressor trained on Indian house data. Make sure the `house_price_rf_model.pkl` file is in the same directory as the `Streamlit app`.

## Screenshots

(Add screenshots of your app here for clarity)

##  License

- This project is open-source and available under the MIT License.


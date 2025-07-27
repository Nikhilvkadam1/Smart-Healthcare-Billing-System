# Smart Healthcare Billing System

A machine learning-powered web application that predicts a patient’s hospital billing amount based on various medical inputs using a trained Random Forest Regressor model.

## Features

- Predicts hospital billing amount based on patient details
- Clean and simple HTML/CSS frontend
- Flask-powered backend
- SQLite database to store predictions
- View all past predictions in a tabular format

## Tech Stack

- Python
- Flask
- Scikit-learn
- HTML/CSS
- SQLite (via SQLAlchemy)

## How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/Nikhilvkadam1/Smart-Healthcare-Billing-System.git
cd Smart-Healthcare-Billing-System
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Application**

```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## Directory Structure

```
Smart-Healthcare-Billing-System/
│
├── app.py                 # Main Flask app
├── model.pkl              # Trained ML model (RandomForestRegressor)
├── scaler.pkl             # Scaler used during preprocessing
├── columns.pkl            # Column structure for one-hot encoding
├── templates/
│   ├── index.html         # Home form
│   └── record.html        # Past predictions display
├── static/
│   └── style.css          # Styling
├── healthcare_dataset.csv # Sample dataset used for training
└── requirements.txt       # Python dependencies
```

## Project Status

✅ Functional and ready for deployment (except MongoDB features, which were removed).

## License

This project is open-source and free to use under the [MIT License](LICENSE).


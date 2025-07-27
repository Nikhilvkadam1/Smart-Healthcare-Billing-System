# Smart Healthcare Billing System 🏥💡

A machine learning-powered web application designed to predict hospital billing costs based on patient data. This system aids both healthcare providers and patients by offering transparent, early-stage cost estimations for hospital services. It uses a trained Random Forest Regressor to analyze factors like age, gender, medical condition, and duration of stay to generate an accurate bill estimate.

This project showcases a complete ML lifecycle: from data preprocessing and model training to deployment via Flask, wrapped in a responsive UI with database-backed CRUD operations.

## 🚀 Key Features

- 🔍 **Smart Bill Prediction**: Estimates hospital charges based on real-world patient inputs.
- 📥 **Dynamic Input Form**: Accepts data like age, gender, condition, length of stay, blood type, etc.
- 🧠 **Trained ML Model**: Built using Random Forest on healthcare billing dataset.
- 💾 **Persistent Storage**: Saves all predictions in an SQLite database using SQLAlchemy.
- 🔄 **CRUD Operations**: Allows users to view, edit, and delete historical billing predictions.
- 🌐 **Responsive Web Interface**: Clean and intuitive UI built using HTML, CSS, and Jinja2 templates.
- ⚡ **Fast & Lightweight**: Runs efficiently on local machines with minimal resources.

## 🧠 Tech Stack

- **Frontend**: HTML5, CSS3, Jinja2 (Flask Templating)
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn (RandomForestRegressor), pandas, NumPy
- **Model Serialization**: `joblib` for saving model, scaler, and column names
- **Database**: SQLite (via SQLAlchemy ORM)
- **Version Control**: Git & GitHub

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


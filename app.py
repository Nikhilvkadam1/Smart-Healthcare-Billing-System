from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'predictions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PatientPrediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bill_amount = db.Column(db.Float, nullable=False)

df = pd.read_csv("healthcare_dataset.csv")
categorical_columns = ['Gender', 'Blood Type', 'Medical Condition', 'Admission Type', 'Insurance Provider', 'Medication', 'Test Results']
df[categorical_columns] = df[categorical_columns].apply(lambda col: col.str.lower())
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])
df['Length of Stay'] = (df['Discharge Date'] - df['Date of Admission']).dt.days
df.drop(['Name', 'Doctor', 'Hospital', 'Room Number', 'Date of Admission', 'Discharge Date'], axis=1, inplace=True)

Q1, Q3 = df['Billing Amount'].quantile([0.25, 0.75])
IQR = Q3 - Q1
df = df[(df['Billing Amount'] >= Q1 - 1.5 * IQR) & (df['Billing Amount'] <= Q3 + 1.5 * IQR)]

df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
X = df_encoded.drop(['Billing Amount'], axis=1)
y = df_encoded['Billing Amount']

scaler = StandardScaler()
X[['Age', 'Length of Stay']] = scaler.fit_transform(X[['Age', 'Length of Stay']])

regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X, y)

feature_columns = X.columns.tolist()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    age = int(request.form['age'])
    gender = request.form['gender'].lower()
    blood = request.form['blood'].lower()
    condition = request.form['condition'].lower()
    admission = request.form['admission'].lower()
    insurance = request.form['insurance'].lower()
    medication = request.form['medication'].lower()
    test = request.form['test'].lower()
    stay = int(request.form['stay'])

    user_input = {
        'Age': age,
        'Gender': gender,
        'Blood Type': blood,
        'Medical Condition': condition,
        'Admission Type': admission,
        'Insurance Provider': insurance,
        'Medication': medication,
        'Test Results': test,
        'Length of Stay': stay
    }

    input_df = pd.DataFrame([user_input])
    input_df = pd.get_dummies(input_df).reindex(columns=feature_columns, fill_value=0)
    input_df[['Age', 'Length of Stay']] = scaler.transform(input_df[['Age', 'Length of Stay']])
    prediction = regressor.predict(input_df)[0]

    record = PatientPrediction(name=name, bill_amount=round(prediction, 2))
    db.session.add(record)
    db.session.commit()

    return render_template("index.html", prediction=f"Patient '{name}', Estimated Bill: ₹{round(prediction)}")

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    prediction = PatientPrediction.query.get_or_404(id)
    if request.method == 'POST':
        prediction.name = request.form['name']
        prediction.bill_amount = float(request.form['bill_amount'])
        db.session.commit()

        return redirect(url_for('records'))
    return render_template("edit.html", prediction=prediction)

@app.route('/delete/<int:id>')
def delete(id):
    prediction = PatientPrediction.query.get_or_404(id)
    db.session.delete(prediction)
    db.session.commit()

    return redirect(url_for('records'))

@app.route('/records')
def records():
    all_predictions = PatientPrediction.query.all()
    return render_template("record.html", predictions=all_predictions)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

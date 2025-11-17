from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/", methods=["Get"])
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "training successfully"

@app.route('/predict', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            # and so on

            data = [fixed_acidity]
            data = np.array(data).reshaoe(1,11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template("results.html", prediction = str(predict))
        except Exception as e:
            raise "something is wrong"

    else:
        return render_template("index.html")
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
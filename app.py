from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

from flask_cors import CORS

application=Flask(__name__)
CORS(application) # Enable CORS for all domains

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('home.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            # Handle both JSON and Form Data
            if request.is_json:
                data_sour = request.json
            else:
                data_sour = request.form

            data=CustomData(
                gender=data_sour.get('gender'),
                race_ethnicity=data_sour.get('ethnicity'),
                parental_level_of_education=data_sour.get('parental_level_of_education'),
                lunch=data_sour.get('lunch'),
                test_preparation_course=data_sour.get('test_preparation_course'),
                reading_score=float(data_sour.get('reading_score')),
                writing_score=float(data_sour.get('writing_score'))
            )
            pred_df=data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            print("after Prediction")
            
            # Return JSON for API calls
            if request.is_json:
                return {"results": results[0]}
            
            return render_template('home.html',results=results[0])
            
        except Exception as e:
             if request.is_json:
                 return {"error": str(e)}, 400
             raise e

@app.route('/predict_api',methods=['POST'])
def predict_api():
    try:
        data_sour = request.json
        data=CustomData(
            gender=data_sour.get('gender'),
            race_ethnicity=data_sour.get('ethnicity'),
            parental_level_of_education=data_sour.get('parental_level_of_education'),
            lunch=data_sour.get('lunch'),
            test_preparation_course=data_sour.get('test_preparation_course'),
            reading_score=float(data_sour.get('reading_score')),
            writing_score=float(data_sour.get('writing_score'))
        )
        pred_df=data.get_data_as_data_frame()
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return {"results": results[0]}
    except Exception as e:
        return {"error": str(e)}, 400

if __name__=="__main__":
    app.run(host="0.0.0.0")        



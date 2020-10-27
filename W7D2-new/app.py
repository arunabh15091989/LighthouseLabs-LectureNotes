from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback
import pickle
import pandas as pd
from joblib import load

# App definition
app = Flask(__name__)
#,template_folder='templates')

# importing models
classifier = load('model.joblib')

#default route
@app.route('/')
def home():
   return render_template('index.html')

#form for user input route
@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [float(x) for x in request.form.values()]
    features_array =  np.array(features)
    features_reshaped = features_array.reshape(1,-1)

    prediction = classifier.predict(features_reshaped)

    output = int(prediction)
    output_text=''
    if output ==1:
        output_text = 'Has CardioVascular Disease'
    else:
        output_text = 'Does not have CardioVascular Disease'

    return render_template('index.html', prediction_text=output_text)

#create api route
@app.route('/predict_api',methods=['POST'])
def make_predict():
    #'age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active'
    data = request.get_json(force=True)
    predict_request = [data['age'],data['gender'],data['height'],data['weight'],data['bp_hi'],data['bp_lo'],data['cholestrol'],data['gluc'],data['smoke'],data['alco'],data['active']]
    predict_request = np.array(predict_request)
    predict_request = predict_request.reshape(1,-1)
    #make Prediction
    y_hat = classifier.predict(predict_request)
    #return our Prediction
    output = [int(y_hat[0])]
    return jsonify(results=output)

if __name__=='__main__':
    app.run(debug=True)

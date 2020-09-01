from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback
import pickle
import pandas as pd


# App definition
app = Flask(__name__)
#,template_folder='templates')

# importing models
with open('./model.pkl', 'rb') as f:
   regressor = pickle.load (f)

with open('./model_columns.pkl', 'rb') as f:
   model_columns = pickle.load (f)


@app.route('/')
def welcome():
   return "Flask App about Boston Housing Price Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       try:
           json_ = request.json
           print(json_)
           query_ = pd.get_dummies(pd.DataFrame(json_))
           query = query_.reindex(columns = model_columns, fill_value= 0)
           prediction = list(regressor.predict(query))

           return jsonify({
               "prediction":str(prediction)
           })

       except:
           return jsonify({
               "trace": traceback.format_exc()
               })


if __name__ == "__main__":
   app.run()

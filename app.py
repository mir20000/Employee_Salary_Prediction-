# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:00:31 2020
@author: my PC
"""

from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def predict():
    iput = [int(x) for x in request.form.values()]
    X_test = [np.array(iput)]
    pred = model.predict(X_test)
    return render_template('index.html',out_put="Employee Salary will be Rs. {}".format(pred))



if __name__=="__main__":
    app.run(debug=True)

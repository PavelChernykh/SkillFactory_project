from numpy.core.arrayprint import FloatingFormat
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes

from flask import Flask, request

import numpy as np

from decimal import *
import pickle

X, y = load_diabetes(return_X_y=True)
X = X[:, 0].reshape(-1, 1) # Берём только один признак
regressor = LinearRegression()
regressor.fit(X,y)
#Обучить модель по примеру и сериализовать её
value_to_predict = np.array([0.04]).reshape(-1, 1)
regressor.predict(value_to_predict)

with open('model.pkl', 'wb') as output:
   	pickle.dump(regressor, output) #Сериализация

def model_predict(value):
        value_to_pr = np.array([value]).reshape(-1, 1)
        return regressor_from_file.predict(value_to_pr)

app = Flask(__name__)

with open('model.pkl', 'rb') as pkl_file:
    	regressor_from_file = pickle.load(pkl_file)#Десериализация

@app.route('/predict')
def predict_func(): 
        value = request.args.get('value')
        prediction = model_predict(Decimal(value))
        return f'the result is {prediction}!'
#функцию, которая будет принимать запрос с числом, отправлять это число в модель и выводить результат на экран

if __name__ == '__main__':
    	app.run('localhost', 5000)
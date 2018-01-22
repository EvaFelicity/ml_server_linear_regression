
from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)


@app.route('/')
def display():
    return "Looks like it works!"


x1_train = []
x2_train_str= []
x2_train = []
y_train = []


@app.route('/learn', methods=['POST'])
def learn():
    data = request.get_json()
    x1_train.append(data['age'])
    if data['species'] not in x2_train_str:
        x2_train_str.append(data['species'])
    x2_train.append(x2_train_str.index(data['species']))
    y_train.append(data['score'])
    return 'ok'


linear = LinearRegression()
X2_dict = None


@app.route('/train', methods=['POST'])
def train():
    x1_train_array = np.array(x1_train)
    x2_train_array = np.array(x2_train)
    x_train_array = np.column_stack((x1_train_array, x2_train_array))
    y_train_array = np.array(y_train)
    linear.fit(x_train_array, y_train_array)
    return 'ok'


@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    x1_test_array = np.array(data['age'])
    x2_test_array = np.array(x2_train_str.index(data['species']))
    x_test_array = np.column_stack((x1_test_array, x2_test_array))
    y_pred = linear.predict(x_test_array)
    print(y_pred)
    return jsonify({'score': y_pred[0]})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', debug=True, port=5000)



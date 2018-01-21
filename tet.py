import requests

requests.post(url="http://localhost:5000/learn", json={"age": 1.1, "species": "cat", "score": 3.1})
requests.post(url="http://localhost:5000/learn", json={"age": 3, "species": "cat", "score": 10})

requests.post(url="http://localhost:5000/learn", json={"age": 1.1, "species": "dog", "score": 5})
requests.post(url="http://localhost:5000/learn", json={"age": 3, "species": "dog", "score": 15})
requests.post(url="http://localhost:5000/train")
r = requests.post(url="http://localhost:5000/predict", json={"age": 4.5, "species": "dog"})

print("prediction is " + r.text)

# from sklearn.linear_model import LinearRegression
# import numpy as np
# linear = LinearRegression()
#
# fit = linear.fit(np.array([[1.1, 1], [3, 1], [1.1, 0], [3, 0]]), np.array([[3.1], [10], [5], [15]]))
# Y_pred = linear.predict(np.array([[4.5, 0]]))
#
#
# print(Y_pred)
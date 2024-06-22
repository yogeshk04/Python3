# Simple linear regresion
# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importing dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Predicting the test test results
y_pred = regression.predict(X_test)

# Visualising the training set results
plt.scatter(X_train, y_train, edgecolors='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Year of experience')
plt.ylabel('Salary')
plt.show()

# Visualisign the test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regression.predict(X_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
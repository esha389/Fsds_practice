import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

dataset = pd.read_csv(r"C:\Users\Dell\Downloads\Salary_Data.csv")

x = dataset.iloc [:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
#we used 80 train 20 test
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

print(regressor) #regressor is ml model which consider linear regression algorithm

print(regressor.get_params())

y_pred = regressor.predict(x_test)
print(y_pred)

comparision = pd.DataFrame({'Actual':y_test, 'prediction':y_pred })
print(comparision)

plt.scatter(x_test, y_test, color='red')
plt.plot(x_train,regressor.predict(x_train), color = 'blue')
plt.title('salary of employee based on experience')
plt.xlabel('experience')
plt.ylabel('salary')
plt.show()

m_slope = regressor.coef_
print(m_slope)

c_intercept = regressor.intercept_
print(c_intercept)
y_12 = (m_slope*12)+c_intercept
print(y_12)

bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)

#STATISTICS
#mean
dataset.mean()
dataset['Salary'].mean()
#median
dataset.median()
dataset['Salary'].median()
#variance

dataset.var()
dataset['Salary'].var()

#standardDeviation

dataset.std()

from scipy.stats import variation

variation(dataset.values)

#correlation: relation btw two variables
dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])

dataset.skew()

#standardError
dataset.sem()

#SSR
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#SSE
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

#SST
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

r_square = 1 - SSR/SST
print(r_square)



# next continue in VS cod
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

import os
print(os.getcwd())
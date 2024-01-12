import pandas as pd
from math import sqrt
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np

df = pd.read_csv('integrated.csv')
X = np.log(df[['Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Rate/100000)']])
y = df["GDP/capita (USD)"] 
RangeofGDP = df["GDP/capita (USD)"].max() - df["GDP/capita (USD)"].min()

# linear regression for actual data
regr = linear_model.LinearRegression().fit(X,y)

print("Feature Name: " + str(regr.feature_names_in_))
print("Intercept: " + str(regr.intercept_))
print("Coefficients: " + str(regr.coef_))

prediction = regr.predict(X)
inr2score = metrics.r2_score(y, prediction)
print("In-sample R2 value: ", inr2score)
inrmse = sqrt(metrics.mean_squared_error(y , prediction))
print("In sample RMSE: ", inrmse)
innorm = sqrt(metrics.mean_squared_error(y, prediction))/RangeofGDP
print("In-sample Normalized Deviation: ", innorm)

print("\n")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
# linear regression for train data
regr = linear_model.LinearRegression().fit(X_train,y_train)

# Use the model to predict y from X_test
y_pred = regr.predict(X_test)
# R-squared score: 1 is perfect prediction
r2score =  metrics.r2_score(y_test, y_pred)
print('Out-of-sample R2 value', r2score)
# Root mean squared error
rmse = sqrt(metrics.mean_squared_error(y_test, y_pred))
print('Out-of-sample RMSE:', rmse)
# Normalized Deviation
NDev = rmse/RangeofGDP
print('Out-of-sample Normalized Deviation: ', NDev)

# to draw a table
f = open("Stage3summary.csv", "w")
f.write("Logged Model, R2, RMSE, Norm RMSE\n")
f.write("In-Sample," + str(round(inr2score,2)) + "," + str(round(inrmse,2)) + "," + str(round(innorm,2)) +"\n")
f.write("Out-of-Sample," + str(round(r2score,2))+ "," + str(round(rmse,2)) + "," + str(round(NDev,2)) +"\n")
f.close()
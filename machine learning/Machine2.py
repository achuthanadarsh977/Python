#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# In[6]:


data = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Documents\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 2 - Regression\Section 4 - Simple Linear Regression\Python\Salary_Data.csv')
print(data)


# In[7]:


# X = data.iloc[:,:-1].values
# y = data.iloc[:,-1].values
# X_train ,  X_test , y_train , y_test = train_test_split(X,y,test_size = 1/3 ,random_state = 0)
# regressor = LinearRegression()
# regressor.fit(X_train,y_train)
# y_pred = regressor.predict(X_test)

# plt.scatter(X_train , y_train , color = "red")
# plt.plot(X_train, regressor.predict(X_train), color = 'blue')
# plt.title("Salary vs Experience(Training Set)")
# plt.xlabel("Salary")
# plt.ylabel("Experience")
# plt.show()


# In[8]:


data1 = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Documents\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 2 - Regression\Section 5 - Multiple Linear Regression\Python\50_Startups.csv')
print(data1)


# In[20]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


X = data1.iloc[:, :-1].values
y = data1.iloc[:, -1].values
print(X)

# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[26]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

data3 = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Documents\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 2 - Regression\Section 6 - Polynomial Regression\Python\Position_Salaries.csv')

X = data3.iloc[:, 1:2].values   # Level column only (skip Position text)
y = data3.iloc[:, -1].values   

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"R² Score : {r2_score(y_test, y_pred) * 100:.2f}%")
print(f"Predicted: {y_pred}")
print(f"Actual   : {y_test}")


# In[ ]:





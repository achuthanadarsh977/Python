#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier


# In[33]:


read = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Documents\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Python\Data.csv')
print(read)


# In[34]:


print(read.describe())

print(read.head())


# In[5]:


print(read.tail())


# In[7]:


print(read.shape)


# In[8]:


print(read.values)


# In[9]:


print(read.isnull())


# In[11]:


print(read['Country'])


# In[ ]:





# In[26]:


df = read['Country']
d1 = pd.DataFrame(df)
encoded = pd.get_dummies(d1 , columns = ['Country'] , drop_first = True )
print(d1)
print(encoded)


# In[27]:


print(read)


# In[35]:


d2 = pd.DataFrame(read['Age'])
encoded1 = pd.get_dummies(d2 , columns = ['Age'] , drop_first = 1)
print(encoded1)

from sklearn.tree import DecisionTreeClassifier
X = read.drop(columns = 'Purchased')
y = read['Purchased']
model = DecisionTreeClassifier()
model.fit(X,y)
print(model)
# In[36]:


print(read)


# In[39]:


X = read.drop(columns = 'Purchased')
print(X)


# In[41]:


a = read.iloc[:,:-1].values
b = read.iloc[:,-1].values
print(a)
print(b)


# In[45]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
deaf = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Documents\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 2 - Regression\Section 4 - Simple Linear Regression\Python\Salary_Data.csv')
X = deaf.iloc[:,:-1].values
y = deaf.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[ ]:





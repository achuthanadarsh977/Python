#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np

x = np.array([1,2,3,4,5])
print(f'Mean:{np.mean(x)}')
print(f'Median:{np.median(x)}')
print(f'Variance:{np.var(x)}')
print(f'Standard Deviation:{np.std(x)}')


# In[51]:


age = [12,13,45,67,23,34,45,19,56]
x = np.percentile(age,45)
print(x)


# In[52]:


import matplotlib.pyplot as plt
y = np.random.uniform(0.0,4.0,250)
plt.hist(x,5)
plt.show()


# In[53]:


z = np.random.uniform(0.0,6.8,350)
plt.bar(z,6)
plt.show()


# In[12]:


import pandas as pd

data = pd.read_csv(r'C:\Users\SriniAchuthan\OneDrive\Desktop\Machine-Learning-A-Z-Codes-Datasets\Machine Learning A-Z\Part 1 - Data Preprocessing\Section 2 -------------------- Part 1 - Data Preprocessing --------------------\Python\Data.csv')
print(data)


# In[17]:


p = data['Salary']
q = data['Age']
plt.scatter(p,q)
plt.xlabel('Salary')
plt.ylabel('Age')
plt.title('Salary vs Age')
plt.show()


# In[28]:


from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p_value, std_err = stats.linregress(x, y)

def myfunc(z):
  return slope * z + intercept

speed = myfunc(10)

print(speed)


plt.title("X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(x,y,color="red")
plt.show()


# In[29]:


data2 = pd.read_csv(r'C:\Users\SriniAchuthan\Downloads\Car - Sheet1.csv')
print(data2)


# In[35]:


from scipy import stats

a = np.array(data2['Volume'])
b = np.array(data2['Weight'])

slope, intercept, r, p_value, std_err = stats.linregress(a, b)

def myfunc(c):
    return slope*c + intercept

special = myfunc(1000)

print(special)


# In[37]:


s = np.array(data2['CO2'])
e = np.array(data2['Volume'])

slope,intercept,r,p_value,std_err = stats.linregress(s,e)

def myfunc(t):
    return slope*t + intercept

print(myfunc(1200))


# In[45]:


from sklearn import linear_model

X = data2[['Weight', 'Volume']]
y = data2['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)


# In[55]:


from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x,y,3))
speed = mymodel(17)
print(speed)


# In[ ]:





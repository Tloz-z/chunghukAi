#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pylab as plt
from sklearn import linear_model as lm

reg = lm.LinearRegression()

X = [[174] , [152] , [138] , [128] , [186]]
y = [71 , 55 , 46 , 38 , 88]
reg.fit(X , y)

print("2016038012_고우영")
print(reg.predict([[165]]))

plt.scatter(X , y , color='black')

y_pred = reg.predict(X)

plt.plot(X , y_pred , color='blue' , linewidth=3)
plt.show()


# In[ ]:





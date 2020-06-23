#!/usr/bin/env python
# coding: utf-8

# In[15]:


from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()

df = pd.DataFrame(data=iris.data , columns=iris.feature_names)
df['target'] = iris.target

df['target'] = df['target'].map({0: "setosa" , 1: "versicolor" , 2: "virginica"})

x_data = df.iloc[: , :-1]
y_data = df.iloc[: , [-1]]

sns.pairplot(df , x_vars=["sepal length (cm)"] , y_vars=["sepal width (cm)"] , hue = "target" , height = 5)

from sklearn.model_selection import train_test_split
X_train, X_test , y_train , y_test = train_test_split(iris['data'], iris['target'], random_state=0)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train , y_train)

y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test , y_pred)
print("2016038012_고우영")
print(scores)

classes = {0 : 'setosa' , 1:'versicolor' , 2:'virginica'}
x_new = [[3,4,5,2] , [5,4,2,2]]
y_predict = knn.predict(x_new)

print(classes[y_predict[0]])
print(classes[y_predict[1]])


# In[10]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

iris = datasets.load_iris()

X = iris.data[: , :2]
y = iris.target

plt.scatter(X[:,0], X[:,1] , c=y , cmap='gist_rainbow')
plt.xlabel('Sepal Length' , fontsize=18)
plt.ylabel('Sepal Width' , fontsize=18)

km = KMeans(n_clusters = 3 , n_jobs = 4 , random_state=21)
km.fit(X)

centers = km.cluster_centers_
print("2016038012_고우영")
print(centers)


# In[ ]:





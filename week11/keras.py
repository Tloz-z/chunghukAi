#!/usr/bin/env python
# coding: utf-8

# In[8]:


import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

sns.set(style="ticks" , color_codes=True)
iris = sns.load_dataset("iris")

X = iris.iloc[:, 0:4].values
y = iris.iloc[: , 4].values

encoder = LabelEncoder()
y1 = encoder.fit_transform(y)
Y = pd.get_dummies(y1).values

X_train, X_test , y_train , y_test = train_test_split(X, Y, test_size=0.2 , random_state=1)

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

model = Sequential()

model.add(Dense(64, input_shape=(4,), activation='relu'))
model.add(Dense(64,activation='relu'))
model.add(Dense(3,activation='softmax'))

model.compile(loss = 'categorical_crossentropy' , optimizer = 'Adam' , metrics = ['accuracy'])

hist = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100)

import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.legend(['loss','val_loss','accuracy','val_accuracy'])
plt.grid()
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


# In[39]:


dataset = pd.read_csv('alert_data.csv')


# In[40]:


dataset = pd.get_dummies(dataset, columns=["Purpose/ Type of Work", "Day of the week", "Time of day", "Weather Condition"])


# In[41]:


X = dataset.drop(columns=["User Id", "Target Alert"])
y = dataset["Target Alert"]


# In[42]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[43]:


rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)


# In[44]:


predictions = rf_classifier.predict(X_test)


# In[45]:


accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))


# In[52]:


input_data = {
    "Session Duration": [83],
    "Purpose/ Type of Work": ['grocery shopping'],
    "Alert Threshold for the work": [20],
    "Day of the week": ['monday'],
    "Time of day": ['night'],
    "Weather Condition": ['rainy'],
    "Deviation": [63],
    "Limit": [22]
}
input_df = pd.DataFrame(input_data)
input_df = pd.get_dummies(input_df, columns=["Purpose/ Type of Work", "Day of the week", "Time of day", "Weather Condition"])
missing_cols = set(X.columns) - set(input_df.columns)
for col in missing_cols:
    input_df[col] = 0
input_df = input_df[X.columns]
input_array = input_df.values
prediction = rf_classifier.predict(input_array)
if prediction == 1:
    print("Generate alert")
else:
    print("No alert")


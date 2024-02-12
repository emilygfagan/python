#!/usr/bin/env python
# coding: utf-8

# ### University Data Practice

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


uni = pd.read_csv("Practice_2_Raw_Data (1).csv")


# Data Insights: 
# - Number rows / columns
# - Values
# - Data Types
# - Missing Values

# In[3]:


# shape displays number of rows and columns in dataset
uni.shape


# In[4]:


# head displays top 5 observations of dataset
uni.head()


# In[5]:


# info displays datatype and information
uni.info()


# In[6]:


"""
Displaying missing values with isnull and sum
to display number of null values
""" 
uni.isnull().sum()


# In[7]:


# percentage of null values in each column
(uni.isnull().sum()/(len(uni)))*100


# In[8]:


uni.head(20)


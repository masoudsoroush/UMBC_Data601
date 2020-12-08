#!/usr/bin/env python
# coding: utf-8

# # Functions

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[16]:


# N_largest finds the items (i.e. rows) in a dafaframe corresponding to the n largest values of feature 'feature'

def N_largest (df,n,feature):
    return df.nlargest(n,feature)[list(df.columns[:4])+[feature]]


# In[17]:


# N_smallest finds the items (i.e. rows) in a dafaframe corresponding to the n smallest values of feature 'feature'

def N_smallest (df,n,feature):
    return df.nsmallest(n,feature)[list(df.columns[:4])+[feature]]


# In[18]:


# number_of_greater_a finds the number of items in a dataframe with feature 'feature'>a

def number_of_greater_a (df,feature,a):
    return len(df[df[feature]>a])


# In[19]:


# number_of_greater_a finds the number of items in a dataframe with feature 'feature'<a

def number_of_smaller_a (df,feature,a):
    return len(df[df[feature]<a])


# In[20]:


# n food items in the category 'FoodGroup' with lowest level of 'feature'

def N_nonzero_smallest(df,n,feature,food_group):
    aux_df = pd.DataFrame()
    aux_df = df[(df[feature] != 0) & (df['FoodGroup'] == food_group)]
    return N_smallest(aux_df,n,feature)


# In[21]:


# remove_unit removes the units of all features (used in the dataframes in the project)

def remove_unit (str_list):
    aux_list=[]
    for element in str_list:
        aux_list.append(element.split('_')[0])
    return aux_list


# In[22]:


# The 'Lin_Reg' function finds the least square regression line for the two lists 'Lone' and 'Ltwo'. Parameter 'c'
# specifies the color of the regression line.

def Lin_Reg(Lone,Ltwo,c):
    a=np.polyfit(Lone,Ltwo,1)
    y=lambda x: a[0]*x+a[1]
    b=np.linspace(min(Lone),max(Lone),200)
    return plt.plot(b,y(b),color=c)


# In[ ]:





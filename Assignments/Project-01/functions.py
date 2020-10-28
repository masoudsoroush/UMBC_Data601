#!/usr/bin/env python
# coding: utf-8

# # Functions Used in Project-1

# In[1]:


def dropzero(x):
    while x[0]=='0':
        x=x.replace(x[0],'',1)
    return x


# In[2]:


def Date_Conversion(x):
    month_length=[31,28,31,30,31,30,31,31,30,31,30,31]
    year=int(dropzero(x.split('-')[0]))
    month=int(dropzero(x.split('-')[1]))
    day=int(dropzero(x.split('-')[2]))
    if month>1:
        y=sum(month_length[:month-1])+day
    elif month==1:
        y=day
    else:
        y='Date is not appropriately specified!'
# Taking into account the leap years:    
#    if year%4==0 and month>2:
#        y+=1
    return y


# In[3]:


# The 'Outlier_Elimination' function replaces the outliers of the list x by the bound. UpLow indicates whether 
# the given bound is an upper or a lower bound.

def Outlier_Elimination(x,bound,UpLow):
    if UpLow=='U':
        if x>bound:
            return bound
        else:
            return x
    elif UpLow=='L':
        if x<bound:
            return bound
        else:
            return x
    else: 
        print('It has not been specified properly whether the bound is a lower bound or an upper bound!')


# In[1]:


# The 'precipitation type' specifies the rain class according to https://climate.ncsu.edu/edu/PrecipTypes.

def precipitation_type(x):
    y=0
    if x==0:
        y=0                        # No rain 
    elif x>=0.01 and x<0.1:
        y=1                        # Light rain
    elif x>=0.1 and x<=0.3:
        y=2                        # Moderate rain
    elif x>0.3:
        y=3                        # Heavy rain
    else:
        y='Precipitation rate has not been specified properly!'
    return y


# In[ ]:





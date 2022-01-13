#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np 
import matplotlib as plot


# In[2]:


T20=pd.read_csv('D:\\AIDTM\\trimester 2\\PYTHON FOR MANAGERS\\data set\\icc t20 world cup 2021.csv')


# In[4]:


T20


# In[5]:


T20.isna().sum()


# In[255]:


T20PIVOT=T20.pivot_table(T20,index=["Toss_descision"],columns=["venue","time"],values="target_achieved",aggfunc="count")


# In[244]:


T20PIVOT


# In[23]:


T20FINAL=T20PIVOT.Winner


# In[24]:


T20FINAL


# In[ ]:





# In[262]:


import matplotlib.pyplot as plot
T20FINAL.plot.barh(figsize=(10,9),title="T20 ICC WC 2021 Toss Decision")
plot.ylabel("Toss Decision")
plot.xlabel("Number of Teams")


# In[30]:


T20PIVOTW=T20.pivot_table(T20,index=["venue","time","Toss_descision"],aggfunc=sum)


# In[33]:


T20wicket=T20PIVOTW.most_individual_wickets


# In[263]:


T20wicket.plot.barh(figsize=(10,9),title="Highest wicket taken")
plot.xlabel("No. of wickets")


# In[48]:


T20maxtarget=T20PIVOT.target


# In[49]:


T20maxtarget


# In[264]:


T20maxtarget.plot.barh(figsize=(10,9),title="Highest Target Given")
plot.xlabel("Runs")


# In[55]:


T20PIVOTachieved=T20PIVOT.target_achieved


# In[56]:


T20PIVOTachieved


# In[265]:


T20PIVOTachieved.plot.barh(figsize=(10,9),title="Target achieved")
plot.xlabel("No. of targets achieved")


# In[74]:


T20target=T20PIVOT.target


# In[252]:


T20target.plot.bar(figsize=(10,9),title="Avg. Target")
plot.ylabel("Runs")


# In[128]:


T20PIVOT


# In[117]:


T20TEAMeco


# In[253]:


T20TEAMeco.plot.bar(figsize=(10,9),title="avg economy")
plot.ylabel("Runs")


# In[254]:


T20mostindividualwicket.plot.bar(figsize=(10,9),title="Most individual wickets")
plot.ylabel("Wickets")


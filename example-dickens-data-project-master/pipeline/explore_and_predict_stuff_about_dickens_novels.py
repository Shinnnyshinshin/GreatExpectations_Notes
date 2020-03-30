import pandas as pd
import statsmodels.formula.api as sm

import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("../data/notable_works_by_charles_dickens/notable_works_by_charles_dickens.csv")


# In[3]:


df.head()


# In[4]:


df["Year completed"].value_counts().sort_index()


# In[5]:


df.Type.value_counts()


# In[6]:


df["title_len"] = df.Title.map(len)
df["year"] = df["Year completed"]
df["is_novel"] = df.Type == "Novel"


# In[7]:


df.head()


# In[8]:


df.is_novel.value_counts()


# In[9]:


df.title_len.hist()


# In[10]:


plt.scatter(df.year, df.title_len)


# In[14]:


result = sm.ols(formula="title_len ~ year", data=df).fit()
result.summary()


# In[19]:


result.rsquared


# In[20]:


result.params["year"]


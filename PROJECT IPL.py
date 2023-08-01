#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis on IPL 2008-2022 dataset

# ### importing all the required libraries

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# *loading the dataset of all IPL matches*

# In[2]:


ipl = pd.read_csv('IPL_Matches_2008_2022.csv')                # ipl variable name stands for overall data of all the matches 
balls = pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')         # balls variable name stands for the data of ball by ball records


# *showing first five records of the overall matches*

# In[3]:


ipl.head()


# *showing last five records of the overall matches*

# In[4]:


ipl.tail()


# *showing first five records of the ball by ball data.* 

# In[7]:


balls.head()


# *showing last five records of the ball by ball data*

# In[8]:


balls.tail()


# In[17]:


df = ipl.sort_values(by = ['ID'])
df.head()


# In[11]:


balls = balls.sort_values(by = ['ID'])
balls.head()


# In[12]:


ipl.columns


# In[13]:


balls.columns


# *the number of rows and columns in the dataset of overall matches*

# In[14]:


ipl.shape


# *the number of rows and columns in the dataset of ball by ball records*

# In[16]:


balls.shape


# In[18]:


edadf = df.merge(balls, on = 'ID')
edadf.columns


# In[20]:


edadf.Season.unique()


# *some Season values are wrongly entered so we will replace these with the correct ones* 

# In[21]:


edadf.Season = edadf.Season.replace(to_replace='2007/08', value='2008')
edadf.Season = edadf.Season.replace(to_replace='2009/10', value='2010')
edadf.Season = edadf.Season.replace(to_replace='2020/21', value='2020')


# In[22]:


edadf.Season.unique()


# *repeat the same thing for the ipl dataset as well*

# In[23]:


ipl.Season = ipl.Season.replace(to_replace='2007/08', value='2008')
ipl.Season = ipl.Season.replace(to_replace='2009/10', value='2010')
ipl.Season = ipl.Season.replace(to_replace='2020/21', value='2020')


# In[24]:


ipl.Season.unique()


# In[25]:


edadf.Venue.unique()


# In[26]:


edadf.City.unique()


# In[27]:


edadf.BattingTeam.unique()


# In[28]:


edadf.BattingTeam = edadf.BattingTeam.replace(to_replace = 'Rising Pune Supergiant', value = 'Rising Pune Supergiants')
edadf.BattingTeam = edadf.BattingTeam.replace(to_replace = 'Delhi Daredevils', value = 'Delhi Capitals')
edadf.BattingTeam = edadf.BattingTeam.replace(to_replace = 'Deccan Chargers', value = 'Sunrisers Hyderabad')
edadf.BattingTeam = edadf.BattingTeam.replace(to_replace = 'Kings XI Punjab', value = 'Punjab Kings')


# In[29]:


edadf.BattingTeam.unique()


# In[30]:


edadf.Team1.unique()


# In[31]:


edadf.Team1 = edadf.Team1.replace(to_replace = 'Rising Pune Supergiant', value = 'Rising Pune Supergiants')
edadf.Team1 = edadf.Team1.replace(to_replace = 'Delhi Daredevils', value = 'Delhi Capitals')
edadf.Team1 = edadf.Team1.replace(to_replace = 'Deccan Chargers', value = 'Sunrisers Hyderabad')
edadf.Team1 = edadf.Team1.replace(to_replace = 'Kings XI Punjab', value = 'Punjab Kings')


# In[32]:


edadf.Team1.unique()


# In[33]:


edadf.Team2.unique()


# In[34]:


edadf.Team2 = edadf.Team2.replace(to_replace = 'Rising Pune Supergiant', value = 'Rising Pune Supergiants')
edadf.Team2 = edadf.Team2.replace(to_replace = 'Delhi Daredevils', value = 'Delhi Capitals')
edadf.Team2 = edadf.Team2.replace(to_replace = 'Deccan Chargers', value = 'Sunrisers Hyderabad')
edadf.Team2 = edadf.Team2.replace(to_replace = 'Kings XI Punjab', value = 'Punjab Kings')


# In[35]:


edadf.Team2.unique()


# In[36]:


edadf.WinningTeam.unique()


# In[37]:


edadf.WinningTeam = edadf.WinningTeam.replace(to_replace = 'Rising Pune Supergiant', value = 'Rising Pune Supergiants')
edadf.WinningTeam = edadf.WinningTeam.replace(to_replace = 'Delhi Daredevils', value = 'Delhi Capitals')
edadf.WinningTeam = edadf.WinningTeam.replace(to_replace = 'Deccan Chargers', value = 'Sunrisers Hyderabad')
edadf.WinningTeam = edadf.WinningTeam.replace(to_replace = 'Kings XI Punjab', value = 'Punjab Kings')


# In[38]:


edadf.WinningTeam.unique()


# ### General analysis of IPL matches

# In[ ]:





# In[6]:


ipl.info()


# ## Ongoing...

# In[ ]:





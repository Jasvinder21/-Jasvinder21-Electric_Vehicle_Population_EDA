#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv(r"C:\Users\dell\OneDrive\Desktop\Electric_Vehicle_Population_Data.csv")


# In[3]:


df.head()


# ## Data Cleaning

# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.isnull().sum()


# In[7]:


df.dropna(axis=0,inplace=True)


# In[8]:


df.duplicated().sum()


# ## EDA and Visualization

# In[9]:


df['Electric Vehicle Type'].value_counts().plot(kind='bar')
plt.title ('Count of Electric Vehicles Types')
plt.xticks(rotation=45)
#plt.tight_layout()
plt.show()


# In[10]:


#Top 20 Electric Vehicle Makes by Number of Electric Vehicels.
ev_counts_by_make=df['Make'].value_counts().nlargest(10)


# In[11]:


sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(x=ev_counts_by_make.values,y=ev_counts_by_make.index,palette="viridis")
plt.title('Top 10 Electric Vehicle Makes by Number of Electric Vehicles',fontsize=12)
plt.xlabel('Number of Vehicles',fontsize=10)
plt.ylabel('Make',fontsize=10)
plt.show()

# Tesla is the top makes leading the electric vehicle market,followed by Nissan, and Chevrolet indicating Tesla is the most popular than any other brand.
# In[12]:


#EV Adoption Over Time

#sns.set_style("whitegrid")
#ev_adoption_over_time=df['Model Year'].value_counts().sort_index()
#plt.figure(figsize=(14,7))
#sns.lineplot(x=ev_adoption_over_time.index,y=ev_adoption_over_time.values, marker='o',color='Purple')
#plt.title('EV Adoption Over Time',fontsize=18)
#plt.xlabel('Model Year',fontsize=14)
#plt.ylabel('Number of EV Registrations',fontsize=14)
#plt.show()

yearly_counts= df.groupby('Model Year').size().reset_index(name='Electric Vehicle Count')

plt.figure(figsize=(10,6))
plt.plot(yearly_counts['Model Year'],yearly_counts['Electric Vehicle Count'],marker='o',color='Purple')
plt.title('Trend in Electric Vehicle Manufacturing Over Time')
plt.xlabel('Model Year')
plt.ylabel('Electric Vehicle Count')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[13]:


#it started to increase in early 2010s, which accelerates further into the 2020.The recent years showing an exponential growth in EV adoption, which means it is becoming more popular.


# In[14]:


#Top 20 Counties by Electric Vehicle Counts
ev_count_distribution=df.groupby('County')['VIN (1-10)'].count().reset_index().sort_values(by='VIN (1-10)',ascending=False)
top_ev_counties = ev_count_distribution.head(20)


# In[15]:


plt.figure(figsize=(10,8))
sns.barplot(x='VIN (1-10)', y= 'County', data = top_ev_counties,palette='viridis')

#plt.bar(top_ev_counties['County'], top_ev_counties['VIN (1-10)'], color='skyblue')
plt.title('Top 20 Counties by Electric Vehicle Counts',fontsize=18)
plt.xlabel('Number of Electric Vehicles',fontsize=12)
plt.ylabel('County',fontsize =12)
plt.tight_layout()
plt.show()

The visualization highlights King County as the leading region in electric vehicle adoption, followed by others like Snohomish and Pierce counties.
# In[16]:


plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Model Year', y='Electric Range', alpha=0.6)

plt.title('Improvement in Electric Range of Vehicles Over the Years')
plt.xlabel('Model Year')
plt.ylabel('Electric Range (miles)')

#sns.regplot(data=df, x='Model Year', y='Electric Range', scatter=False, color='Purple')

plt.show()


# In[24]:


# Filtering out rows where Base MSRP is zero or high
filtered_df = df[(df['Base MSRP'] > 0) & (df['Base MSRP'] < 200000)]

sns.set_style("darkgrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_df, x='Model Year', y='Base MSRP', palette="viridis")
plt.title('Distribution of Electric Vehicle Prices Over the Years', fontsize=16)
plt.xlabel('Model Year', fontsize=14)
plt.ylabel('Base MSRP ($)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#In 2008 to 2011 the prices where very high compare to prices now.
# In[18]:


top_makes = filtered_df['Make'].value_counts().nlargest(10).index
filtered_top_makes_df = filtered_df[filtered_df['Make'].isin(top_makes)]


# In[22]:


plt.figure(figsize=(10,6))
sns.barplot(data=filtered_top_makes_df, x='Make', y='Base MSRP', palette="coolwarm")
plt.title('Distribution of Electric Vehicle Prices by Make (Top 10 Makes)', fontsize=16)
plt.xlabel('Make', fontsize=14)
plt.ylabel('Base MSRP ($)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

The boxplot reveals a significant variation in the Base MSRP among the top 10 EV makes, Porsche as it is very popular has price range between 80000 to 180000. Fisker has the second highest price
# In[20]:


district_counts = df.groupby('Legislative District')['DOL Vehicle ID'].count().reset_index()

district_counts_sorted = district_counts.sort_values(by='DOL Vehicle ID', ascending=False)


# In[23]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Legislative District', y='DOL Vehicle ID', data=district_counts_sorted,
            palette='coolwarm')
plt.title('Electric Vehicles by Legislative District')
plt.xlabel('Legislative District')
plt.ylabel('Number of Electric Vehicles')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

The visualization highlights the disparity in electric vehicle (EV) adoption across legislative districts, with Districts 41, 45, and 48 leading by a significant margin.
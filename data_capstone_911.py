import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = 'Py_DS_ML_Bootcamp-master\\Refactored_Py_DS_ML_Bootcamp-master\\10-Data-Capstone-Projects\\911.csv'
df = pd.read_csv(file_name)

df.info()
print(df.head())

#** What are the top 5 zipcodes for 911 calls? **

print(df['zip'].value_counts().head(5))

#** What are the top 5 townships (twp) for 911 calls? **

print(df['twp'].value_counts().head(5))

#** Take a look at the 'title' column, how many unique title codes are there?

print(df['title'].nunique())

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].value_counts())
sns.countplot(x='Reason', data=df)
plt.show()

print(type(df['timeStamp'].iloc[0]))
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

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
sns.countplot(x='Reason', data=df, palette='coolwarm')

print(type(df['timeStamp'].iloc[0]))
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',
        1:'Tue',
        2:'Wed',
        3:'Thu',
        4:'Fri',
        5:'Sat',
        6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

sns.set_style('whitegrid')
sns.countplot(x='Day of Week', hue='Reason', data=df, palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

sns.countplot(x='Month', hue='Reason', data=df, palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

byMonth = df.groupby('Month').count()

sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())

df['Date']=df['timeStamp'].apply(lambda t:t.date())

byDate = df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()

dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
dayHour.head()

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')

sns.clustermap(dayHour, cmap='viridis')

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()
dayMonth.head()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')



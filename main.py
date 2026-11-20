import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:\Users\RISHABH\Downloads\archive (15).zip')
df.head()
df.info()
df.isnull().sum()
df.duplicated().sum()
df.describe()
math_80 = df[df['Math_Score']>80]
science_80 = df[df['Science_Score']>80]
English_80 = df[df['English_Score']>80]
sns.scatterplot(x=df['Study_Hours_Per_Day'],y=df['Final_Percentage'],data=df,hue=df['Pass_Fail'],legend='full')
g = sns.PairGrid(df)
g.map_lower(sns.histplot)
g.map_upper(sns.kdeplot)
df.head()
df['score_improvement'] = df['Final_Percentage'] - df['Previous_Year_Score']
df.head()
df.groupby('Gender')[['Math_Score','English_Score','Science_Score']].mean()
df.groupby('Parental_Education')[['Math_Score','English_Score','Science_Score']].mean()
df.groupby('Internet_Access')[['Math_Score','English_Score','Science_Score']].mean()
df.groupby('Extracurricular_Activities')[['Math_Score','English_Score','Science_Score']].mean()
sns.heatmap(df.corr(numeric_only=True),annot=True,robust=True)
sns.boxplot(x=df['Parental_Education'],y=df['Final_Percentage'],data=df)
sns.countplot(df['Pass_Fail'])
sns.countplot(df['Performance_Level'])
sns.barplot(x=df['Final_Percentage'],y=df['Internet_Access'])
sns.histplot(df['Final_Percentage'])
def get_grade(p):
    if p>=90:
        return 'A+'
    elif p>=80:
        return 'A'
    elif p >=70:
        return 'B'
    elif p>=60:
        return 'C'
    elif p>=50:
        return 'D'
    else:
        return 'F'
df['Grade'] = df['Final_Percentage'].apply(get_grade)
df.head()

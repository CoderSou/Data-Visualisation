# Import necessary libraries
import sqlite3 
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# Connect to sql database
con=sqlite3.connect("/content/drive/MyDrive/ca682_dataset/switrs.sqlite")
cur=con.cursor()

# Querying with SQL and storing as a pandas dataframe and Combining tables based on case_id
df1 = pd.read_sql_query("SELECT case_ids.case_id,collisions.killed_victims, collisions.injured_victims, collisions.weather_1, collisions.collision_date FROM case_ids, collisions WHERE case_ids.case_id = collisions.case_id", con)
print(len(df1))

# Storing a copy of the original dataframe
df_copy=df1.copy()

# Cleaning the data for any NULL values
null_cols=df1.columns[df1.isnull().any()]
print(null_cols)

# Printing to check the NULL values
print(null_cols);print(df1[df1['killed_victims'].isnull()][null_cols]);print(df1[df1['injured_victims'].isnull()][null_cols]);print(df1[df1['weather_1'].isnull()][null_cols])

# Getting the number of null values 
print(df1.isna().sum()); print(df1.isna().sum().sum())

#Dropping rows having any NULL value
drop_null = df1.dropna(axis=0, how='any')
print(len(drop_null));

# Checking for any duplicate rows
print(len(drop_null[drop_null.duplicated()]))

# Checking for Outlier
drop_null.boxplot(column=['killed_victims','injured_victims'])

# Separating the date, month, and year into differnt columns
drop_null['collision_date']=pd.to_datetime(drop_null['collision_date'])

# Making those columns
drop_null['year'] = drop_null['collision_date'].dt.year
drop_null['month'] = drop_null['collision_date'].dt.month
drop_null['day'] = drop_null['collision_date'].dt.day
print(drop_null['year'].max());print(drop_null['month'].max());print(drop_null['day'].max())
print(drop_null.columns)

# Storing as a csv file
drop_null.to_csv("/content/drive/MyDrive/ca682_dataset/out4.csv")

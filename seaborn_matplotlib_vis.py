# Import necessary libraries
import sqlite3 
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to database
con=sqlite3.connect("/content/drive/MyDrive/ca682_dataset/switrs.sqlite")
cur=con.cursor()


# Querying with SQL and storing as a pandas dataframe. Additionally, rejecting columns having Nulls in them
df2 = pd.read_sql_query("SELECT case_ids.case_id,collisions.killed_victims, collisions.injured_victims, collisions.lighting FROM case_ids,collisions WHERE case_ids.case_id = collisions.case_id AND (collisions.killed_victims IS NOT NULL AND collisions.injured_victims IS NOT NULL AND collisions.lighting IS NOT NULL)", con)
print(len(df2))
print(df2.isna().sum())

# Storing a copy of the original dataframe
df_copy_2=df2.copy()

# Checking for any duplicate rows
print(len(df2[df2.duplicated()]))

# Storing as a csv file
df2.to_csv("/content/drive/MyDrive/ca682_dataset/out_5.csv")

# Get unique values in the lighting column
val1=df2['lighting'].unique()
# Get the count for each category
cou1=df2['lighting'].value_counts()

# Set the theme for the plot
sns.set_theme(style="white", font='Arial')
# Condition for green colored bar
colors=['grey' if (x < max(cou1)) else 'green' for x in cou1]
# Make a bar plot with the provided 2 colors
ax = sns.barplot(x=cou1,y=val1, palette=colors)
sns.despine() # Removing the borders
#Give names to the plot and axis with their fontsizes
plt.title('Collisions in California \n Effect of Lighting conditions', fontsize = 15, weight='bold')
plt.xlabel('Number of Collisions', fontsize=12)

# Save the figure
plt.savefig('/content/drive/MyDrive/ca682_dataset/plot3.jpg', dpi=100, bbox_inches='tight')
plt.show()



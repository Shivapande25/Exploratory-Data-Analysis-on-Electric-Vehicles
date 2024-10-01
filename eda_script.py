

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

"""**Reading the dataset in CSV format**"""

dataset2 = "https://raw.githubusercontent.com/arifikmal/EVCarAnalysis/main/evdataset.csv"
dataset=pd.read_csv(dataset2)

"""**Preprocessing and Data Cleaning**"""

#Showing the initial dataset
dataset

#Dropping the columns which are not required
dataset = dataset.drop(columns=['link','City - Cold Weather','Highway - Cold Weather','City - Mild Weather','Highway - Mild Weather','Fastcharge Speed'])

#Renaming the columns for better understanding
dataset.rename(columns = {'Combined - Cold Weather' : 'Electric Range(Cold Whether)', 'Combined - Mild Weather' : 'Electric Range(Mild Whether)'}, inplace = True)

#Renaming the columns for better understanding
dataset.rename(columns = {'Acceleration 0 - 100 km/h' : 'Acceleration Time', 'Drive' : 'Drive Type', 'Seats' : 'Number of Seats' }, inplace = True)

#Renaming the columns for better understanding
dataset.rename(columns={'Make': 'Manufacturer', 'id': 'Model Number'}, inplace= True)

#Changing the datatype of columns
dataset["Electric Range(Cold Whether)"] = dataset["Electric Range(Cold Whether)"].astype(int).astype(float)
dataset["Electric Range(Mild Whether)"] = dataset["Electric Range(Mild Whether)"].astype(int).astype(float)
dataset["Electric Range"] = dataset["Electric Range"].astype(int).astype(float)
dataset["Top Speed"] = dataset["Top Speed"].astype(int).astype(float)
dataset["Charge Speed"] = dataset["Charge Speed"].astype(int).astype(float)
dataset["Total Power"] = dataset["Total Power"].astype(int).astype(float)
dataset["Total Torque"] = dataset["Total Torque"].astype(int).astype(float)

#Checking datatype of all columns
dataset.dtypes

#Showing the count of the missing data
total_data=dataset.isnull().sum().sort_values(ascending=False)
print(total_data)

"""**Basic Information about dataset**"""

#Number of rows and columns in the dataset
dataset.shape

#Top 5 rows of dataset
dataset.head()

#Bottom 5 rows of dataset
dataset.tail()

#Describing the dataset
dataset.describe()

#Information about dataset
dataset.info()

#Unique values in each column
dataset.nunique()

#Unique manufacturer of EVs
print('\n Manufacturers : \n',dataset['Manufacturer'])

"""**Dataset Correlation**"""

#Coorelation Matrix between numeric columns of dataset
dataset.corr()

#Heatmap between numeric columns of dataset
plt.figure(figsize=(20,20))
sns.set(font_scale=1)
sns.heatmap(dataset.corr(),annot=True)
plt.title("Heatmap between numeric columns of dataset",fontsize=20)
plt.show()

"""**Exploratory Data Analysis**

Pie chart 1 - Seating capacity
    Pie chart 2 - Drive type
    Pie chart 3 - Charge power

    Countplot 1 - Manufracturer (no. of cars)
    Countplot 2 - Electric Range and number of cars

    Box Plot 1 - Top speeds of each manufacturer
    Box Plot 2 - Electric Ranges of each manufacturer

    Bar Chart 1 - Average speed of each maufacturer
    Bar Chart 2 - Average Average Range of each manufacturer

    Relationship plot 1 - Accln time vs total torque
    Relationship plot 2 - Electric range vs battary capacity
    Relationship plot 3 - Total power vs top speed
    Relationship plot 4 - Subplots of Length vs GVWR, Width vs GVWR, Height vs GVWR

    Line Graph 1 - Total Torque vs Total Power

    Ques - Top speed of each manufacturer
    Ques - Top Electric Range of each manufacturer

**Graph 1 : Pie chart 1 - Seating Capacity**
"""

plt.figure(figsize=(6,6))
sns.set(font_scale=1)
values=dataset['Number of Seats'].value_counts(dropna=True)
plt.pie(values, autopct= lambda x: '{:.0f}'.format(x*values.sum()/100), labels = ['5 Seater','4 Seater','9 Seater','7 Seater','8 Seater'])
plt.title("Number of EVs according to Seating Capacity",fontsize=20)
plt.show()

"""**Graph 2 : Pie chart 2 - Drive type**"""

plt.figure(figsize=(6,6))
sns.set(font_scale=1)
values=dataset['Drive Type'].value_counts(dropna=True)
plt.pie(values, autopct= lambda x: '{:.0f}'.format(x*values.sum()/100) , labels = ['AWD', 'Front', 'Rear'])
plt.title("Number of EVs according to different Drive Type",fontsize=20)
plt.show()

"""**Graph 3 : Pie chart 3 - Charge Power**"""

plt.figure(figsize=(6,6))
sns.set(font_scale=1)
values=dataset['Charge Power'].value_counts(dropna=True)
plt.pie(values, autopct= lambda x: '{:.0f}'.format(x*values.sum()/100), labels = ['11kW','7.4kW','6.6kW','7.2kW','22kW'])
plt.title("Number of EVs according to different Charger Power",fontsize=20)
plt.show()

"""**Graph 4 : Countplot 1 - Manufracturer (no. of cars)**


"""

plt.figure(figsize=(20,15))
sns.set(font_scale=1)
ax = sns.countplot(x ='Manufacturer', data=dataset)
for p in ax.patches:
   ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x()+0.07, p.get_height()+0.2))
plt.xticks(rotation=90)
plt.title("Number of EVs of different companies",fontsize=20)
plt.xlabel("Manufacturer",fontsize=16)
plt.ylabel("No. of EVs",fontsize=16)
plt.show()

"""**Graph 5 : Countplot 2 - Electric Range - Histogram**"""

plt.figure(figsize=(10,10))
sns.set(font_scale=1)
ax = sns.histplot(data=dataset, x="Electric Range", bins=[100,200,300,400,500,600,700])
for p in ax.patches:
   ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x()+35, p.get_height()+0.7))
plt.xlabel("Electric Range (in km)",fontsize=16)
plt.ylabel("No. of EVs",fontsize=16)
plt.title("Number of EVs according to Electric Range",fontsize=20)
plt.show()

"""**Graph 6 : Box Plot 1 - Top speeds of each manufacturer**"""

plt.figure(figsize=(20,8))
sns.set(font_scale=1)
sns.boxplot(x='Manufacturer', y='Top Speed', data=dataset, notch=False)
plt.xticks(rotation=90)
plt.title('Top Speeds of EVs by different Manufacturer', fontsize=20)
plt.show()

"""**Graph 7 : Box Plot 2 - Electric Ranges of each manufacturer**"""

plt.figure(figsize=(20,8))
sns.set(font_scale=1)
sns.boxplot(x='Manufacturer', y='Electric Range', data=dataset, notch=False)
plt.xticks(rotation=90)
plt.title('Electric Range of EVs by different Manufacturer', fontsize=20)
plt.show()

"""**Graph 8 : Bar Chart 1 - Average speed of each maufacturer**"""

df_g = dataset[['Manufacturer','Top Speed']].groupby('Manufacturer', as_index = False)[['Top Speed']].mean()
plt.figure(figsize=(20,10))
sns.set(font_scale=0.8)
ax = sns.barplot(data = df_g, y = 'Top Speed', x = 'Manufacturer')
for p in ax.patches:
   ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x(), p.get_height()+0.7))
plt.xticks(rotation=90)
plt.xlabel("Manufacturer",fontsize=16)
plt.ylabel("Average Speed (in km/h)",fontsize=16)
plt.title("Average Speed offered by different manufacturer of EVs",fontsize=20)
plt.show()

"""**Graph 9 : Bar Chart 2 - Average Electric Range of each manufacturer**"""

df_g = dataset[['Manufacturer','Electric Range']].groupby('Manufacturer', as_index = False)[['Electric Range']].mean()
plt.figure(figsize=(20,10))
sns.set(font_scale=0.8)
ax = sns.barplot(data = df_g, y = 'Electric Range', x = 'Manufacturer')
for p in ax.patches:
   ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x(), p.get_height()+0.7))
plt.xticks(rotation=90)
plt.xlabel("Manufacturer",fontsize=16)
plt.ylabel("Average Electric Range (in km)",fontsize=16)
plt.title("Average Electric Range offered by different manufacturer of EVs",fontsize=20)
plt.show()

"""**Graph 10 : Relationship plot 1 - Accln time vs total torque**"""

plt.figure(figsize=(20,10))
sns.set(font_scale=0.8)
sns.relplot(x='Acceleration Time', y='Total Torque',data=dataset)
plt.xlabel('Acceleration Time (in sec)',fontsize=14)
plt.ylabel('Total Torque (in Nm)',fontsize=14)
plt.title("Scatter Plot between Accleration Time and Total Torque",fontsize=18)
plt.show()

"""**Graph 11 : Relationship plot 2 - Electric range vs Battery Capacity**"""

plt.figure(figsize=(20,10))
sns.set(font_scale=0.8)
sns.relplot(x='Electric Range', y='Battery Capacity',data=dataset)
plt.xlabel('Electric Range (in km)',fontsize=14)
plt.ylabel('Battery Capacity (in kWh)',fontsize=14)
plt.title("Scatter Plot between Electric range and Battery Capacity",fontsize=18)
plt.show()

"""**Graph 12 : Relationship plot 3 - Total power vs top speed**"""

plt.figure(figsize=(20,10))
sns.set(font_scale=0.8)
sns.relplot(x='Total Power', y='Top Speed',data=dataset)
plt.xlabel('Total Power (in kW)',fontsize=14)
plt.ylabel('Top Speed (in km/h)',fontsize=14)
plt.title("Scatter Plot between Total Power and Top Speed",fontsize=18)
plt.show()

"""**Graph 13 : Relationship plot 4 - Subplots of Length vs GVWR, Width vs GVWR, Height vs GVWR**"""

variables = ['Length','Width','Height']
fig = plt.figure(figsize=(30,45))
sns.set(font_scale=1)
num = 1
for variable in variables:
  ax = fig.add_subplot(3,1,num)
  sns.scatterplot(x = variable, y = "Gross Vehicle Weight (GVWR)", hue="Manufacturer", data=dataset)
  plt.title("Relation between {} and Gross Vehicle Weight (GVWR)".format(variable))
  plt.xlabel(variable)
  plt.ylabel("Gross Vehicle Weight (GVWR)")
  num += 1

"""#**Statistical Analysis**

**Analysis 1 : Details of Top Speed EV in the dataset**
"""

print("Max Speed of Top Speed EV in the dataset =",max(dataset['Top Speed']),"km/h \n")
print(dataset.iloc[dataset['Top Speed'].idxmax()])

"""**Analysis 2 : Details of Best EV in terms of Electric Range**


"""

print("Max Electric Range of EVs in the dataset =",max(dataset['Electric Range']),"km \n")
print(dataset.iloc[dataset['Electric Range'].idxmax()])

"""**Analysis 3 : Details of Best EV in terms of Battery Capacity**"""

print("Max Battery Capacity of EVs in the dataset =",max(dataset['Battery Capacity']),"kWh \n")
print(dataset.iloc[dataset['Battery Capacity'].idxmax()])

s = dataset.loc[dataset['Battery Capacity'] == dataset['Battery Capacity'].max(),'Manufacturer']
print(s)

"""**Analysis 4 : Details of Best EV in terms of Efficiency**



"""

#Calculating Efficiency of all EVs available in the dataset

#Efficiency of EV (in Wh/km) = Battery Capacity/Electric Range

dataset["Efficiency"]=(dataset['Battery Capacity']*1000)/dataset['Electric Range']
print(dataset.Efficiency)
print()

print("Max Efficiency of EVs in the dataset =",max(dataset['Efficiency']),"Wh/km \n")
print(dataset.iloc[dataset['Efficiency'].idxmax()])

"""**Analysis 5 : Details of Best EV in terms of Charge Time**


"""

#Calculating Charging Time of all EVs available in the dataset

#Charging Time of EV (in hours) = Electric Range/Charge Speed

dataset["Charge_Time"]=dataset['Electric Range']/dataset['Charge Speed']
print(dataset.Charge_Time)
print()

print("Min Charge Time of EVs in the dataset =",min(dataset['Charge_Time']),"hours\n")
print(dataset.iloc[dataset["Charge_Time"].idxmin()])

"""**Analysis 6 : Top Speed EV with maximum possible Seating Capacity**

"""

# Here we are considering EVs whose speed is greater than average Top Speed of all EVs in dataset and EVs which provide maximum Seating Capacity

maxseat = max(dataset['Number of Seats'][(dataset['Top Speed'] >= dataset['Top Speed'].mean())])
u = dataset['Number of Seats'][(dataset['Top Speed'] >= dataset['Top Speed'].mean() )] == maxseat
for i in u.index:
  if u[i] == True:
    print(i)

print("Top Speed EVs with maximum possible Seating Capacity are : ")
print(dataset['Manufacturer'][93] +' '+ str(dataset['Model Number'][93]))
print(dataset['Manufacturer'][94] +' '+ str(dataset['Model Number'][94]))

"""**Analysis 7 : Best long range EV with maximum possible Seating Capacity**"""

# Here we are considering EVs whose electric range is greater than average electric range of all EVs in dataset and EVs which provide maximum Seating Capacity

maxseat = max(dataset['Number of Seats'][(dataset['Electric Range'] >= dataset['Electric Range'].mean())])
u = dataset['Number of Seats'][(dataset['Electric Range'] >= dataset['Electric Range'].mean() )] == maxseat
for i in u.index:
  if u[i] == True:
    print(i)

print("Best long range EVs with maximum possible Seating Capacity are : ")
print(dataset['Manufacturer'][93] +' '+ str(dataset['Model Number'][93]))
print(dataset['Manufacturer'][94] +' '+ str(dataset['Model Number'][94]))

"""**Analysis 8 : Top Speed EV with maximum possible Cargo Space**"""

# Here we are considering EVs whose speed is greater than average Top Speed of all EVs in dataset and EVs which provide maximum Cargo Volume

maxspace = max(dataset['Cargo Volume'][(dataset['Top Speed'] >= dataset['Top Speed'].mean())])
u = dataset['Cargo Volume'][(dataset['Top Speed'] >= dataset['Top Speed'].mean() )] == maxspace
for i in u.index:
  if u[i] == True:
    print(i)

print("Top Speed EVs with maximum possible Cargo Space are : ")
print(dataset['Manufacturer'][138] +' '+ str(dataset['Model Number'][138]))
print(dataset['Manufacturer'][151] +' '+ str(dataset['Model Number'][151]))

"""**Analysis 9 : Best long range EV with maximum possible Cargo Space**"""

# Here we are considering EVs whose electric range is greater than average electric range of all EVs in dataset and EVs which provide maximum Cargo Volume

maxspace = max(dataset['Cargo Volume'][(dataset['Electric Range'] >= dataset['Electric Range'].mean())])
u = dataset['Cargo Volume'][(dataset['Electric Range'] >= dataset['Electric Range'].mean() )] == maxspace
for i in u.index:
  if u[i] == True:
    print(i)

print("Best long range EVs with maximum possible Cargo Space are : ")
print(dataset['Manufacturer'][138] +' '+ str(dataset['Model Number'][138]))
print(dataset['Manufacturer'][151] +' '+ str(dataset['Model Number'][151]))

"""**Analysis 10 : Manufacturer which gives best electric range in cold weather and mild weather**"""

#Which EV manufacturer gives best electric range in cold weather

s1 = dataset.loc[dataset['Electric Range(Cold Whether)'] == dataset['Electric Range(Cold Whether)'].max(), 'Manufacturer']
print("Max Electric Range in Cold Weather =",max(dataset["Electric Range(Cold Whether)"]),"km \n")
print("Manufacturer which gives best electric range in cold weather is ")
print(s1)

print()

#Which EV manufacturer gives best electric range in mild weather

s2 = dataset.loc[dataset['Electric Range(Mild Whether)'] == dataset['Electric Range(Mild Whether)'].max(), 'Manufacturer']
print("Max Electric Range in Mild Weather =",max(dataset["Electric Range(Mild Whether)"]),"km \n")
print("Manufacturer which gives best electric range in mild weather is ")
print(s2)

"""**Analysis 11 : Manufacturer wise best EV in terms of Electric Range in Cold Weather and Mild Weater**"""

#Best EV in terms of Electric Range in Cold Weather of each manufacturer
new1 = dataset[['Model Number','Manufacturer','Electric Range(Cold Whether)']].groupby(['Manufacturer']).max()
new1

#Best EV in terms of Electric Range in Mild Weather of each manufacturer
new2 = dataset[['Model Number','Manufacturer','Electric Range(Mild Whether)']].groupby(['Manufacturer']).max()
new2

"""**Analysis 12 : Charge Speed Average and EVs above Average Charge Speed**"""

#Charge Speed Average
print("Average Charge Speed of EVs in the dataset =",dataset['Charge Speed'].mean(),"km/h \n")

#EVs above average charge speed
print("Details of EVs which have Charge Speed above Average Charge Speed : \n")
dataset[dataset['Charge Speed'] > dataset['Charge Speed'].mean()]
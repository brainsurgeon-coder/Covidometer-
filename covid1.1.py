import requests
import json
import pandas as pd
from pandas import DataFrame
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




#intros
print(" Welcome to Live COVIDOMETER 1.1! - © Dr Hrishikesh Sarkar ".center(80,'*'))
print("Data Source - Worldometer, cdc.gov, Johns Hopkins, astsiasko(RapidAPI)")
print("*".center(80, '*'))
print()

#variables, setting url, API endpoint, query parameter, headers
entry = input("Enter the name of country to fetch the data  ")

url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

querystring = {"country": entry}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "7d2dc6ae87mshf52f13eb6ce2d12p17dbdejsn976751fafe61"
    }

#.request method to get response from server
response = requests.request("GET", url, headers=headers, params=querystring)

#print(len(response.json()))

# creating json file of the reponse 
dict1 = response.json()
dict2 = dict1["latest_stat_by_country"][0]
def remove_empty_from_dict(dict2):
    if type(dict2) is dict:
        return dict((k, remove_empty_from_dict(v)) for k, v in dict2.items() if v and remove_empty_from_dict(v))
    elif type(dict2) is list:
        return [remove_empty_from_dict(v) for v in d if v and remove_empty_from_dict(v)]
    else:
        return dict2
    
dict3 = remove_empty_from_dict(dict2)
#print(dict3)

#json data mapping and setting the required variables
total_cases = dict1["latest_stat_by_country"][0]["total_cases"]
new_cases = dict1["latest_stat_by_country"][0]["new_cases"]
active_cases = dict1["latest_stat_by_country"][0]['active_cases']
total_deaths = dict1["latest_stat_by_country"][0]['total_deaths']
total_recovered = dict1["latest_stat_by_country"][0]['total_recovered']
serious_critical = dict1["latest_stat_by_country"][0]['serious_critical']
record_date = dict1["latest_stat_by_country"][0]['record_date']

#print("Total no of cases: ", total_cases)
#print("Total no of new cases: ", new_cases) 
#print("Total no of active_cases: ", active_cases)
#print("Total no of deaths: " , total_deaths) 
#print("Total no new deaths: ", new_deaths)
#print("Total recovered: ", total_recovered)
#print("Total serious: ", serious_critical) 
#print("Data recorded: ", record_date)
    
    
y = [int(total_cases.replace(',', '')), int(total_deaths.replace(',', '')), int(new_cases.replace(',', '')), int(active_cases.replace(',', ''))]   
#y_Count = [int(total_cases.replace(',', '')), int(new_cases.replace(',', '')), int(active_cases.replace(',', '')), int(total_deaths.replace(',', '')), int(new_deaths.replace(',', '')), int(total_recovered.replace(',', '')), int(serious_critical.replace(',', ''))]
#print(y_Count) 
#x_data = ["total_cases1", "new_cases1", "active_cases1", "total_deaths1", "new_deaths1", "total_recovered1", "serious_critical1"]

#xpos = np.arange(len(x_data))
#print(xpos)
#plt.bar(xpos, y_Count)
#plt.show()

#print(type(Count))

#df = pd.concat([pd.DataFrame(v) for k,v in dict1.items()], keys=dict1)
#print (df)
#print(pd.concat(map(pd.DataFrame, dict1.values()), keys=dict1.keys()).stack().unstack(0))
#df = pd.Panel.from_dict(dict1).to_frame()
df = pd.DataFrame([dict3])
#print(df)
df1 = DataFrame.transpose(df)
#print(df1)
df2 = df1.dropna()
#print(df2.index.values)
#print(df2.columns.values)
#df2.drop(df2.drop[0], axis =0, inplace = True)
#print(df2)

#pd.DataFrame([dict_])
#df2 = json_normalize(df['latest_stat_by_country'])
#print(df2)

#parameters = ["total_cases1", "new_cases1", "serious_critical1"]
#counts = [total_cases, new_cases, serious_critical]
#df2.plot.bar(x="parameters", y="counts", rot=70, title="Number of tourist visits - Year 2018");

#plot.show(block=True);
#print(df2.columns.tolist())
#df2 = df2.drop(df2.columns[[2:9:3]], axis=1, inplace=True)
#print(df2.columns.tolist())
#df3 = df2.delete(['id', 'record_date'])
#print(df2)
#df2 = df1.reset_index()
#print(df3)
#df2.dtypes

#print(y)
data = y
labels = ['Total Cases', 'Total Deaths', 'New cases', 'Active Cases' ]
my_colors = 'grbykmc'
plt.figure(figsize=(10,8))
plt.yticks(range(len(data)), labels)
plt.barh(range(len(data)), data, color=my_colors)
for i, v in enumerate(y):
    plt.text(v, i, v, color='blue', va='center', fontweight='bold')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.3)
plt.xlabel('Covid Statistics', fontsize = 20)
plt.ylabel('Count', fontsize = 20)
plt.title('Most recent Covid 19 statistics from ' + entry +  " updated at \n" + record_date, fontsize = 20)
plt.show()

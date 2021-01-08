import pandas as pd
import json
import datetime

# Reads the downloaded data
json_file = open('occupation.json', 'r')
lines = json_file.readlines()

data = []
for line in lines:
    data.append(json.loads(line))

# Reads the json file
# into a DataFrame
new_data = pd.DataFrame()
for line in data:
    new_data = new_data.append(pd.DataFrame.from_records(pd.DataFrame.from_records(line['hits']['hits'])['_source']))

# Converts date to correct type
new_data['dataNotificacaoOcupacao'] = pd.to_datetime(new_data['dataNotificacaoOcupacao'], infer_datetime_format=True).dt.date


# Reads the previous data
# and reshapes it as needed
prev_data = pd.read_csv("occupation.csv", low_memory = False)
prev_data = prev_data.drop(prev_data.columns[0], axis = 1)
prev_data = prev_data[new_data.columns]

# Appends the new data to previous data
df = prev_data.append(new_data)

# Sorts the dataframe and save a csv image of it
df = df.sort_values(by = ['estadoSigla', 'municipio', 'nomeCnes', 'dataNotificacaoOcupacao'])
df = df.drop_duplicates()

df.to_csv("occupation.csv")

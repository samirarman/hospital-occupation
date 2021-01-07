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
df = pd.DataFrame()
for line in data:
    df = df.append(pd.DataFrame.from_records(pd.DataFrame.from_records(line['hits']['hits'])['_source']))

# Converts date to correct type
df['dataNotificacaoOcupacao'] = pd.to_datetime(df['dataNotificacaoOcupacao'], infer_datetime_format=True).dt.date

# Sorts the dataframe and save a csv image of it
df = df.sort_values(by = ['estadoSigla', 'municipio', 'nomeCnes', 'dataNotificacaoOcupacao'])
df = df.drop_duplicates()
df.to_csv("occupation.csv")

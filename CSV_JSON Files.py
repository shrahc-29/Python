#importing csv file from local PC
from google.colab import files
uploaded = files.upload()

#Operations on csv file
import pandas as pd
df = pd.read_csv('healthcare.csv')
print(df)
print("    ")
print("    ")
print("    ")
print(df.info())

import json
from google.colab import files
uploaded = files.upload()

#Operations on json file
import pandas as pd
df2 = pd.read_json('java.json')
print(df2)
print("   ")
print("   ")
print("   ")
print(df2.info())


#Merging both tables
merge = pd.merge(df,df2, on='ID')
print(merge)


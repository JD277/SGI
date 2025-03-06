import json
import pandas as pd

#Convierte un archivo de formato json a una variable tipo Dataframe de Pandas
def json2dataframe(path):
    with open(path) as j:
        dictionary = json.load(j)
    
    dataframe = pd.DataFrame.from_dict(dictionary, orient= 'index')
    dataframe.columns
    dataframe = dataframe.T

    
    return dataframe
    


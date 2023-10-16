
import pandas as pd
import os
import pprint
ruta_csv = '../data_set/flights_final.csv'

#Ruta Absoluta del Dataset
ruta_absoluta = os.path.abspath(ruta_csv)


df = pd.read_csv(ruta_absoluta)

df = df.reset_index(drop=True)

#filtra el dataset sin filas que esten exactamente repetidas
df = df.drop_duplicates()
df = df.reset_index(drop=True)
num_filas, num_columnas = df.shape


#crear un diccionario para guardar el source_airport_code y el destination_airport_code, a los que son iguales ponerle el mismo id
diccionario = {}
codido_id = 1
for i in range(num_filas):
    if df['Source Airport Code'][i] not in diccionario:
        diccionario[df['Source Airport Code'][i]] = codido_id
        codido_id += 1

for i in range(num_filas):
    if df['Destination Airport Code'][i] not in diccionario:
        diccionario[df['Destination Airport Code'][i]] = codido_id
        codido_id += 1










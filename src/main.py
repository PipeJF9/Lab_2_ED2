from weighted_graph import WeightedGraph, Node
from manejo_data_set import df, diccionario,distancia_haversine
from Map import add_markers

#instancia de la clase WeightedGraph
graph = WeightedGraph(len(diccionario))


diccionario1 = {} #diccionario para guardar el source_airport_code y el destination_airport_code, a los que son iguales ponerle el mismo id
contador1 = 1 #contador para asignar el id a cada nodo

#agregar los nodos al grafo
for index, row in df.iterrows():
    if row['Source Airport Code'] not in diccionario1:
        diccionario1[row['Source Airport Code']] = contador1
        contador1 += 1
        graph.add_node(Node(row['Source Airport Code'], row['Source Airport Name'], row['Source Airport City'], row['Source Airport Country'], row['Source Airport Latitude'], row['Source Airport Longitude']))

    #agregar los nodos al grafo que no esten en source_airport_code si no en destination_airport_code
    if row['Destination Airport Code'] not in diccionario1:
        diccionario1[row['Destination Airport Code']] = contador1
        contador1 += 1
        graph.add_node(Node(row['Destination Airport Code'], row['Destination Airport Name'], row['Destination Airport City'], row['Destination Airport Country'], row['Destination Airport Latitude'], row['Destination Airport Longitude']))

#agregar las aristas al grafo
Vuelos= []
for index, row in df.iterrows():
    source_airport_code = row['Source Airport Code']
    destination_airport_code = row['Destination Airport Code']
    distancia=distancia_haversine(float(row['Source Airport Latitude']),float(row['Source Airport Longitude']),float(row['Destination Airport Latitude']),float(row['Destination Airport Longitude']))
    Vuelos.append([source_airport_code, destination_airport_code,str(distancia)])
    source_node = graph.search_node(source_airport_code)
    destination_node = graph.search_node(destination_airport_code)
    if source_node is not None and destination_node is not None:
        graph.add_edge(source_node, destination_node)
print(len(graph.nodes))
print(len(Vuelos))
#Map = add_markers(graph)
#Map.show_in_browser()

valores_unicos = set()
valores=[]
for fila in Vuelos:
    # Ordena la fila para asegurarte de que las columnas no importen
    fila_ordenada = sorted(fila,reverse=True)

    # Convierte la fila ordenada en una tupla para que sea hasheable y pueda usarse en el conjunto
    fila_tupla = tuple(fila_ordenada)

    # Si la fila ordenada no está en el conjunto, es un valor único
    if fila_tupla not in valores_unicos:
        valores.append(fila_ordenada)
        valores_unicos.add(fila_tupla)

print(len(graph.aristas))
print(len(valores_unicos))
print(len(valores))

#graph.Dijkstra("HUS",valores)

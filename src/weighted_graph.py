import math

from typing import Any, List, Optional, Tuple
from queue import Queue


class Node:

    #constructor de la clase Node recibe los parametros de la clase que se encuentra en manejo_data_set.py
    # y añadir el parametro codigo_id y los nodos adyacentes
    def __init__(self, Source_Airport_Code: str, Source_Airport_Name: str,
                 Source_Airport_City: str, Source_Airport_Country: str,
                 Source_Airport_Latitude: float, Source_Airport_Longitude: float,
                 codigo_id: int
                 ) -> None:
        self.Source_Airport_Code = Source_Airport_Code
        self.Source_Airport_Name = Source_Airport_Name
        self.Source_Airport_City = Source_Airport_City
        self.Source_Airport_Country = Source_Airport_Country
        self.Source_Airport_Latitude = Source_Airport_Latitude
        self.Source_Airport_Longitude = Source_Airport_Longitude
        self.codigo_id = codigo_id
        self.edges: List["Node"] = []

    #añadir los nodos adyacentes
    def add_edge(self, node: "Node") -> None:
        if node not in self.edges:
            self.edges.append(node)

    def __str__(self) -> str:
        return f"Source_Airport_Code: {self.Source_Airport_Code}\nSource_Airport_Name: {self.Source_Airport_Name}\nSource_Airport_City: {self.Source_Airport_City}\nSource_Airport_Country: {self.Source_Airport_Country}\nSource_Airport_Latitude: {self.Source_Airport_Latitude}\nSource_Airport_Longitude: {self.Source_Airport_Longitude}\nID: {self.codigo_id}\n"

class WeightedGraph:

    INF = (1 << 31) - 1  # 2 ** 31 - 1

    #constructor de la clase WeightedGraph recibe el parametro n que es el numero de nodos
    def __init__(self, n: int) -> None:
        self.n = n
        self.nodes: List["Node"] = []
        self.C = [[0 for i in range(n)] for j in range(n)]

    #añadir los nodos
    def add_node(self, node: "Node") -> None:
        self.nodes.append(node)

    #añadir las aristas
    def add_edge(self, node1:"Node", node2:"Node") -> bool:
        weight = self.haversine(node1.Source_Airport_Latitude, node1.Source_Airport_Longitude, node2.Source_Airport_Latitude, node2.Source_Airport_Longitude)
        if not ((0 <= node1.codigo_id < self.n) and (0 <= node2.codigo_id < self.n)):
            return False
        self.C[node1.codigo_id][node2.codigo_id] = self.C[node2.codigo_id][node1.codigo_id] = weight
        node1.add_edge(node2)
        node2.add_edge(node1)
        return True

    #calcular la distancia
    def haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        R = 6372.8
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        lat1 = math.radians(lat1)
        lat2 = math.radians(lat2)
        a = math.sin(dLat / 2)**2 + math.cos(lat1) * \
            math.cos(lat2) * math.sin(dLon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c

    #buscar el nodo
    def search_node(self, source_airport_code: str) -> Optional["Node"]:
        for node in self.nodes:
            if node.Source_Airport_Code == source_airport_code:
                return node
        return None











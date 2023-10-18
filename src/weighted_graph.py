import math
import numpy as np
from typing import Any, List, Optional, Tuple
from queue import Queue


class Node:

    #constructor de la clase Node recibe los parametros de la clase que se encuentra en manejo_data_set.py
    # y los nodos adyacentes
    def __init__(self, Source_Airport_Code: str, Source_Airport_Name: str,
                 Source_Airport_City: str, Source_Airport_Country: str,
                 Source_Airport_Latitude: float, Source_Airport_Longitude: float,
                 ) -> None:
        self.Source_Airport_Code = Source_Airport_Code
        self.Source_Airport_Name = Source_Airport_Name
        self.Source_Airport_City = Source_Airport_City
        self.Source_Airport_Country = Source_Airport_Country
        self.Source_Airport_Latitude = Source_Airport_Latitude
        self.Source_Airport_Longitude = Source_Airport_Longitude
        self.edges: List[Tuple['Node', str]] = []

    #añadir los nodos adyacentes
    def add_edge(self, edge: Tuple['Node', str]) -> None:
        if edge not in self.edges:
            self.edges.append(edge)

    def __str__(self) -> str:
        return (f"Source_Airport_Code: {self.Source_Airport_Code}\n"
                f"Source_Airport_Name: {self.Source_Airport_Name}\n"
                f"Source_Airport_City: {self.Source_Airport_City}\n"
                f"Source_Airport_Country: {self.Source_Airport_Country}\n"
                f"Source_Airport_Latitude: {self.Source_Airport_Latitude}\n"
                f"Source_Airport_Longitude: {self.Source_Airport_Longitude}\n")

class WeightedGraph:

    INF = (1 << 31) - 1  # 2 ** 31 - 1

    #constructor de la clase WeightedGraph recibe el parametro n que es el numero de nodos
    def __init__(self, n: int) -> None:
        self.n = n
        self.nodes: List["Node"] = []
        self.aristas: List[Tuple[str, str,str]] = []

    #añadir los nodos
    def add_node(self, node: "Node") -> None:
        self.nodes.append(node)

    #añadir las aristas
    def add_edge(self, node1: "Node", node2: "Node") -> bool:
        weight = str(self.haversine(node1.Source_Airport_Latitude, node1.Source_Airport_Longitude, node2.Source_Airport_Latitude, node2.Source_Airport_Longitude))
        if (node1.Source_Airport_Code, node2.Source_Airport_Code,weight) in self.aristas or (node2.Source_Airport_Code, node1.Source_Airport_Code,weight) in self.aristas:
            return False
        self.aristas.append((node1.Source_Airport_Code, node2.Source_Airport_Code,weight))
        node1.add_edge((node2, weight))
        node2.add_edge((node1, weight))
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
    def __get_minimum(self, l):
        minor = ["", np.inf]
        index = -1
        for i in range(len(l)):
            if l[i][1] < minor[1]:
                minor = l[i].copy()
                index = i

        return (minor, index)

    def __print_iteration(self, distance, father):
        for key in distance:
         print(key + ": " + str(distance[key]) + " - " + (father[key] if father[key] != None else "-"), end=" | ")

        print()

  #source: nodo fuente
    def Dijkstra(self, source,conection):
        distance = dict()
        father = dict()
        visited = dict()

        for u in self.nodes:
            distance[u.Source_Airport_Code] = np.inf
            father[u.Source_Airport_Code] = None
            visited[u.Source_Airport_Code] = False

        distance[source] = 0
        queue = [[source, distance[source]]]
        while len(queue) != 0:
            t = self.__get_minimum(queue)
            u = t[0]
            u_name = u[0]
            queue.pop(t[1])
            visited[u_name] = True

            for v in conection:
                v_name = None
                if v[0] == u_name:
                    v_name, (v_weight) = v[1], float(v[2])
                elif v[1] == u_name:
                    v_name, v_weight = v[0], float(v[2])
                if (v_name != None):
                    if (not visited[v_name]):
                        if (distance[v_name] > distance[u_name] + v_weight):
                            distance[v_name] = distance[u_name] + v_weight
                            father[v_name] = u_name
                            queue.append([v_name, distance[v_name]])

        self.__print_iteration(distance, father)
            
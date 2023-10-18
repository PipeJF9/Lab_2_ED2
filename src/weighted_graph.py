import math
import numpy as np
from typing import Any, List, Optional, Tuple
from queue import Queue
from Map import aristas,show_in_browser

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
        self.aristas= None

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
    def __get_minimum(self, l):
        minor = ["", np.inf]
        index = -1
        for i in range(len(l)):
            if l[i][1] < minor[1]:
                minor = l[i].copy()
                index = i

        return (minor, index)

    #hallar las distancias minimas
    def distancias_minimas(self,distance,father):
        minimas=dict()
        for key in distance:
            total=0
            clave=key
            ws=0
            while ws==0:
                total=total+float(distance[clave])
                if father[clave]!=None:
                    clave=father[clave]
                else:
                    ws=1
            minimas[key]=total
        #self.tenmax(minimas)
        self.notinf(minimas,father,distance)
        return minimas
    #hallar las 10 distancias minimas
    def tenmax(self,minimas,father,distance):
        max_ordenadas = sorted(minimas.items(), key=lambda x: x[1], reverse=True)
        ten=max_ordenadas[:10]
        if ten[0][1]==0:
            return
    #hallar las aristas de las 10 distancias minimas (no sirve)   
        for key in ten:
            for clave in distance:
                if clave==key:
                    ws=0
                    l=clave
                    while ws==0:
                        if father[l]!=None:
                            aristas(self.search_node(l).Source_Airport_Latitude,self.search_node(l).Source_Airport_Longitude,self.search_node(father[l]).Source_Airport_Latitude,self.search_node(father[l]).Source_Airport_Latitude,l,father[l])
                            l=father[l]
                        else:
                            ws=1
        show_in_browser()

    #hallar las distancias infinitas y volverlas 0
    def notinf(self,distance,father,distance1):
        for key in distance:
            if distance[key]==np.inf:
                distance[key]=0
        self.tenmax(distance,father,distance1)
        return distance
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
        print(len(distance))
        print(len(father))

        
        return self.distancias_minimas(distance,father)
        #self.__print_iteration(distance, father)
    
    
import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList = DAO.getAllObjects()
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap = {}
        for v in self._artObjectList:
            self._idMap[v.object_id] = v

    def getNumNodes(self):
        return len(self._grafo.nodes)
    def getNumEdges(self):
        return len(self._grafo.edges)

    def creaGrafo(self):
        self.addEdges()
    def addEdges(self):
        self._grafo.clear_edges()


        #soluzione 1: Ciclare sui nodi

        # for u in self._artObjectList:
        #     for v in self._artObjectList:
        #         peso = DAO.getPeso(u,v)
        #         self._grafo.add_edge(u, v, weight = peso)
        #soluzione 2: una sola query
        allEdges = DAO.getAllConnessioni(self._idMap)

        for e in allEdges:
            self._grafo.add_edge(e.o1, e.o2, weight=e.peso)


    def checkExistence(self, idOggetto):
        return idOggetto in self._idMap
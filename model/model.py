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

    def getObjectFromId(self, idOggetto):
        return self._idMap[idOggetto]

    def getConnessa(self, v0int):
        v0 = self._idMap[v0int]


        #modo 1: successori di v0 in DFS
        successors =nx.dfs_successors(self._grafo, v0)
        allSucc = []
        for v in successors.values():
            allSucc.extend(v)
        # diz = {}
        # for i in allSucc:
        #     if i in diz:
        #         diz[i] += 1
        #     else:
        #         diz[i] = 1
        # for i in diz:
        #     if diz[i] > 1:
        #         print(i)

        print(f"Metodo 1 (succ): {len(allSucc)}")

        #modo 2: predecessori di v0 in DFS
        predecessors = nx.dfs_predecessors(self._grafo, v0)
        print(f"Metodo 2 (prec): {len(predecessors.values())}")

        #modo 3: conto i nodi dell'albero
        tree = nx.dfs_tree(self._grafo, v0)
        print(f"Metodo 3 (tree): {len(tree.nodes)}")

        #modo 4: node_coinnected_component
        connComp =nx.node_connected_component(self._grafo, v0)
        print(f"Metodo 4 (connected comp): {len(connComp)}")

        return len(connComp)

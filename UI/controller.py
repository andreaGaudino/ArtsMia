import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato"))

        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))
        self._view._btnCompConnessa.disabled = False
        self._view.update_page()

    def handleCompConnessa(self,e):
        idAdded = self._view._txtIdOggetto.value

        try:
            intId = int(idAdded)
            pass
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Il valore inserito non è valido"))

        if self._model.checkExistence(intId):
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intId} è presente nel grafo"))
        else:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intId} non è presente nel grafo"))

        sizeConnessa = self._model.getConnessa(intId)
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {intId} ha {sizeConnessa} archi"))

        #fill dd
        self._view._ddLun.disabled = False
        self._view._btnCercaPercorso.disabled = False
        myOptsNum = list(range(2, sizeConnessa))
        myOptsDD = list(map(lambda x: ft.dropdown.Option(x), myOptsNum))
        self._view._ddLun.options = myOptsDD
        self._view.update_page()



    def handleCercaPercorso(self, e):
        self._model.getBestPath(self._view._ddLun.value, self._model.getObjectFromId(self._view._txtIdOggetto.value))

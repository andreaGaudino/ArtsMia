import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.creaGrafo()
        self._view.txt_result.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato"))

        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))
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
        self._view.update_page()
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Slot
from schemas import PokemonCard

class SearchResultList:
    def __init__(self, list_widget: QListWidget):
        self._list = list_widget    
      
    @Slot(object)
    def catch_search_results(self, results: list) -> None:
        self.display(results)
        
    def widget(self) -> QListWidget:
        return self._list
        
    def display(self, items: list[PokemonCard]) -> None:
        self.widget().clear()
        for entry in items:
            item = QListWidgetItem(entry.__str__())
            self.widget().addItem(item)
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from interface import Ui_MainWindow

from data_loader import CardData

from search_list import SearchResultList
from signals import SearchSignals
from new_card_dialog import NewCardDialog

from errors import InvalidSetName


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialize()
        
    def _search_filter(self) -> str:
        return self.line_filter.text()
    
    def _search_type(self) -> str:
        return "SET" if self.chk_by_set.isChecked() else "NAME"
        
    def initialize(self) -> None:
        self._search_list = SearchResultList(self.list_search_result)
        
    def search_list(self) -> SearchResultList:
        return self._search_list
    
    def search_button(self) -> QPushButton:
        return self.pb_search
    
    def button_add_card(self) -> QPushButton:
        return self.pb_add_card
    
    def search_settings(self) -> dict:
        return {"search_type": self._search_type(), "search_filter": self._search_filter()}

class App:
    def __init__(self, db_path: str):
        super().__init__()
        self._app = QApplication(sys.argv)
        self._db = CardData.load(db_path)
        self._window: MainWindow = MainWindow()
        self._search_signals = SearchSignals()
        
        self._new_card_dialog = NewCardDialog()
        
        
        self._connection_client = ConnectionClient(self)
        self._window.show()
        self._app.exec()
        
    def window(self) -> MainWindow:
        return self._window
    
    def db(self) -> CardData:
        return self._db
    
    def search_signals(self) -> SearchSignals:
        return self._search_signals
    
    def search(self, search_settings: dict) -> None:
        try:
            results = self.db().search(**search_settings)
        except InvalidSetName:
            results = ['Nothing to see...']
        self.search_signals().search_finished(results)
        
    def new_card_dialog(self) -> NewCardDialog:
        return self._new_card_dialog

class ConnectionClient:
    def __init__(self, app: App):
        
        self._window = app.window()
        self._app = app
        self.initialize()
        
    def window(self) -> MainWindow:
        return self._window
    
    def app(self) -> App:
        return self._app
    
    def initialize(self) -> None:
        self.window().search_button().clicked.connect(lambda: self.app().search(self.window().search_settings()))
        self.app().search_signals().searchFinished.connect(self.window().search_list().catch_search_results)
        self.window().button_add_card().clicked.connect(self.app().new_card_dialog().exec)

         
if __name__ == '__main__':
    app = App('C:/projects/pokemon-bulk-tracker/source_file.json')
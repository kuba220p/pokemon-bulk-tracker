from PySide6.QtCore import QObject, Signal

class SearchSignals(QObject):
    searchFinished = Signal(object)
    
    def __init__(self) -> None:
        super(SearchSignals, self).__init__()
        
    def search_finished(self, results: list) -> None:
        self.searchFinished.emit(results)
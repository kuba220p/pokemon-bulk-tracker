from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QCheckBox, QWidget
from PySide6.QtCore import Qt

_RARITY_OPTIONS = ["Common", "Double Rare", "Illustration Rare", "Special Illustration Rare"]
_REVERSE_TYPE = ["Regular", "Pokeball", "Masterball", "Energy"]
_OPTION_SHORTCUT = {
    "Common": "C",
    "Double Rare": "DR",
    "Illustration Rare": "IR",
    "Special Illustration Rare": "SIR"
}

class NewCardDialog(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Add new pokemon card to database")
        
        self._name_line = QLineEdit()
        self._set_name = QLineEdit()
        self._card_no = QLineEdit()
        self._count = QLineEdit()
        self._rarity_combo = QComboBox()
        self._reverse_type = QComboBox()
        self._is_reverse = QCheckBox("Reverse Holo")
        self._ok = QPushButton("Add")
        
        self._layout = QHBoxLayout()
        
        self._name_line.setPlaceholderText("Card name")
        self._set_name.setPlaceholderText("Set name")
        self._card_no.setPlaceholderText("Card no.")
        self._count.setPlaceholderText("Amount owned")
        self._rarity_combo.setPlaceholderText("Choose rarity")
        self._reverse_type.setPlaceholderText("Reverse holo type")
        
        self._rarity_combo.addItems(_RARITY_OPTIONS)
        self._reverse_type.addItems(_REVERSE_TYPE)
        
        self._is_reverse.setDisabled(True)
        self._reverse_type.setDisabled(True)
        
        self.add_widget(self._name_line)
        self.add_widget(self._set_name)
        self.add_widget(self._card_no)
        self.add_widget(self._count)
        self.add_widget(self._rarity_combo)
        self.add_widget(self._is_reverse)
        self.add_widget(self._reverse_type)
        self.add_widget(self._ok)
        
        self.setLayout(self._layout)
        
        self._ok.clicked.connect(self._accept)
        self._is_reverse.stateChanged.connect(lambda: self._reverse_type.setEnabled(self._is_reverse.isChecked()))
        self._rarity_combo.currentIndexChanged.connect(lambda: self._is_reverse.setEnabled(self._rarity_combo.currentText() == "Common"))
        
        self._new_card: dict = None
        
    def new_card(self) -> dict:
        return self._new_card

    def add_widget(self, widget: QWidget):
        self._layout.addWidget(widget, Qt.AlignmentFlag.AlignLeft)
        
    def _accept(self) -> None:
        self._new_card = {
            "name": self._name_line.text(),
            "parent_set": self._set_name.text().upper(),
            "card_no": int(self._card_no.text()),
            "count": int(self._count.text()),
            "rarity": _OPTION_SHORTCUT[self._rarity_combo.currentText()],
            "is_reverse": self._is_reverse.isChecked(),
            "reverse_type": self._reverse_type.currentText()
        }
        
        self.accept()

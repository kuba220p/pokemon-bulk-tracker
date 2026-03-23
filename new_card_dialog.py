from PySide6.QtWidgets import QDialog, QLineEdit, QComboBox, QPushButton, QHBoxLayout, QCheckBox, QWidget
from PySide6.QtCore import Qt


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
        
        self.add_widget(self._name_line)
        self.add_widget(self._set_name)
        self.add_widget(self._card_no)
        self.add_widget(self._count)
        self.add_widget(self._rarity_combo)
        self.add_widget(self._is_reverse)
        self.add_widget(self._reverse_type)
        self.add_widget(self._ok)
        
        self.setLayout(self._layout)

    def add_widget(self, widget: QWidget):
        self._layout.addWidget(widget, Qt.AlignmentFlag.AlignLeft)
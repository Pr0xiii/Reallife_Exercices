from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from functools import partial

btns_dictionnary = {
    "C": (1, 0, 1, 1),
    "DEL": (1, 2, 1, 1),
    "/": (1, 3, 1, 1),
    "x": (2, 3, 1, 1),
    "-": (3, 3, 1, 1),
    "+": (4, 3, 1, 1),
    ".": (5, 2, 1, 1),
    "=": (5, 3, 1, 1),
    "1": (2, 0, 1, 1),
    "2": (2, 1, 1, 1),
    "3": (2, 2, 1, 1),
    "4": (3, 0, 1, 1),
    "5": (3, 1, 1, 1),
    "6": (3, 2, 1, 1),
    "7": (4, 0, 1, 1),
    "8": (4, 1, 1, 1),
    "9": (4, 2, 1, 1),
    "0": (5, 0, 1, 2),
}

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculatrice App")
        self.calculator_grid = QGridLayout(self)

        self.result_text = QLabel()
        self.result_text.setAlignment(Qt.AlignRight)
        self.calculator_grid.addWidget(self.result_text, 0, 3, 1, 4)

        self.setup_btns()

    def setup_btns(self):
        for cle, value in btns_dictionnary.items():
            btn = QPushButton(cle)
            if cle == "C":
                btn.pressed.connect(self.clear_line)
            elif cle == "DEL":
                btn.pressed.connect(self.delete_text)
            elif cle == "=":
                btn.pressed.connect(self.calculate)
            else:
                btn.pressed.connect(partial(self.onClickBtn, cle))

            self.calculator_grid.addWidget(btn, *value)

    def onClickBtn(self, item):
        self.last_text = self.result_text.text()
        self.result_text.setText(self.last_text + item)

    def clear_line(self):
        self.result_text.clear()

    def delete_text(self):
        self.result_text.setText(self.last_text)

    def calculate(self):
        final_text = self.result_text.text().replace("x", "*")
        result = eval(final_text)
        self.result_text.setText(str(result))

app = QApplication()
calculator_window = Calculator()

calculator_window.show()
app.exec()
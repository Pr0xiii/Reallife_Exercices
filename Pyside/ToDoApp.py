from PySide6.QtWidgets import QApplication, QWidget, QListWidget, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Docstring ToDo")

        main_box_layout = QVBoxLayout()
        self.setLayout(main_box_layout)
        self.list_widget = QListWidget()
        self.le_text = QLineEdit()
        self.le_text.setPlaceholderText("Que devons-nous faire aujourd'hui ?...")
        btn_clear = QPushButton("Tout supprimer")

        main_box_layout.addWidget(self.list_widget)
        main_box_layout.addWidget(self.le_text)
        main_box_layout.addWidget(btn_clear)

        self.le_text.returnPressed.connect(self.onEnterText)
        self.list_widget.itemDoubleClicked.connect(self.onSelectItem)
        btn_clear.pressed.connect(self.delete_all)
    
    def onEnterText(self):
        self.list_widget.addItem(self.le_text.text())
        self.le_text.clear()

    def onSelectItem(self):
        item = self.list_widget.currentItem()
        self.list_widget.takeItem(self.list_widget.row(item))

    def delete_all(self):
        self.list_widget.clear() 
        self.le_text.clear()


app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()

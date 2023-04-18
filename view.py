from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller

class View(QMainWindow):
    def __init__(self, c: Controller):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.pb_execute.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)
        self.inputNum.setRange(-1000,1000)
        self.setWindowTitle("Wurzelberechnung mit komplexen Zahlen")
        self.setTextStatusBar("Bitte geben Sie eine Zahl zur Berechnung der Wurzel ein")

    def reset(self)->None:
        self.inputNum.setValue(0.00)
        self.checkK.setChecked(False)
        self.output.clear()
        self.setTextStatusBar("Keine Berechnung durchgeführt!")

    def setTextStatusBar(self, text):
        self.statusbar.showMessage(text)

    def get_inputNum(self)->float:
        return self.inputNum.value()

    def get_checked(self)->bool:
        return self.checkK.isChecked()

    def set_output(self, t:str)->None:
        self.output.setText(t)



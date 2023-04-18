import sys
from PyQt6.QtWidgets import QApplication
from model import Model
import modelPos
import modelNeg
import view

class Controller():
    mo: Model

    def __init__(self)->None:
        self.view = view.View(self)
        self.model = Model()

    def reset(self):
        self.view.reset()

    def execute(self):
        num = self.view.get_inputNum()
        if(num>=0.00):
            self.model = modelPos.ModelPos()
            self.view.set_output(self.model.berechnen(num))
        if(num<0.00):
            if(self.view.get_checked()==True):
                self.model = modelNeg.ModelNeg()
                self.view.set_output(self.model.berechnen(num))
            else:
                self.view.set_output("Negative Zahl")
                self.view.setTextStatusBar("Achtung negative Zahl")
        self.view.setTextStatusBar("Berechnung durchgeführt!")

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
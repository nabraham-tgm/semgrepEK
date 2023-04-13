from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from Controller import Controller
class View(QMainWindow):
    def __init__(self, c: Controller):
        super().__init__()
        uic.loadUi("layout.ui", self)
        self.aktion.addItem("Schere")
        self.aktion.addItem("Stein")
        self.aktion.addItem("Papier")
        self.pb_execute.clicked.connect(c.execute)
        self.pb_reset.clicked.connect(c.reset)
        self.aktion.setToolTip("Wähle einen Spielzug aus")
        self.pb_execute.setToolTip("Ausführen")
        self.pb_reset.setToolTip("Zurücksetzen")
        self.pb_close.setToolTip("Schließen")

    def reset(self)->None:
        self.aktion.setCurrentIndex(0)
        self.player.setText("0")
        self.computer.setText("0")
        self.round.setText("1")
        self.playerpic.setPixmap(QPixmap())
        self.computerpic.setPixmap(QPixmap())
        self.set_text_statusbar(
    "Wähle einen Spielzug und klicke auf 'Ausführen' ")

    def set_round(self, t: str)->None:
        self.round.setText(t)

    def set_text_statusbar(self, t: str)->None:
        self.statusbar.showMessage(t)

    def set_player(self, t:str)->None:
        self.player.setText(t)

    def set_computer(self, t:str)->None:
        self.computer.setText(t)

    def set_playerpic(self, t:str)->None:
        self.playerpic.setPixmap(QPixmap(t))

    def set_computerpic(self, t:str)->None:
        self.computerpic.setPixmap(QPixmap(t))

    def get_aktion(self)->str:
        return self.aktion.currentText()

if __name__ == '__main__':
    import sys
    app = QApplication([])
    v = View()
    v.show()
    sys.exit(app.exec())
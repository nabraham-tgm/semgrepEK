import sys
from PyQt6.QtWidgets import QApplication
import model
import view

class Controller:
    def __init__(self):
        self.model = model.Generator()
        self.view = view.View(self)

    def reset(self) -> None:
        self.model.reset()
        self.view.reset()

    def execute(self) -> None:
        aktion = self.view.get_aktion()
        error = self.model.playing(aktion)

        if error is None:
            self.view.set_round(self.model.round)
            self.view.set_player(self.model.player)
            self.view.set_computer(self.model.computer)
            self.view.set_text_statusbar(self.model.text)
            self.view.set_playerpic(self.model.pixmapP)
            self.view.set_computerpic(self.model.pixmapC)
        else:
            self.view.set_round("Fehler")
            self.view.set_text_statusbar(error)

if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())
    
exec("something")

import random
class Generator:
    def __init__(self):
        self.player = None
        self.computer = None
        self.pixmapP = None
        self.pixmapC = None
        self.aktion = None
        self.round = None
        self.error = None
        self.count = 1
        self.playerscore = 0
        self.computerscore = 0
        self.text = None

    def computer_choice(self):
        self.computer = random.randint(0,2)

    def reset(self):
        self.player = "0"
        self.computer = "0"
        self.pixmapP = ""
        self.pixmapC = ""
        self.aktion = ""
        self.round = "1"
        self.error = None
        self.count = 1
        self.playerscore = 0
        self.computerscore = 0
        self.text = "Wähle einen Spielzug aus und klicke auf 'Ausführen'"


    def playing(self, aktion:str)->str:
        self.aktion = aktion
        self.count = self.count+1
        self.round = str(self.count)
        self.player = str(self.playerscore)
        self.computer = str(self.computerscore)

        if self.aktion == "Schere":self.Schere()
        elif self.aktion == "Stein":self.Stein()
        elif self.aktion == "Papier":self.Papier()
        else:
            self.error = "Fehler: Auswahl unbekannt".\
                format(self.aktion)
        return self.error

    def Schere(self)->None:
        self.pixmapP = "schere.png"
        possible_actions = ["Schere", "Stein", "Papier"]
        com = random.choice(possible_actions)
        if com == "Schere":
            self.text = "Unentschieden"
            self.pixmapC = "schere.png"
        elif com == "Stein":
            self.text = "Sie haben die Runde verloren"
            self.pixmapC = "stein.png"
            self.computerscore = self.computerscore+1
            self.computer = str(self.computerscore)
        elif com == "Papier":
            self.text = "Sie haben die Runde gewonnen"
            self.pixmapC = "papier.png"
            self.playerscore = self.playerscore+1
            self.player = str(self.playerscore)

    def Stein(self)->None:
        self.pixmapP = "stein.png"
        possible_actions = ["Schere", "Stein", "Papier"]
        com = random.choice(possible_actions)
        if com == "Schere":
            self.text = "Sie haben die Runde gewonnen"
            self.pixmapC = "schere.png"
            self.playerscore = self.playerscore+1
            self.player = str(self.playerscore)
        elif com == "Stein":
            self.text = "Unentschieden"
            self.pixmapC = "stein.png"
        elif com == "Papier":
            self.text = "Sie haben die Runde verloren"
            self.pixmapC = "papier.png"
            self.computerscore = self.computerscore+1
            self.computer = str(self.computerscore)

    def Papier(self)->None:
        self.pixmapP = "papier.png"
        possible_actions = ["Schere", "Stein", "Papier"]
        com = random.choice(possible_actions)
        if com == "Schere":
            self.text = "Sie haben die Runde verloren"
            self.pixmapC = "schere.png"
            self.computerscore = self.computerscore+1
            self.computer = str(self.computerscore)
        elif com == "Stein":
            self.text = "Sie haben die Runde gewonnen"
            self.pixmapC = "stein.png"
            self.playerscore = self.playerscore+1
            self.player = str(self.playerscore)
        elif com == "Papier":
            self.text = "Unentschieden"
            self.pixmapC = "papier.png"

    #if __name__ == '__main__':
        query = "SELECT * FROM users WHERE id = %s"

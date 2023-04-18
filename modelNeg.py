import requests
from model import Model


class ModelNeg(Model):
    def __init__(self):
        self.output = ""

    def berechnen(self, num: float):
        '''
        Hier wird die Eingabe/Zahl an das Webservice übermittelt und die Antwort zurück an den Controller geliefert.
        :param zahl:
        :return: Ausgabetext
        '''
        try:
            url = 'http://127.0.0.1:5000/wurzel'
            params = {'zahl': num, 'komplex': True}
            res = requests.get(url, params=params)
            res = res.json()
            self.output = f"Value: <b>{res['value']}</b> <br>" \
                          f"Wurzel: <b>{res['imag']}j</b> <br>"
            return self.output
        except:
           return "Webservice nicht verfügbar!"
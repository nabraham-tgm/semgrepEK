import requests
from model import Model


class ModelPos(Model):
    def __init__(self):
        self.ausgabe = ""

    def berechnen(self, num: float):
        '''

        :param num:
        :return:
        '''
        try:
            url = 'http://127.0.0.1:5000/wurzel'
            params = {'zahl': num}
            res = requests.get(url, params=params)
            res = res.json()
            self.ausgabe = f"Zahl: <b>{res['value']}</b> <br>" \
                          f"Wurzel: <b>{res['real']}</b> <br>"
            return self.ausgabe
        except:
            return "Problem mit dem Webservice"

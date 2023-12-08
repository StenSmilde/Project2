from PyQt6.QtWidgets import *
from Gui import *
import requests
from PIL import Image
from datetime import datetime
from requests.exceptions import RequestException


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.reset())
        self.pushButton_2.clicked.connect(lambda: self.get_forcast())

    def get_forcast(self):
        try:
            city = self.lineEdit.text()
            api_key = '1907f77f2aba9a9229147223194e5d61'
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
            weather_data.raise_for_status()  # raise HTTPError for bad responses (4xx and 5xx)
        except RequestException:
            self.label_15.setText(f'No city found')
            self.label_9.setText(f'')
            self.label_10.setText(f'')
            self.label_11.setText(f'')
            self.label_12.setText(f'')
            self.label_13.setText(f'')
            self.label_14.setText(f'')
            self.label_17.setText(f'')
        else:
            self.label_15.setText(f'')
            temp = weather_data.json()['main']['temp']
            self.label_9.setText(f'{temp}°F')
            feels_like = weather_data.json()['main']['feels_like']
            self.label_10.setText(f'{feels_like}°F')
            weather = weather_data.json()['weather'][0]['main']
            self.label_11.setText(f'{weather}')
            description = weather_data.json()['weather'][0]['description']
            self.label_12.setText(f'{description}')
            pressure = weather_data.json()['main']['pressure']
            self.label_13.setText(f'{pressure} hPa')
            humidity = weather_data.json()['main']['humidity']
            self.label_14.setText(f'{humidity}%')
            wind = weather_data.json()['wind']['speed']
            self.label_17.setText(f'{wind} mph')

    def reset(self):
        pass

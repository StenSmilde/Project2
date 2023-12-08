from PyQt6.QtWidgets import *
from Gui import *
import requests
from datetime import datetime
from requests.exceptions import RequestException
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.reset())
        self.pushButton_2.clicked.connect(lambda: self.get_forcast())

        self.weather_icon_label = QLabel(self)  # create QLabel for displaying the weather icon

        layout = QVBoxLayout(self)  # center the weather icon
        layout.addSpacing(-400)
        layout.addWidget(self.weather_icon_label)
        layout.setAlignment(self.weather_icon_label, Qt.AlignmentFlag.AlignCenter)
        self.centralWidget().setLayout(layout)

        self.setStyleSheet("background-color: lightblue;")   # set the background color for the Gui
        self.lineEdit.setStyleSheet("background-color: white;") # as well as the widgets
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton_2.setStyleSheet("background-color: white;")

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
            self.label_18.setText(f'')
            self.weather_icon_label.clear()
        else:
            date = datetime.fromtimestamp(weather_data.json()['dt'])
            self.label_18.setText(f'Today: {date}')
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

            icon_id = weather_data.json()['weather'][0]['icon'] # Display weather icon
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(icon_url).content)
            self.weather_icon_label.setPixmap(pixmap)

    def reset(self):
        self.label_15.setText(f'')
        self.label_9.setText(f'')
        self.label_10.setText(f'')
        self.label_11.setText(f'')
        self.label_12.setText(f'')
        self.label_13.setText(f'')
        self.label_14.setText(f'')
        self.label_17.setText(f'')
        self.lineEdit.setText(f'')
        self.label_18.setText(f'')
        self.weather_icon_label.clear()

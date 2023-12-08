from PyQt6.QtWidgets import *
from Gui import *
import requests
from datetime import datetime
from requests.exceptions import RequestException
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class containing all the logic for the gui.
    """

    def __init__(self) -> None:
        """
        Method to initialize functions, set the background color of the gui and place the weather icon.
        """
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

        self.setStyleSheet("background-color: lightblue;")  # set the background color for the Gui
        self.lineEdit.setStyleSheet("background-color: white;")  # as well as the widgets
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton_2.setStyleSheet("background-color: white;")

    def get_forcast(self) -> None:
        """
        Method to extract information from the weather application and show it on the gui. Exception handling is performed whenever an incorrect city name is entered.
        """
        try:
            city = self.lineEdit.text()
            api_key = '1907f77f2aba9a9229147223194e5d61'
            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")  # extract weather data
            weather_data.raise_for_status()  # raise HTTPError for bad responses (4xx and 5xx)
        except RequestException:
            self.label_15.setText(f'No city found.')
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
            self.label_15.setText(f'The weather today in {city}:')
            date = datetime.fromtimestamp(weather_data.json()['dt'])
            self.label_18.setText(f'Today: {date}')
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

            icon_id = weather_data.json()['weather'][0]['icon']  # display weather icon
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(icon_url).content)
            self.weather_icon_label.setPixmap(pixmap)

    def reset(self) -> None:
        """
        Method to reset every line including the weather icon.
        """
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

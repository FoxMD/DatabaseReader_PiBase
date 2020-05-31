import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
import sqlite3

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My window name")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.read.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        database = DatabaseConnector()  # sqlite3.connect('E:\\Programming\\betaDB.db')
        database.getNewValues()

        temperature = round(database.latestTemperature, 1)
        temperature = str(temperature) + "°C"

        pressure = round(database.latestPressure, 0)
        pressure = str(pressure) + "hPa"

        humidity = round(database.latestHumidity, 1)
        humidity = str(humidity) + "%"

        self.ui.temperature_text.setText(temperature)
        self.ui.humidity_text.setText(humidity)
        self.ui.pressure_text.setText(pressure)


class DatabaseConnector:
    def __init__(self):
        self.connected = True
        self.databaseName = "myDatabase"
        self.address = 'E:\\Programming\\betaDB.db'  # "192.168.0.2"
        self.port = "3306"

        self.latestTemperature = 0
        self.latestHumidity = 0
        self.latestPressure = 0

    def getNewValues(self):
        conn = sqlite3.connect(self.address)
        curs = conn.cursor()

        for row in curs.execute("SELECT * FROM stuffToPlot ORDER BY datestamp DESC LIMIT 1"):
            time = str(row[1])
            self.latestTemperature = row[3]
            self.latestHumidity = row[5]
            self.latestPressure = row[7]

        conn.close()


window = MainWindow()

window.show()

sys.exit(app.exec_())

# get data
# def getHistData(numSamples):
#    curs.execute("SELECT * FROM stuffToPlot ORDER BY datestamp DESC LIMIT " + str(numSamples))
#    data = curs.fetchall()
#    dates = []
#    temps = []
#    hums = []
#    presss = []
#    for row in reversed(data):
#        dates.append(row[1])
#        temps.append(row[3])
#        hums.append(row[5])
#        presss.append(row[7])
#    return dates, temps, hums, presss

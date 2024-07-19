import sys

from PySide6.QtWidgets import QMessageBox
from matplotlib.figure import Figure

from Backend.Server import Server
from UI.ui import *
from Validators.FunctionValidator import FunctionValidator
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar

class MainWindow(QMainWindow):
    def __showMessage__(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Parsing Error")
        msg_box.setText(message)
        msg_box.exec()

    def __submit__(self):
        equation = self.ui.functionInput.text()

        errorMessage = self.functionValidator.validate(equation)
        if errorMessage != "":
            self.__showMessage__(errorMessage)
            return False

        xMin = self.ui.xMinInput.text()
        xMax = self.ui.xMaxInput.text()

        def isNumber(x):
            try:
                float(x)  # Try to convert the string to a float
                return True
            except ValueError:
                return False


        if not isNumber(xMin) or not isNumber(xMax):
            self.__showMessage__("Range Values Must Be Numbers")
            return False

        xMin = float(xMin)
        xMax = float(xMax)

        if xMin > xMax:
            self.__showMessage__("range start must be less than or equal to range end")
            return False

        xList, yList = self.server.generatePlot(equation, xMin, xMax)
        self.createPlotCanvas(xList, yList)

    def zoom(self,event):
        # Get the current x and y limits
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        # Get the zoom factor
        zoom_factor = 1.1 if event.button == 'down' else 0.9

        # Calculate the new limits
        x_center = event.xdata
        y_center = event.ydata
        x_range = (xlim[1] - xlim[0]) * zoom_factor
        y_range = (ylim[1] - ylim[0]) * zoom_factor

        self.ax.set_xlim([x_center - x_range / 2, x_center + x_range / 2])
        self.ax.set_ylim([y_center - y_range / 2, y_center + y_range / 2])

        # Redraw the canvas
        self.canvas.draw_idle()


    def __init__(self):
        super(MainWindow, self).__init__()

        width = 605
        height = 492
        # setting  the fixed size of window
        self.setFixedSize(width, height)

        self.toolbar = None
        self.canvas = None
        self.ax = None
        self.functionValidator = FunctionValidator()
        self.server = Server()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.createPlotCanvas([],[])
        self.invokeListeners()

    def invokeListeners(self):
        self.ui.plotButton.clicked.connect(self.__submit__)

    def createPlotCanvas(self, x, y):
        if self.canvas is not None:
            self.ui.plotArea.removeWidget(self.canvas)
            self.ui.plotArea.removeWidget(self.toolbar)

        fig = Figure(facecolor="silver", edgecolor="red", dpi=100)
        self.ax = fig.add_subplot()

        self.ax.set_facecolor('red')
        self.ax.plot(x, y, color="#000000")
        self.ax.grid()
        self.ax.set_xlim([-20, 20])
        self.ax.set_ylim([-20, 20])
        # Set axis color to white
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('white')

        self.canvas = FigureCanvasQTAgg(fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.ui.plotArea.addWidget(self.toolbar)
        self.ui.plotArea.addWidget(self.canvas)

        self.canvas.mpl_connect("scroll_event", self.zoom)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

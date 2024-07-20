import sys

import numpy as np
from PySide6.QtWidgets import QMessageBox
from matplotlib.figure import Figure
from Backend.Server import Server
from UI.ui import *
from Validators.FunctionValidator import FunctionValidator
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar


class CustomToolbar(NavigationToolbar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_button_icons()
    
    def set_button_icons(self):
        # Modify the icons for each button
        for action in self.actions():
            icon = action.icon()
            pixmap = icon.pixmap(16, 16)
            colored_pixmap = self.color_pixmap(pixmap, Qt.red)  # Change color here
            action.setIcon(QIcon(colored_pixmap))

    def color_pixmap(self, pixmap, color):
        # Convert pixmap to QImage
        image = pixmap.toImage()
        # Apply color filter
        for x in range(image.width()):
            for y in range(image.height()):
                if image.pixelColor(x, y).alpha() > 0:  # Apply color only to non-transparent pixels
                    image.setPixelColor(x, y, color)
        return QPixmap.fromImage(image)


class MainWindow(QMainWindow):
    def __showMessage__(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Parsing Error")
        msg_box.setText(message)
        msg_box.exec()

    def __submit__(self):
        equation = self.ui.functionInput.text()

        if equation.replace(" ", "") == "":
            return

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

        if xMin >= xMax:
            self.__showMessage__("range start must be less than range end")
            return False

        try:
            xList, yList = self.server.generatePlot(equation, xMin, xMax)
        except Exception as e:
            self.__showMessage__("Parsing Error")
            return False

        self.createPlotCanvas(xList, yList)
        return True

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

        width = 991
        height = 665
        # setting  the fixed size of window
        self.setFixedSize(width, height)
        

        self.toolbar = None
        self.canvas = None
        self.limitsMargin = [1, 10]
        self.ax = None
        self.functionValidator = FunctionValidator()
        self.server = Server()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dezmoz")
        self.setWindowIcon(QIcon("./UI/rsc/icon.png"))

        self.createPlotCanvas([0], [0])
        self.invokeListeners()

    def invokeListeners(self):
        self.ui.plotButton.clicked.connect(self.__submit__)

    def createPlotCanvas(self, x, y):
        
        if (len(x) == 0) or len(y) == 0:
            x.append(0)
            y.append(0)

        if self.canvas is not None:
            self.ui.plotArea.removeWidget(self.canvas)
            self.ui.plotArea.removeWidget(self.toolbar)

        fig = Figure(facecolor="silver", edgecolor="red", dpi=100)
        self.ax = fig.add_subplot(1, 1, 1)

        self.ax.set_facecolor('red')
        self.ax.plot(x, y, color="#000000")
        self.ax.grid()

        first_quartile = np.percentile(y, 25)
        third_quartile = np.percentile(y, 75)

        self.ax.set_xlim([x[0] - self.limitsMargin[0], x[-1] + self.limitsMargin[0]])
        self.ax.set_ylim([first_quartile - self.limitsMargin[1], third_quartile + self.limitsMargin[1]])

        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('white')

        self.canvas = FigureCanvasQTAgg(fig)
        self.toolbar = CustomToolbar(self.canvas, self)
        self.ui.plotArea.addWidget(self.toolbar)
        self.ui.plotArea.addWidget(self.canvas)

        self.canvas.mpl_connect("scroll_event", self.zoom)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

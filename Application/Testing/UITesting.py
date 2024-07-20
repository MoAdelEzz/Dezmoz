import pytest
from PySide6.QtCore import Qt
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
from __init__ import MainWindow


@pytest.fixture(scope="module")
def app(request):
    qApp = QApplication.instance()
    if qApp is None:
        qApp = QApplication([])
    qApp.setAttribute(Qt.AA_Use96Dpi, True)

    def teardown():
        qApp.quit()

    request.addfinalizer(teardown)
    return qApp


class TestMainWindow:

    @pytest.fixture(autouse=True)
    def setup_method(self, app):
        self.window = MainWindow()
        self.app = app
        self.functionInput = self.window.functionInput
        self.xmin = self.window.xMinInput
        self.xmax = self.window.xMaxInput
        self.btn = self.window.plotButton

    def test_plot_generation(self):
        self.functionInput.setText("x^2")
        self.xmin.setValue(-5)
        self.xmax.setValue(5)

        QTest.mouseClick(self.btn, Qt.LeftButton)

        print(self.window.plotArea)

    def test_min_max_validation(self):
        self.xmin.setValue(30)
        self.xmax.setValue(20)

        QTest.mouseClick(self.btn, Qt.LeftButton)

        error_text = self.window.error_dialog.text().lower()

        assert "range start must be less than range end" in error_text


    def test_invalid_function(self):
        self.functionInput.setText("x**")

        QTest.mouseClick(self.btn, Qt.LeftButton)


        error_text = self.window.error_dialog.text()
        assert "Parsing Error" in error_text


    def test_default_function_and_range(self):
        QTest.mouseClick(self.window.button1, Qt.LeftButton)

        assert self.window.axes.lines

    def test_function_error_message(self):
        self.functionInput.setText("x**2 +")

        QTest.mouseClick(self.btn, Qt.LeftButton)

        error_text = self.window.error_dialog.text()
        assert "Parsing Error" in error_text

    
    def test_empty_function_entry(self):
        self.window.min.setValue(-10)
        self.window.max.setValue(10)

        self.window.function.setText("")

        QTest.mouseClick(self.window.button1, Qt.LeftButton)

        assert "Parsing Error" in self.window.error_dialog.text()

    def test_valid_function_with_zero_range(self):
        self.window.function.setText("x**2")

        self.window.min.setValue(0)
        self.window.max.setValue(0)

        QTest.mouseClick(self.window.button1, Qt.LeftButton)

        assert self.window.axes.lines




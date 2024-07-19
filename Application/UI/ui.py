# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(605, 492)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 641, 501))
        self.widget.setStyleSheet(u"background-color:black;\n"
"")
        self.widget565 = QWidget(self.widget)
        self.widget565.setObjectName(u"widget565")
        self.widget565.setGeometry(QRect(0, 0, 601, 781))
        self.widget565.setStyleSheet(u"background-color: black")
        self.groupBox = QGroupBox(self.widget565)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 310, 581, 171))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.functionInput = QLineEdit(self.groupBox)
        self.functionInput.setObjectName(u"functionInput")
        self.functionInput.setMinimumSize(QSize(434, 30))
        self.functionInput.setStyleSheet(u"background-color: #0f0f0f;\n"
"color: white;\n"
"border-width: 2px;\n"
"\n"
"border-style: outset;\n"
"border-radius: 10px;\n"
"border-color: red")
        self.functionInput.setMaxLength(64)
        self.functionInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.functionInput.setReadOnly(False)

        self.horizontalLayout.addWidget(self.functionInput)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.xMinInput = QLineEdit(self.groupBox)
        self.xMinInput.setObjectName(u"xMinInput")
        self.xMinInput.setStyleSheet(u"border-color:red;\n"
"border-top: none;\n"
"border-left:none;\n"
"border-right:none;\n"
"color:white;\n"
"border-width: 2px;\n"
"border-style: outset")
        self.xMinInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.xMinInput)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:white;\n"
"font-weight: bold;\n"
"font-size: 20px")

        self.horizontalLayout_2.addWidget(self.label)

        self.xMaxInput = QLineEdit(self.groupBox)
        self.xMaxInput.setObjectName(u"xMaxInput")
        self.xMaxInput.setStyleSheet(u"border-color:red;\n"
"border-top: none;\n"
"border-left:none;\n"
"border-right:none;\n"
"color:white;\n"
"border-width: 2px;\n"
"border-style: outset")
        self.xMaxInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.xMaxInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.plotButton = QPushButton(self.groupBox)
        self.plotButton.setObjectName(u"plotButton")
        self.plotButton.setMinimumSize(QSize(87, 0))
        self.plotButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.plotButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 100, 255), stop:1 rgba(255, 0, 0, 255));\n"
"\n"
"border-color:red;\n"
"border-style: outset;\n"
"border-width:0.5px;\n"
"border-radius: 5px;\n"
"\n"
"padding: 5px;\n"
"color: black;\n"
"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.plotButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.widget565)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 0, 81, 70))
        self.label_2.setStyleSheet(u"color:white;\n"
"font-weight: bold;\n"
"font-size: 20px")
        self.verticalLayoutWidget = QWidget(self.widget565)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 60, 571, 241))
        self.plotArea = QVBoxLayout(self.verticalLayoutWidget)
        self.plotArea.setObjectName(u"plotArea")
        self.plotArea.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.functionInput.setText(QCoreApplication.translate("MainWindow", u"X^2 * sqrt(X)", None))
        self.functionInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"f(x)", None))
        self.xMinInput.setText(QCoreApplication.translate("MainWindow", u"-20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>&lt; X &lt;</p></body></html>", None))
        self.xMaxInput.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.plotButton.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Dezmoz</p></body></html>", None))
    # retranslateUi


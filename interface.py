# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton_2 = QRadioButton(self.widget_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.chk_by_set = QRadioButton(self.widget_4)
        self.chk_by_set.setObjectName(u"chk_by_set")

        self.horizontalLayout_2.addWidget(self.chk_by_set)


        self.verticalLayout_2.addWidget(self.widget_4, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_filter = QLineEdit(self.widget_3)
        self.line_filter.setObjectName(u"line_filter")

        self.horizontalLayout.addWidget(self.line_filter, 0, Qt.AlignTop)

        self.pb_search = QPushButton(self.widget_3)
        self.pb_search.setObjectName(u"pb_search")

        self.horizontalLayout.addWidget(self.pb_search, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_add_card = QPushButton(self.widget_5)
        self.pb_add_card.setObjectName(u"pb_add_card")

        self.horizontalLayout_4.addWidget(self.pb_add_card)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.horizontalLayout_3.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.list_search_result = QListWidget(self.centralwidget)
        self.list_search_result.setObjectName(u"list_search_result")

        self.horizontalLayout_3.addWidget(self.list_search_result)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout_3.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Search by name", None))
        self.chk_by_set.setText(QCoreApplication.translate("MainWindow", u"Search by set", None))
        self.pb_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pb_add_card.setText(QCoreApplication.translate("MainWindow", u"Add Pokemon Card", None))
    # retranslateUi


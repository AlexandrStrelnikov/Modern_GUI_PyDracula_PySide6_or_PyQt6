# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import json
from matplotlib import pyplot as plt
import numpy as np
import pyqtgraph as pg

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        self.setGeometry(300, 200, 1400, 800)

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Фотон-Био вер. ХХХ"
        description = ""
        # APPLY TEXTS
        self.setWindowTitle(title)
        # widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_anamnes.clicked.connect(self.buttonClick)
        widgets.btn_visits.clicked.connect(self.buttonClick)
        widgets.btn_diagnostics.clicked.connect(self.buttonClick)
        widgets.btn_logout.clicked.connect(self.buttonClick)
        widgets.btn_login.clicked.connect(self.buttonClick)

        widgets.inspectionButton.clicked.connect(self.buttonClick)
        widgets.spectroscopyButton.clicked.connect(self.buttonClick)
        widgets.USIButton.clicked.connect(self.buttonClick)
        widgets.diagnosticsResultsButton.clicked.connect(self.buttonClick)

        widgets.redactAnamnesButton.clicked.connect(self.buttonClick)
        widgets.cancelAnamnesButton.clicked.connect(self.buttonClick)
        widgets.saveAnamnesButton.clicked.connect(self.buttonClick)

        widgets.isCycleRadioBox.clicked.connect(self.cycleDayClick)


        # widgets.illnesHistoryText.setEnabled(False)
        # widgets.ECONumSpinBox.setEnabled(False)
        # widgets.IGHComboBox.setEnabled(False)

        # Try page wigets
        # widgets.pushButton_3.clicked.connect(self.buttonClick)
        # widgets.labelVersion_5.setText('')
        # graph_widget = pg.GraphicsLayoutWidget(show=True)
        # graph_widget.setBackground(background=Settings.PLOT_BACKGROUND) # setting up graph background color
        # plot_widget = graph_widget.addPlot(title="Updating plot")
        # # plot_widget.enableAutoRange('xy', True)
        # plot_widget.autoRange()
        #
        #
        # global plot
        # plot = plot_widget.plot(pen='y')
        # plot.setPen(Settings.PLOT_LINE_COLOR[1]) # setting up line properties (here color only)
        # widgets.graph_layout.addWidget(graph_widget)


        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        widgets.btn_logout.clicked.connect(openCloseRightBox)
        widgets.btn_message.clicked.connect(openCloseRightBox)
        widgets.btn_print.clicked.connect(openCloseRightBox)
        widgets.btn_reconnect.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        themeFile = "themes\pb_theme.qss"
        # themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS охуенный блядь хак
            # Они изменяют класс Settings
            # после вызова (предыдущая строка) и переназначают атрибуты класса Settings.
            # (!) Не проебитесь на этом моменте
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.autorisation_page)
        self.buttouEnable(False)
        self.setUserInformation(name='',
                          lastname='',
                          midlename='',
                          birthday='',
                          cardnumber='')
        self.resetUserLineEdit()

    def buttouEnable(self, status):
        # for left menu buttons only
        widgets.btn_anamnes.setEnabled(status)
        widgets.btn_visits.setEnabled(status)
        widgets.btn_diagnostics.setEnabled(status)
        widgets.toggleButton.setEnabled(status)
        widgets.settingsTopBtn.setEnabled(status)

    def setUserInformation(self, name, lastname, midlename, birthday, cardnumber):
        widgets.nameMidleNameLabel.setText(name + ' ' + midlename)
        widgets.lastNameLabel.setText(lastname)
        widgets.ageLabel.setText(birthday)
        widgets.cartNLabel.setText(cardnumber)

    def resetUserLineEdit(self):
        widgets.nameLlineEdit.setText(''),
        widgets.surnameLineEdit.setText(''),
        widgets.middlenameLineEdit.setText(''),
        # widgets.birthdateLineEdit.setText(''),
        widgets.cardLineEdit.setText('')

    def cycleDayClick(self):
        btn = self.sender()
        widgets.cycleDaySpinBox.setEnabled(not(btn.isChecked()))
        widgets.cycleDaySpinBox.setValue(0)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "btn_anamnes":
            widgets.stackedWidget.setCurrentWidget(widgets.anamnes)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_visits":
            widgets.stackedWidget.setCurrentWidget(widgets.visits)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_diagnostics":
            widgets.stackedWidget.setCurrentWidget(widgets.diagnostics) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "inspectionButton":
            widgets.diagnosticStackedWidget.setCurrentWidget(widgets.inspectionPage) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "spectroscopyButton":
            widgets.diagnosticStackedWidget.setCurrentWidget(widgets.spectroscopyPage) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "USIButton":
            widgets.diagnosticStackedWidget.setCurrentWidget(widgets.USIPage) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "diagnosticsResultsButton":
            widgets.diagnosticStackedWidget.setCurrentWidget(widgets.resultsPage) # SET PAGE
            # UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            # btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_logout":
            widgets.stackedWidget.setCurrentWidget(widgets.autorisation_page)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            UIFunctions.resetMenu(self)
            self.buttouEnable(False)
            self.setUserInformation(name='',
                                    lastname='',
                                    midlename='',
                                    birthday='',
                                    cardnumber='')
            self.resetUserLineEdit()

        if btnName == "btn_login":
            widgets.stackedWidget.setCurrentWidget(widgets.anamnes)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            widgets.btn_anamnes.setStyleSheet(UIFunctions.selectMenu(widgets.btn_anamnes.styleSheet()))

            self.buttouEnable(True)

            self.setUserInformation(name=widgets.nameLlineEdit.text(),
                                    lastname=widgets.surnameLineEdit.text(),
                                    midlename=widgets.middlenameLineEdit.text(),
                                    birthday=widgets.birthdateLineEdit.text(),
                                    cardnumber=widgets.cardLineEdit.text())
            self.resetUserLineEdit()


        if btnName == "pushButton_3" :
            openFileName = widgets.lineEdit_3.text()

            try:
                with open(openFileName, 'r') as file:
                    freq, I, Q = json.load(file)
                    freq = np.array(freq)
                    I = np.array(I)
                    Q = np.array(Q)
                # plot.setData(x=[], y=[])
                plot.setData(x=freq, y=np.sqrt(I**2 + Q**2))
                widgets.labelVersion_5.setText('')
            except FileNotFoundError:
                plot.setData(x=[], y=[])
                widgets.labelVersion_5.setText('File Not Found')
            # widgets.graph_layout.update() # не знаю, нужна ли эта строчка вообще

        if btnName == "redactAnamnesButton":
            widgets.stackedWidget_2.setCurrentWidget(widgets.anamnesSavePage)
            widgets.illnesHistoryText.setEnabled(True)
            widgets.ECONumSpinBox.setEnabled(True)
            widgets.IGHComboBox.setEnabled(True)

        if btnName == "cancelAnamnesButton":
            widgets.stackedWidget_2.setCurrentWidget(widgets.anamnesRedactioPage)
            widgets.illnesHistoryText.setEnabled(False)
            widgets.ECONumSpinBox.setEnabled(False)
            widgets.IGHComboBox.setEnabled(False)

            widgets.illnesHistoryText.setText('')
            widgets.ECONumSpinBox.setText('')
            widgets.IGHComboBox.SelectedValue(1)


        if btnName == "saveAnamnesButton":
            widgets.stackedWidget_2.setCurrentWidget(widgets.anamnesRedactioPage)
            widgets.illnesHistoryText.setEnabled(False)
            widgets.ECONumSpinBox.setEnabled(False)
            widgets.IGHComboBox.setEnabled(False)
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())

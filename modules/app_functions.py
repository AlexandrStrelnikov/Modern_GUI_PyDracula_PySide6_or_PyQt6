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

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #37B5A7;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #37B5A7;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(55,181,167,255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #37B5A7;
        color : #ffffff;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #FFFFFF;")
        # self.ui.lineEdit_3.setStyleSheet("background-color: #FFFFFF;")
        self.ui.pushButton.setStyleSheet("background-color: #37B5A7;")
        # self.ui.pushButton_3.setStyleSheet("background-color: #37B5A7;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #FFFFFF;")

        # здесь настраиваются скроллеры
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #F2F2F2; } QScrollBar:horizontal { background: #F2F2F2; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #F2F2F2; } QScrollBar:horizontal { background: #F2F2F2; }")
        self.ui.comboBox.setStyleSheet("background-color: #FFFFFF;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #F2F2F2;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #F2F2F2;")
        # self.ui.commandLinkButton.setStyleSheet("color: #000000;")
        # todo проблема с фоновыми цветами решается, если явно указать область, к которой относятся те или иные кнопки. Все эти костыли надо исправить при работе начисто

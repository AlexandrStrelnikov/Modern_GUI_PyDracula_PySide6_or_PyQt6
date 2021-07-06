# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainCPwotW.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 652)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.toggleButton = QPushButton(self.topLogoInfo)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setGeometry(QRect(0, 0, 60, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setFocusPolicy(Qt.NoFocus)
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-right.png);")

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_anamnes = QPushButton(self.topMenu)
        self.btn_anamnes.setObjectName(u"btn_anamnes")
        sizePolicy.setHeightForWidth(self.btn_anamnes.sizePolicy().hasHeightForWidth())
        self.btn_anamnes.setSizePolicy(sizePolicy)
        self.btn_anamnes.setMinimumSize(QSize(0, 45))
        self.btn_anamnes.setFont(font)
        self.btn_anamnes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_anamnes.setFocusPolicy(Qt.NoFocus)
        self.btn_anamnes.setLayoutDirection(Qt.LeftToRight)
        self.btn_anamnes.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-clipboard.png);")

        self.verticalLayout_8.addWidget(self.btn_anamnes)

        self.btn_visits = QPushButton(self.topMenu)
        self.btn_visits.setObjectName(u"btn_visits")
        sizePolicy.setHeightForWidth(self.btn_visits.sizePolicy().hasHeightForWidth())
        self.btn_visits.setSizePolicy(sizePolicy)
        self.btn_visits.setMinimumSize(QSize(0, 45))
        self.btn_visits.setFont(font)
        self.btn_visits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visits.setFocusPolicy(Qt.NoFocus)
        self.btn_visits.setLayoutDirection(Qt.LeftToRight)
        self.btn_visits.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-history.png);")

        self.verticalLayout_8.addWidget(self.btn_visits)

        self.btn_diagnostics = QPushButton(self.topMenu)
        self.btn_diagnostics.setObjectName(u"btn_diagnostics")
        sizePolicy.setHeightForWidth(self.btn_diagnostics.sizePolicy().hasHeightForWidth())
        self.btn_diagnostics.setSizePolicy(sizePolicy)
        self.btn_diagnostics.setMinimumSize(QSize(0, 45))
        self.btn_diagnostics.setFont(font)
        self.btn_diagnostics.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_diagnostics.setFocusPolicy(Qt.NoFocus)
        self.btn_diagnostics.setLayoutDirection(Qt.LeftToRight)
        self.btn_diagnostics.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart.png);")

        self.verticalLayout_8.addWidget(self.btn_diagnostics)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 2, -1, 2)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.lastNameLabel = QLabel(self.leftBox)
        self.lastNameLabel.setObjectName(u"lastNameLabel")

        self.verticalLayout_21.addWidget(self.lastNameLabel)

        self.nameMidleNameLabel = QLabel(self.leftBox)
        self.nameMidleNameLabel.setObjectName(u"nameMidleNameLabel")

        self.verticalLayout_21.addWidget(self.nameMidleNameLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_2 = QSpacerItem(250, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(4)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, 0, -1)
        self.cartNLabel = QLabel(self.leftBox)
        self.cartNLabel.setObjectName(u"cartNLabel")

        self.verticalLayout_22.addWidget(self.cartNLabel)

        self.ageLabel = QLabel(self.leftBox)
        self.ageLabel.setObjectName(u"ageLabel")

        self.verticalLayout_22.addWidget(self.ageLabel)


        self.horizontalLayout_3.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.leftBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.settingsTopBtn.setFocusPolicy(Qt.NoFocus)
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setFocusPolicy(Qt.NoFocus)
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.anamnes = QWidget()
        self.anamnes.setObjectName(u"anamnes")
        self.verticalLayout_25 = QVBoxLayout(self.anamnes)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(18, 18, 18, 18)
        self.illnesHistoryLabel = QLabel(self.anamnes)
        self.illnesHistoryLabel.setObjectName(u"illnesHistoryLabel")

        self.verticalLayout_25.addWidget(self.illnesHistoryLabel)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.scrollArea_2 = QScrollArea(self.anamnes)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 92, 87))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.illnesHistoryText = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.illnesHistoryText.setObjectName(u"illnesHistoryText")
        self.illnesHistoryText.setFrameShape(QFrame.StyledPanel)
        self.illnesHistoryText.setLineWidth(1)

        self.verticalLayout_24.addWidget(self.illnesHistoryText)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_6.addWidget(self.scrollArea_2)


        self.verticalLayout_25.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_4)

        self.ECONumLabel = QLabel(self.anamnes)
        self.ECONumLabel.setObjectName(u"ECONumLabel")

        self.verticalLayout_25.addWidget(self.ECONumLabel)

        self.ECONumSpinBox = QSpinBox(self.anamnes)
        self.ECONumSpinBox.setObjectName(u"ECONumSpinBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ECONumSpinBox.sizePolicy().hasHeightForWidth())
        self.ECONumSpinBox.setSizePolicy(sizePolicy2)
        self.ECONumSpinBox.setMinimumSize(QSize(200, 30))
        self.ECONumSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_25.addWidget(self.ECONumSpinBox)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_3)

        self.IGHLabel = QLabel(self.anamnes)
        self.IGHLabel.setObjectName(u"IGHLabel")

        self.verticalLayout_25.addWidget(self.IGHLabel)

        self.IGHComboBox = QComboBox(self.anamnes)
        self.IGHComboBox.addItem("")
        self.IGHComboBox.addItem("")
        self.IGHComboBox.setObjectName(u"IGHComboBox")
        sizePolicy2.setHeightForWidth(self.IGHComboBox.sizePolicy().hasHeightForWidth())
        self.IGHComboBox.setSizePolicy(sizePolicy2)
        self.IGHComboBox.setMinimumSize(QSize(200, 30))

        self.verticalLayout_25.addWidget(self.IGHComboBox)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_5)

        self.stackedWidget_2 = QStackedWidget(self.anamnes)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy3)
        self.anamnesRedactioPage = QWidget()
        self.anamnesRedactioPage.setObjectName(u"anamnesRedactioPage")
        self.verticalLayout_26 = QVBoxLayout(self.anamnesRedactioPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(300, 9, 300, -1)
        self.redactAnamnesButton = QPushButton(self.anamnesRedactioPage)
        self.redactAnamnesButton.setObjectName(u"redactAnamnesButton")

        self.verticalLayout_26.addWidget(self.redactAnamnesButton)

        self.stackedWidget_2.addWidget(self.anamnesRedactioPage)
        self.anamnesSavePage = QWidget()
        self.anamnesSavePage.setObjectName(u"anamnesSavePage")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.anamnesSavePage.sizePolicy().hasHeightForWidth())
        self.anamnesSavePage.setSizePolicy(sizePolicy4)
        self.horizontalLayout_7 = QHBoxLayout(self.anamnesSavePage)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, -1, 9, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.saveAnamnesButton = QPushButton(self.anamnesSavePage)
        self.saveAnamnesButton.setObjectName(u"saveAnamnesButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.saveAnamnesButton.sizePolicy().hasHeightForWidth())
        self.saveAnamnesButton.setSizePolicy(sizePolicy5)
        self.saveAnamnesButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_7.addWidget(self.saveAnamnesButton)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.cancelAnamnesButton = QPushButton(self.anamnesSavePage)
        self.cancelAnamnesButton.setObjectName(u"cancelAnamnesButton")
        sizePolicy5.setHeightForWidth(self.cancelAnamnesButton.sizePolicy().hasHeightForWidth())
        self.cancelAnamnesButton.setSizePolicy(sizePolicy5)
        self.cancelAnamnesButton.setMinimumSize(QSize(120, 30))

        self.horizontalLayout_7.addWidget(self.cancelAnamnesButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.stackedWidget_2.addWidget(self.anamnesSavePage)

        self.verticalLayout_25.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.anamnes)
        self.autorisation_page = QWidget()
        self.autorisation_page.setObjectName(u"autorisation_page")
        self.verticalLayout_23 = QVBoxLayout(self.autorisation_page)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(18, 18, 18, 18)
        self.verticalFrame = QFrame(self.autorisation_page)
        self.verticalFrame.setObjectName(u"verticalFrame")
        sizePolicy3.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy3)
        self.verticalLayout_14 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(150, 160, 150, 1)
        self.surnameLineEdit = QLineEdit(self.verticalFrame)
        self.surnameLineEdit.setObjectName(u"surnameLineEdit")
        self.surnameLineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.surnameLineEdit)

        self.nameLlineEdit = QLineEdit(self.verticalFrame)
        self.nameLlineEdit.setObjectName(u"nameLlineEdit")
        self.nameLlineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.nameLlineEdit)

        self.middlenameLineEdit = QLineEdit(self.verticalFrame)
        self.middlenameLineEdit.setObjectName(u"middlenameLineEdit")
        self.middlenameLineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.middlenameLineEdit)

        self.birthdateLineEdit = QDateEdit(self.verticalFrame)
        self.birthdateLineEdit.setObjectName(u"birthdateLineEdit")
        self.birthdateLineEdit.setMinimumSize(QSize(0, 30))
        self.birthdateLineEdit.setCalendarPopup(True)
        self.birthdateLineEdit.setCurrentSectionIndex(0)

        self.verticalLayout_14.addWidget(self.birthdateLineEdit)

        self.cardLineEdit = QLineEdit(self.verticalFrame)
        self.cardLineEdit.setObjectName(u"cardLineEdit")
        self.cardLineEdit.setMinimumSize(QSize(0, 30))

        self.verticalLayout_14.addWidget(self.cardLineEdit)

        self.horizontalFrame = QFrame(self.verticalFrame)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy3.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sqlStatusLabel = QLabel(self.horizontalFrame)
        self.sqlStatusLabel.setObjectName(u"sqlStatusLabel")
        sizePolicy4.setHeightForWidth(self.sqlStatusLabel.sizePolicy().hasHeightForWidth())
        self.sqlStatusLabel.setSizePolicy(sizePolicy4)
        self.sqlStatusLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_17.addWidget(self.sqlStatusLabel)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_14)

        self.btn_registration = QPushButton(self.horizontalFrame)
        self.btn_registration.setObjectName(u"btn_registration")
        sizePolicy5.setHeightForWidth(self.btn_registration.sizePolicy().hasHeightForWidth())
        self.btn_registration.setSizePolicy(sizePolicy5)
        self.btn_registration.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_17.addWidget(self.btn_registration)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_13)

        self.btn_login = QPushButton(self.horizontalFrame)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy2.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy2)
        self.btn_login.setMinimumSize(QSize(100, 30))
        self.btn_login.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_17.addWidget(self.btn_login)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_15)


        self.verticalLayout_14.addWidget(self.horizontalFrame)


        self.verticalLayout_23.addWidget(self.verticalFrame)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)

        self.stackedWidget.addWidget(self.autorisation_page)
        self.visits = QWidget()
        self.visits.setObjectName(u"visits")
        self.visits.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.visits)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(18, 18, 18, 18)
        self.row_1 = QFrame(self.visits)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.visits)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")
        self.radioButton.setAutoExclusive(False)

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon5)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.visits)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.visits)
        self.diagnostics = QWidget()
        self.diagnostics.setObjectName(u"diagnostics")
        self.verticalLayout_20 = QVBoxLayout(self.diagnostics)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.diagnosticButtonsFrame = QFrame(self.diagnostics)
        self.diagnosticButtonsFrame.setObjectName(u"diagnosticButtonsFrame")
        sizePolicy3.setHeightForWidth(self.diagnosticButtonsFrame.sizePolicy().hasHeightForWidth())
        self.diagnosticButtonsFrame.setSizePolicy(sizePolicy3)
        self.horizontalLayout_8 = QHBoxLayout(self.diagnosticButtonsFrame)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.inspectionButton = QPushButton(self.diagnosticButtonsFrame)
        self.inspectionButton.setObjectName(u"inspectionButton")
        sizePolicy5.setHeightForWidth(self.inspectionButton.sizePolicy().hasHeightForWidth())
        self.inspectionButton.setSizePolicy(sizePolicy5)
        self.inspectionButton.setMinimumSize(QSize(160, 60))
        self.inspectionButton.setFocusPolicy(Qt.NoFocus)
        self.inspectionButton.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inspectionButton.setIcon(icon6)
        self.inspectionButton.setIconSize(QSize(16, 16))
        self.inspectionButton.setAutoDefault(False)
        self.inspectionButton.setFlat(False)

        self.horizontalLayout_8.addWidget(self.inspectionButton)

        self.spectroscopyButton = QPushButton(self.diagnosticButtonsFrame)
        self.spectroscopyButton.setObjectName(u"spectroscopyButton")
        sizePolicy5.setHeightForWidth(self.spectroscopyButton.sizePolicy().hasHeightForWidth())
        self.spectroscopyButton.setSizePolicy(sizePolicy5)
        self.spectroscopyButton.setMinimumSize(QSize(160, 60))
        self.spectroscopyButton.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_8.addWidget(self.spectroscopyButton)

        self.USIButton = QPushButton(self.diagnosticButtonsFrame)
        self.USIButton.setObjectName(u"USIButton")
        sizePolicy5.setHeightForWidth(self.USIButton.sizePolicy().hasHeightForWidth())
        self.USIButton.setSizePolicy(sizePolicy5)
        self.USIButton.setMinimumSize(QSize(160, 60))
        self.USIButton.setFocusPolicy(Qt.NoFocus)
        self.USIButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.USIButton)

        self.diagnosticsResultsButton = QPushButton(self.diagnosticButtonsFrame)
        self.diagnosticsResultsButton.setObjectName(u"diagnosticsResultsButton")
        sizePolicy5.setHeightForWidth(self.diagnosticsResultsButton.sizePolicy().hasHeightForWidth())
        self.diagnosticsResultsButton.setSizePolicy(sizePolicy5)
        self.diagnosticsResultsButton.setMinimumSize(QSize(160, 60))
        self.diagnosticsResultsButton.setFocusPolicy(Qt.NoFocus)
        self.diagnosticsResultsButton.setAcceptDrops(False)
        self.diagnosticsResultsButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.diagnosticsResultsButton)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_20.addWidget(self.diagnosticButtonsFrame)

        self.diagnosticStackedWidget = QStackedWidget(self.diagnostics)
        self.diagnosticStackedWidget.setObjectName(u"diagnosticStackedWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.diagnosticStackedWidget.sizePolicy().hasHeightForWidth())
        self.diagnosticStackedWidget.setSizePolicy(sizePolicy7)
        self.diagnosticStackedWidget.setMinimumSize(QSize(0, 0))
        self.beginDiagnosticPage = QWidget()
        self.beginDiagnosticPage.setObjectName(u"beginDiagnosticPage")
        self.horizontalLayout_18 = QHBoxLayout(self.beginDiagnosticPage)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.beginDiagnosticButton = QPushButton(self.beginDiagnosticPage)
        self.beginDiagnosticButton.setObjectName(u"beginDiagnosticButton")
        sizePolicy5.setHeightForWidth(self.beginDiagnosticButton.sizePolicy().hasHeightForWidth())
        self.beginDiagnosticButton.setSizePolicy(sizePolicy5)
        self.beginDiagnosticButton.setMinimumSize(QSize(300, 30))

        self.horizontalLayout_18.addWidget(self.beginDiagnosticButton)

        self.diagnosticStackedWidget.addWidget(self.beginDiagnosticPage)
        self.inspectionPage = QWidget()
        self.inspectionPage.setObjectName(u"inspectionPage")
        self.verticalLayout_27 = QVBoxLayout(self.inspectionPage)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(18, 18, 18, 18)
        self.inspectionDatTimeLabel = QLabel(self.inspectionPage)
        self.inspectionDatTimeLabel.setObjectName(u"inspectionDatTimeLabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.inspectionDatTimeLabel.sizePolicy().hasHeightForWidth())
        self.inspectionDatTimeLabel.setSizePolicy(sizePolicy8)
        self.inspectionDatTimeLabel.setMidLineWidth(0)

        self.verticalLayout_27.addWidget(self.inspectionDatTimeLabel)

        self.dateTimeEdit = QDateTimeEdit(self.inspectionPage)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy2.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy2)
        self.dateTimeEdit.setMinimumSize(QSize(150, 30))
        self.dateTimeEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_27.addWidget(self.dateTimeEdit)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_27.addItem(self.verticalSpacer)

        self.cycleDayLabel = QLabel(self.inspectionPage)
        self.cycleDayLabel.setObjectName(u"cycleDayLabel")
        sizePolicy8.setHeightForWidth(self.cycleDayLabel.sizePolicy().hasHeightForWidth())
        self.cycleDayLabel.setSizePolicy(sizePolicy8)

        self.verticalLayout_27.addWidget(self.cycleDayLabel)

        self.cycleDaySpinBox = QSpinBox(self.inspectionPage)
        self.cycleDaySpinBox.setObjectName(u"cycleDaySpinBox")
        sizePolicy2.setHeightForWidth(self.cycleDaySpinBox.sizePolicy().hasHeightForWidth())
        self.cycleDaySpinBox.setSizePolicy(sizePolicy2)
        self.cycleDaySpinBox.setMinimumSize(QSize(100, 30))
        self.cycleDaySpinBox.setSizeIncrement(QSize(0, 30))
        self.cycleDaySpinBox.setValue(0)

        self.verticalLayout_27.addWidget(self.cycleDaySpinBox)

        self.isCycleRadioBox = QRadioButton(self.inspectionPage)
        self.isCycleRadioBox.setObjectName(u"isCycleRadioBox")
        self.isCycleRadioBox.setMinimumSize(QSize(0, 40))
        self.isCycleRadioBox.setFocusPolicy(Qt.NoFocus)
        self.isCycleRadioBox.setChecked(False)

        self.verticalLayout_27.addWidget(self.isCycleRadioBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)

        self.diagnosticStackedWidget.addWidget(self.inspectionPage)
        self.spectroscopyPage = QWidget()
        self.spectroscopyPage.setObjectName(u"spectroscopyPage")
        self.verticalLayout_28 = QVBoxLayout(self.spectroscopyPage)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(18, 18, 18, 18)
        self.spinBox = QSpinBox(self.spectroscopyPage)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_28.addWidget(self.spinBox)

        self.diagnosticStackedWidget.addWidget(self.spectroscopyPage)
        self.USIPage = QWidget()
        self.USIPage.setObjectName(u"USIPage")
        self.verticalLayout_29 = QVBoxLayout(self.USIPage)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.USIscrollArea = QScrollArea(self.USIPage)
        self.USIscrollArea.setObjectName(u"USIscrollArea")
        self.USIscrollArea.setFrameShape(QFrame.NoFrame)
        self.USIscrollArea.setWidgetResizable(True)
        self.USIscrollAreaWidget = QWidget()
        self.USIscrollAreaWidget.setObjectName(u"USIscrollAreaWidget")
        self.USIscrollAreaWidget.setGeometry(QRect(0, 0, 634, 832))
        sizePolicy8.setHeightForWidth(self.USIscrollAreaWidget.sizePolicy().hasHeightForWidth())
        self.USIscrollAreaWidget.setSizePolicy(sizePolicy8)
        self.verticalLayout_31 = QVBoxLayout(self.USIscrollAreaWidget)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.MECHOlabel = QLabel(self.USIscrollAreaWidget)
        self.MECHOlabel.setObjectName(u"MECHOlabel")
        sizePolicy8.setHeightForWidth(self.MECHOlabel.sizePolicy().hasHeightForWidth())
        self.MECHOlabel.setSizePolicy(sizePolicy8)

        self.verticalLayout_31.addWidget(self.MECHOlabel)

        self.MECHOframe = QFrame(self.USIscrollAreaWidget)
        self.MECHOframe.setObjectName(u"MECHOframe")
        sizePolicy8.setHeightForWidth(self.MECHOframe.sizePolicy().hasHeightForWidth())
        self.MECHOframe.setSizePolicy(sizePolicy8)
        self.horizontalLayout_10 = QHBoxLayout(self.MECHOframe)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, -1, -1, -1)
        self.spinBox_2 = QSpinBox(self.MECHOframe)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(120, 30))
        self.spinBox_2.setWrapping(False)
        self.spinBox_2.setFrame(True)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setProperty("showGroupSeparator", False)
        self.spinBox_2.setMaximum(1000)

        self.horizontalLayout_10.addWidget(self.spinBox_2)

        self.label_2 = QLabel(self.MECHOframe)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)


        self.verticalLayout_31.addWidget(self.MECHOframe)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)

        self.structureLabel = QLabel(self.USIscrollAreaWidget)
        self.structureLabel.setObjectName(u"structureLabel")

        self.verticalLayout_31.addWidget(self.structureLabel)

        self.structureFrame = QFrame(self.USIscrollAreaWidget)
        self.structureFrame.setObjectName(u"structureFrame")
        sizePolicy4.setHeightForWidth(self.structureFrame.sizePolicy().hasHeightForWidth())
        self.structureFrame.setSizePolicy(sizePolicy4)
        self.structureFrame.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_13 = QHBoxLayout(self.structureFrame)
        self.horizontalLayout_13.setSpacing(30)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(10, -1, 1, -1)
        self.structuredButton = QRadioButton(self.structureFrame)
        self.structuredButton.setObjectName(u"structuredButton")
        self.structuredButton.setMinimumSize(QSize(0, 40))
        self.structuredButton.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.structuredButton)

        self.notStructuredButton = QRadioButton(self.structureFrame)
        self.notStructuredButton.setObjectName(u"notStructuredButton")
        self.notStructuredButton.setMinimumSize(QSize(0, 40))
        self.notStructuredButton.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.notStructuredButton)

        self.partlyStructuredButton = QRadioButton(self.structureFrame)
        self.partlyStructuredButton.setObjectName(u"partlyStructuredButton")
        self.partlyStructuredButton.setMinimumSize(QSize(0, 40))
        self.partlyStructuredButton.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_13.addWidget(self.partlyStructuredButton)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)


        self.verticalLayout_31.addWidget(self.structureFrame)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_7)

        self.phaseCoincidenceLabel = QLabel(self.USIscrollAreaWidget)
        self.phaseCoincidenceLabel.setObjectName(u"phaseCoincidenceLabel")

        self.verticalLayout_31.addWidget(self.phaseCoincidenceLabel)

        self.phaseCoincidenceFrame = QFrame(self.USIscrollAreaWidget)
        self.phaseCoincidenceFrame.setObjectName(u"phaseCoincidenceFrame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.phaseCoincidenceFrame.sizePolicy().hasHeightForWidth())
        self.phaseCoincidenceFrame.setSizePolicy(sizePolicy9)
        self.phaseCoincidenceFrame.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.phaseCoincidenceFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(30)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(10, -1, -1, -1)
        self.earlySecretoryPhaseButton = QRadioButton(self.phaseCoincidenceFrame)
        self.earlySecretoryPhaseButton.setObjectName(u"earlySecretoryPhaseButton")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.earlySecretoryPhaseButton.sizePolicy().hasHeightForWidth())
        self.earlySecretoryPhaseButton.setSizePolicy(sizePolicy10)
        self.earlySecretoryPhaseButton.setMinimumSize(QSize(0, 40))
        self.earlySecretoryPhaseButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.earlySecretoryPhaseButton, 1, 1, 1, 1)

        self.latePolyferativePhaseButton = QRadioButton(self.phaseCoincidenceFrame)
        self.latePolyferativePhaseButton.setObjectName(u"latePolyferativePhaseButton")
        self.latePolyferativePhaseButton.setMinimumSize(QSize(0, 40))
        self.latePolyferativePhaseButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.latePolyferativePhaseButton, 6, 0, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.earlyPolyferativePhaseButton = QRadioButton(self.phaseCoincidenceFrame)
        self.earlyPolyferativePhaseButton.setObjectName(u"earlyPolyferativePhaseButton")
        self.earlyPolyferativePhaseButton.setMinimumSize(QSize(0, 40))
        self.earlyPolyferativePhaseButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.earlyPolyferativePhaseButton, 1, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.lateSecretoryPhaseButton = QRadioButton(self.phaseCoincidenceFrame)
        self.lateSecretoryPhaseButton.setObjectName(u"lateSecretoryPhaseButton")
        self.lateSecretoryPhaseButton.setMinimumSize(QSize(0, 40))
        self.lateSecretoryPhaseButton.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.lateSecretoryPhaseButton, 6, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 6, 2, 1, 1)


        self.verticalLayout_31.addWidget(self.phaseCoincidenceFrame)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_8)

        self.organicChangesLabel = QLabel(self.USIscrollAreaWidget)
        self.organicChangesLabel.setObjectName(u"organicChangesLabel")

        self.verticalLayout_31.addWidget(self.organicChangesLabel)

        self.organicChangesFrame = QFrame(self.USIscrollAreaWidget)
        self.organicChangesFrame.setObjectName(u"organicChangesFrame")
        self.organicChangesFrame.setMinimumSize(QSize(0, 100))
        self.gridLayout_4 = QGridLayout(self.organicChangesFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(30)
        self.gridLayout_4.setContentsMargins(10, -1, -1, -1)
        self.checkBox_3 = QCheckBox(self.organicChangesFrame)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(0, 40))
        self.checkBox_3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_3, 2, 0, 1, 1)

        self.checkBox_6 = QCheckBox(self.organicChangesFrame)
        self.checkBox_6.setObjectName(u"checkBox_6")
        sizePolicy2.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy2)
        self.checkBox_6.setMinimumSize(QSize(0, 40))
        self.checkBox_6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_6, 1, 2, 1, 1)

        self.checkBox_4 = QCheckBox(self.organicChangesFrame)
        self.checkBox_4.setObjectName(u"checkBox_4")
        sizePolicy2.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy2)
        self.checkBox_4.setMinimumSize(QSize(0, 40))
        self.checkBox_4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_4, 2, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.organicChangesFrame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        sizePolicy2.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy2)
        self.checkBox_2.setMinimumSize(QSize(0, 40))
        self.checkBox_2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.organicChangesFrame)
        self.checkBox_5.setObjectName(u"checkBox_5")
        sizePolicy2.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy2)
        self.checkBox_5.setMinimumSize(QSize(0, 40))
        self.checkBox_5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_5, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 2, 3, 1, 1)

        self.checkBox_7 = QCheckBox(self.organicChangesFrame)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setMinimumSize(QSize(0, 40))
        self.checkBox_7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.checkBox_7, 2, 2, 1, 1)


        self.verticalLayout_31.addWidget(self.organicChangesFrame)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_31.addItem(self.verticalSpacer_9)

        self.OvaryFrame = QFrame(self.USIscrollAreaWidget)
        self.OvaryFrame.setObjectName(u"OvaryFrame")
        sizePolicy8.setHeightForWidth(self.OvaryFrame.sizePolicy().hasHeightForWidth())
        self.OvaryFrame.setSizePolicy(sizePolicy8)
        self.OvaryFrame.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_14 = QHBoxLayout(self.OvaryFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.leftOvaryFrame = QFrame(self.OvaryFrame)
        self.leftOvaryFrame.setObjectName(u"leftOvaryFrame")
        sizePolicy4.setHeightForWidth(self.leftOvaryFrame.sizePolicy().hasHeightForWidth())
        self.leftOvaryFrame.setSizePolicy(sizePolicy4)
        self.leftOvaryFrame.setMinimumSize(QSize(0, 0))
        self.verticalLayout_32 = QVBoxLayout(self.leftOvaryFrame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.leftOvaryLabel = QLabel(self.leftOvaryFrame)
        self.leftOvaryLabel.setObjectName(u"leftOvaryLabel")
        sizePolicy8.setHeightForWidth(self.leftOvaryLabel.sizePolicy().hasHeightForWidth())
        self.leftOvaryLabel.setSizePolicy(sizePolicy8)

        self.verticalLayout_32.addWidget(self.leftOvaryLabel)

        self.leftYellowBodyFrame = QFrame(self.leftOvaryFrame)
        self.leftYellowBodyFrame.setObjectName(u"leftYellowBodyFrame")
        self.horizontalLayout_15 = QHBoxLayout(self.leftYellowBodyFrame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(10, -1, 1, -1)
        self.label_3 = QLabel(self.leftYellowBodyFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy8.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy8)

        self.horizontalLayout_15.addWidget(self.label_3)

        self.leftYellowBodySiseSpinBox = QSpinBox(self.leftYellowBodyFrame)
        self.leftYellowBodySiseSpinBox.setObjectName(u"leftYellowBodySiseSpinBox")
        sizePolicy5.setHeightForWidth(self.leftYellowBodySiseSpinBox.sizePolicy().hasHeightForWidth())
        self.leftYellowBodySiseSpinBox.setSizePolicy(sizePolicy5)
        self.leftYellowBodySiseSpinBox.setMinimumSize(QSize(35, 30))
        self.leftYellowBodySiseSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_15.addWidget(self.leftYellowBodySiseSpinBox)

        self.label_5 = QLabel(self.leftYellowBodyFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy11)

        self.horizontalLayout_15.addWidget(self.label_5)


        self.verticalLayout_32.addWidget(self.leftYellowBodyFrame)

        self.leftDominanteFoliculCheckBox = QCheckBox(self.leftOvaryFrame)
        self.leftDominanteFoliculCheckBox.setObjectName(u"leftDominanteFoliculCheckBox")
        self.leftDominanteFoliculCheckBox.setMinimumSize(QSize(0, 40))
        self.leftDominanteFoliculCheckBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_32.addWidget(self.leftDominanteFoliculCheckBox)

        self.leftCystCheckBox = QCheckBox(self.leftOvaryFrame)
        self.leftCystCheckBox.setObjectName(u"leftCystCheckBox")
        self.leftCystCheckBox.setMinimumSize(QSize(0, 40))
        self.leftCystCheckBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_32.addWidget(self.leftCystCheckBox)


        self.horizontalLayout_14.addWidget(self.leftOvaryFrame)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.rightOvaryFrame = QFrame(self.OvaryFrame)
        self.rightOvaryFrame.setObjectName(u"rightOvaryFrame")
        self.verticalLayout_33 = QVBoxLayout(self.rightOvaryFrame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.rightOvaryLabel = QLabel(self.rightOvaryFrame)
        self.rightOvaryLabel.setObjectName(u"rightOvaryLabel")
        sizePolicy8.setHeightForWidth(self.rightOvaryLabel.sizePolicy().hasHeightForWidth())
        self.rightOvaryLabel.setSizePolicy(sizePolicy8)

        self.verticalLayout_33.addWidget(self.rightOvaryLabel)

        self.rightYellowBodyFrame = QFrame(self.rightOvaryFrame)
        self.rightYellowBodyFrame.setObjectName(u"rightYellowBodyFrame")
        self.horizontalLayout_16 = QHBoxLayout(self.rightYellowBodyFrame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, -1, -1, -1)
        self.label_4 = QLabel(self.rightYellowBodyFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy8.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy8)

        self.horizontalLayout_16.addWidget(self.label_4)

        self.rightYellowBodySiseSpinBox = QSpinBox(self.rightYellowBodyFrame)
        self.rightYellowBodySiseSpinBox.setObjectName(u"rightYellowBodySiseSpinBox")
        sizePolicy5.setHeightForWidth(self.rightYellowBodySiseSpinBox.sizePolicy().hasHeightForWidth())
        self.rightYellowBodySiseSpinBox.setSizePolicy(sizePolicy5)
        self.rightYellowBodySiseSpinBox.setMinimumSize(QSize(35, 30))
        self.rightYellowBodySiseSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_16.addWidget(self.rightYellowBodySiseSpinBox)

        self.label_6 = QLabel(self.rightYellowBodyFrame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy11.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy11)

        self.horizontalLayout_16.addWidget(self.label_6)


        self.verticalLayout_33.addWidget(self.rightYellowBodyFrame)

        self.rightDominanteFoliculCheckBox = QCheckBox(self.rightOvaryFrame)
        self.rightDominanteFoliculCheckBox.setObjectName(u"rightDominanteFoliculCheckBox")
        self.rightDominanteFoliculCheckBox.setMinimumSize(QSize(0, 40))
        self.rightDominanteFoliculCheckBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_33.addWidget(self.rightDominanteFoliculCheckBox)

        self.rightCystCheckBox = QCheckBox(self.rightOvaryFrame)
        self.rightCystCheckBox.setObjectName(u"rightCystCheckBox")
        self.rightCystCheckBox.setMinimumSize(QSize(0, 40))
        self.rightCystCheckBox.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_33.addWidget(self.rightCystCheckBox)


        self.horizontalLayout_14.addWidget(self.rightOvaryFrame)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)


        self.verticalLayout_31.addWidget(self.OvaryFrame)

        self.USIscrollArea.setWidget(self.USIscrollAreaWidget)

        self.verticalLayout_29.addWidget(self.USIscrollArea)

        self.diagnosticStackedWidget.addWidget(self.USIPage)
        self.resultsPage = QWidget()
        self.resultsPage.setObjectName(u"resultsPage")
        self.verticalLayout_30 = QVBoxLayout(self.resultsPage)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(18, 18, 18, 18)
        self.pushButton_2 = QPushButton(self.resultsPage)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setFocusPolicy(Qt.NoFocus)
        self.pushButton_2.setFlat(False)

        self.verticalLayout_30.addWidget(self.pushButton_2)

        self.diagnosticStackedWidget.addWidget(self.resultsPage)

        self.verticalLayout_20.addWidget(self.diagnosticStackedWidget)

        self.diagnosticsNavigationButtonsFrame = QFrame(self.diagnostics)
        self.diagnosticsNavigationButtonsFrame.setObjectName(u"diagnosticsNavigationButtonsFrame")
        self.horizontalLayout_19 = QHBoxLayout(self.diagnosticsNavigationButtonsFrame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.previousPageDiagnostic = QPushButton(self.diagnosticsNavigationButtonsFrame)
        self.previousPageDiagnostic.setObjectName(u"previousPageDiagnostic")
        self.previousPageDiagnostic.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_19.addWidget(self.previousPageDiagnostic)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_16)

        self.finishDiagnostics = QPushButton(self.diagnosticsNavigationButtonsFrame)
        self.finishDiagnostics.setObjectName(u"finishDiagnostics")
        self.finishDiagnostics.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_19.addWidget(self.finishDiagnostics)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.naexPageDiagnostic = QPushButton(self.diagnosticsNavigationButtonsFrame)
        self.naexPageDiagnostic.setObjectName(u"naexPageDiagnostic")
        self.naexPageDiagnostic.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_19.addWidget(self.naexPageDiagnostic)


        self.verticalLayout_20.addWidget(self.diagnosticsNavigationButtonsFrame)

        self.stackedWidget.addWidget(self.diagnostics)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.topMenus)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_reconnect = QPushButton(self.topMenus)
        self.btn_reconnect.setObjectName(u"btn_reconnect")
        sizePolicy.setHeightForWidth(self.btn_reconnect.sizePolicy().hasHeightForWidth())
        self.btn_reconnect.setSizePolicy(sizePolicy)
        self.btn_reconnect.setMinimumSize(QSize(0, 45))
        self.btn_reconnect.setFont(font)
        self.btn_reconnect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reconnect.setFocusPolicy(Qt.NoFocus)
        self.btn_reconnect.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_15.addWidget(self.btn_reconnect)

        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setFocusPolicy(Qt.NoFocus)
        self.btn_message.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_15.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setFocusPolicy(Qt.NoFocus)
        self.btn_print.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_15.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setFocusPolicy(Qt.NoFocus)
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_15.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(1)
        self.inspectionButton.setDefault(False)
        self.diagnosticStackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"\u0424\u043e\u0442\u043e\u043d-\u0411\u0438\u043e", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440. \u0425\u0425\u0425", None))
        self.btn_anamnes.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043c\u043d\u0435\u0437", None))
        self.btn_visits.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0438\u0442\u044b", None))
        self.btn_diagnostics.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText("")
        self.btn_adjustments.setText("")
        self.btn_more.setText("")
        self.textEdit.setMarkdown("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.nameMidleNameLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.cartNLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.ageLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Not connected", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.illnesHistoryLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0421\u0422\u041e\u0420\u0418\u042f \u0411\u041e\u041b\u0415\u0417\u041d\u0418", None))
        self.ECONumLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u041b\u0418\u0427\u0415\u0421\u0422\u0412\u041e \u041f\u0420\u041e\u0426\u0415\u0414\u0423\u0420 \u042d\u041a\u041e", None))
        self.IGHLabel.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0413\u0425", None))
        self.IGHComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0440\u043e\u0432\u043e\u0434\u0438\u043b\u043e\u0441\u044c", None))
        self.IGHComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u043e\u0434\u0438\u043b\u043e\u0441\u044c", None))

        self.redactAnamnesButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.saveAnamnesButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.cancelAnamnesButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.surnameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.nameLlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None))
        self.middlenameLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.birthdateLineEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/mm/yyyy", None))
        self.cardLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u0430\u0440\u0442\u044b", None))
        self.sqlStatusLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_registration.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.inspectionButton.setText(QCoreApplication.translate("MainWindow", u"1. \u041e\u0441\u043c\u043e\u0442\u0440", None))
        self.spectroscopyButton.setText(QCoreApplication.translate("MainWindow", u"2. \u0421\u043f\u0435\u043a\u0442\u0440\u043e\u0441\u043a\u043e\u043f\u0438\u044f", None))
        self.USIButton.setText(QCoreApplication.translate("MainWindow", u"3. \u0423\u0437\u0438", None))
        self.diagnosticsResultsButton.setText(QCoreApplication.translate("MainWindow", u"4.\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b\n"
"\u0438 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0430\u0446\u0438\u0438", None))
        self.beginDiagnosticButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c \u041f\u0420\u041e\u0426\u0415\u0414\u0423\u0420\u0423 \u0414\u0418\u0410\u0413\u041d\u041e\u0421\u0422\u0418\u041a\u0418", None))
        self.inspectionDatTimeLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410\u0422\u0410 \u0418 \u0412\u0420\u0415\u041c\u042f \u041e\u0421\u041c\u041e\u0422\u0420\u0410", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy h:mm", None))
        self.cycleDayLabel.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0415\u041d\u042c \u0426\u0418\u041a\u041b\u0410", None))
        self.isCycleRadioBox.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0418\u041a\u041b \u041e\u0422\u0421\u0423\u0422\u0421\u0422\u0412\u0423\u0415\u0422", None))
        self.MECHOlabel.setText(QCoreApplication.translate("MainWindow", u"\u041c-\u042d\u0425\u041e", None))
        self.spinBox_2.setSpecialValueText("")
        self.spinBox_2.setSuffix("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041c", None))
        self.structureLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0420\u0423\u041a\u0422\u0423\u0420\u0410", None))
        self.structuredButton.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439", None))
        self.notStructuredButton.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0435 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439", None))
        self.partlyStructuredButton.setText(QCoreApplication.translate("MainWindow", u"\u0447\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439", None))
        self.phaseCoincidenceLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u041e\u0422\u0412\u0415\u0422\u0421\u0422\u0412\u0418\u0415 \u0424\u0410\u0417\u0415 \u0426\u0418\u041a\u041b\u0410", None))
        self.earlySecretoryPhaseButton.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u043d\u043d\u044f\u044f \u0441\u0435\u043a\u0440\u0442\u043e\u0440\u043d\u0430\u044f \u0444\u0430\u0437\u0430", None))
        self.latePolyferativePhaseButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0437\u0434\u043d\u044f\u044f \u043f\u043e\u043b\u0438\u0444\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0444\u0430\u0437\u0430", None))
        self.earlyPolyferativePhaseButton.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0430\u043d\u043d\u044f\u044f \u043f\u043e\u043b\u0438\u0444\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u0430\u044f \u0444\u0430\u0437\u0430", None))
        self.lateSecretoryPhaseButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0437\u0434\u043d\u044f\u044f \u0441\u0435\u043a\u0440\u0442\u043e\u0440\u043d\u0430\u044f \u0444\u0430\u0437\u0430", None))
        self.organicChangesLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0420\u0413\u0410\u041d\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0418\u0417\u041c\u0415\u041d\u0415\u041d\u0418\u042f", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0437\u043b\u044b", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u043b\u0438\u043f", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0438\u0441\u0442\u043e\u0437\u043d\u044b\u0435 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0435\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u0430\u0434\u0435\u043d\u043e\u043c\u0438\u043e\u0437", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"\u0433\u0438\u043f\u0435\u0440\u043f\u043b\u0430\u0437\u0438\u044f", None))
        self.leftOvaryLabel.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0418\u0427\u041d\u0418\u041a (\u041b\u0415\u0412\u042b\u0419)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0436\u0435\u043b\u0442\u043e\u0435 \u0442\u0435\u043b\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041c", None))
        self.leftDominanteFoliculCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u043c\u0438\u043d\u0430\u043d\u0442\u043d\u044b\u0439 \u0444\u043e\u043b\u0438\u043a\u0443\u043b", None))
        self.leftCystCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0438\u0441\u0442\u0430 \u0436\u0435\u043b\u0442\u043e\u0433\u043e \u0442\u0435\u043b\u0430", None))
        self.rightOvaryLabel.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0418\u0427\u041d\u0418\u041a (\u041f\u0420\u0410\u0412\u042b\u0419)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0436\u0435\u043b\u0442\u043e\u0435 \u0442\u0435\u043b\u043e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u041c", None))
        self.rightDominanteFoliculCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u043c\u0438\u043d\u0430\u043d\u0442\u043d\u044b\u0439 \u0444\u043e\u043b\u0438\u043a\u0443\u043b", None))
        self.rightCystCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0438\u0441\u0442\u0430 \u0436\u0435\u043b\u0442\u043e\u0433\u043e \u0442\u0435\u043b\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.previousPageDiagnostic.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.finishDiagnostics.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0435\u0440\u0448\u0438\u0442\u044c", None))
        self.naexPageDiagnostic.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.btn_reconnect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi


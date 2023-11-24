# test tag -  v1.0.0
# titleSecond - объект QLabel - главный заголовок 'Программирование бинарного файла'
# shiftAddress - объект QLabel - просто подпись 'Адрес сдвига'
# recordSize - объект QLabel - просто подпись 'Размер записи/считывания'
# shiftAddress_txt - объект QPlainTextEdit - блок ввода текста для 'Адрес сдвига'
# recordSize_txt - объект QPlainTextEdit - блок ввода текста для 'Размер записи/считывания'
# verification - объект QPushButton - 'Верефикация'
# openingButton - объект QPushButton - 'Открыть...'
# saveButton - объект QPushButton - 'Сохранить'
# mainCommands - объект QVBoxLayout - группа кнопок для основных команд 'v', 'r', 'w', 'p'
# minorCommands - объект QVBoxLayout - группа кнопок для второстепенных команд 'GET', 'PUT' и тд
# buttonReadVersion - объект QPushButton - кнопка запрашивает версию FW 'Версия ПО FIRMWARE'
# buttonReadKey - объект QPushButton - кнопка для цикла чтения ключа 'Чтение ключа'
# buttonWriteKey - объект QPushButton - кнопка для цикла записи ключа 'Запись ключа'
# buttonWriteProtection - объект QPushButton - кнопка для цикла защита от записи 'Защита от записи'
# secondaryButtonsReading - объект QHBoxLayout - второстепенная группа кнопок для чтения ключа 'GET'
# secondaryButtonsRecording - объект QHBoxLayout - второстепенная группа кнопок для записи ключа 'PUT'
# secondaryButtonsProtection - объект QHBoxLayout - второстепенная группа кнопок для защиты от записи 'SETWP'
# FIRMWAREVersion - объект QLabel - если заглушка -> добавить в footer объект QLabel, иначе выводить версию FW
# buttonGET$ - объект QPushButton - кнопка для отправки данных на FW при чтении, $- порядковый номер, см. Приложение Б
# buttonPUT$ - объект QPushButton - кнопка для отправки данных на FW при записи, $- порядковый номер, см. Приложение Б
# button(SETWP)/(RESWP) - объект QPushButton - кнопка для отправки данных на FW при защите, см. Приложение Б
# footerListVersion - объект QHBoxLayout - группа либо содержит версии и GUI, и FW, либо только версию GUI
# GUIVersion - объект QLabel - для отображения версии GUI 'GUI version 0.0'
# operationStatus - объект QLabel - для отображения статуса операции 'СТАТУС'

from PyQt6 import QtCore, QtGui, QtWidgets
import git

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(790, 625)
        style_file = QtCore.QFile("styleForProgBiFi.css")
        style_file.open(QtCore.QIODevice.OpenModeFlag.ReadOnly | QtCore.QIODevice.OpenModeFlag.Text)
        style_sheet = style_file.readAll().data().decode("utf-8")
        style_file.close()
        MainWindow.setStyleSheet(style_sheet)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        MainWindow.setFont(font)
        self.globalWrapper = QtWidgets.QWidget(parent=MainWindow)
        self.globalWrapper.setObjectName("globalWrapper")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.globalWrapper)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainBlock = QtWidgets.QWidget(parent=self.globalWrapper)
        self.mainBlock.setMinimumSize(QtCore.QSize(0, 100))
        self.mainBlock.setMaximumSize(QtCore.QSize(16777215, 100))
        self.mainBlock.setObjectName("mainBlock")
        self.gridLayout = QtWidgets.QGridLayout(self.mainBlock)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.recordSize_txt = QtWidgets.QPlainTextEdit(parent=self.mainBlock)
        self.recordSize_txt.setMaximumSize(QtCore.QSize(16777215, 27))
        self.recordSize_txt.setObjectName("recordSize_txt")
        self.gridLayout.addWidget(self.recordSize_txt, 2, 1, 1, 1)
        self.shiftAddress_txt = QtWidgets.QPlainTextEdit(parent=self.mainBlock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shiftAddress_txt.sizePolicy().hasHeightForWidth())
        self.shiftAddress_txt.setSizePolicy(sizePolicy)
        self.shiftAddress_txt.setMaximumSize(QtCore.QSize(16777215, 27))
        self.shiftAddress_txt.setStyleSheet("")
        self.shiftAddress_txt.setObjectName("shiftAddress_txt")
        self.gridLayout.addWidget(self.shiftAddress_txt, 1, 1, 1, 1)
        self.recordSize = QtWidgets.QLabel(parent=self.mainBlock)
        self.recordSize.setObjectName("recordSize")
        self.gridLayout.addWidget(self.recordSize, 2, 0, 1, 1)
        self.shiftAddress = QtWidgets.QLabel(parent=self.mainBlock)
        self.shiftAddress.setObjectName("shiftAddress")
        self.gridLayout.addWidget(self.shiftAddress, 1, 0, 1, 1)
        self.titleSecond = QtWidgets.QLabel(parent=self.mainBlock)
        self.titleSecond.setMinimumSize(QtCore.QSize(0, 27))
        self.titleSecond.setMaximumSize(QtCore.QSize(16777215, 16777212))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.titleSecond.setFont(font)
        self.titleSecond.setObjectName("titleSecond")
        self.gridLayout.addWidget(self.titleSecond, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.mainBlock)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.mainButtons = QtWidgets.QGridLayout()
        self.mainButtons.setObjectName("mainButtons")
        self.verification = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.verification.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.verification.setObjectName("verification")
        self.mainButtons.addWidget(self.verification, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(161, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.mainButtons.addItem(spacerItem1, 0, 2, 2, 1)
        self.openingButton = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.openingButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.openingButton.setObjectName("openingButton")
        self.mainButtons.addWidget(self.openingButton, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.saveButton.setObjectName("saveButton")
        self.mainButtons.addWidget(self.saveButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.mainButtons)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.executiveButtons = QtWidgets.QHBoxLayout()
        self.executiveButtons.setObjectName("executiveButtons")
        self.mainCommands = QtWidgets.QVBoxLayout()
        self.mainCommands.setObjectName("mainCommands")
        self.buttonReadVersion = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonReadVersion.setMinimumSize(QtCore.QSize(190, 0))
        self.buttonReadVersion.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonReadVersion.setObjectName("buttonReadVersion")
        self.mainCommands.addWidget(self.buttonReadVersion)
        self.buttonReadKey = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonReadKey.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonReadKey.setObjectName("buttonReadKey")
        self.mainCommands.addWidget(self.buttonReadKey)
        self.buttonWriteKey = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonWriteKey.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonWriteKey.setObjectName("buttonWriteKey")
        self.mainCommands.addWidget(self.buttonWriteKey)
        self.buttonWriteProtection = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonWriteProtection.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonWriteProtection.setObjectName("buttonWriteProtection")
        self.mainCommands.addWidget(self.buttonWriteProtection)
        self.executiveButtons.addLayout(self.mainCommands)
        spacerItem3 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.executiveButtons.addItem(spacerItem3)
        self.minorCommands = QtWidgets.QVBoxLayout()
        self.minorCommands.setObjectName("minorCommands")
        self.FIRMWAREVersion = QtWidgets.QLabel(parent=self.globalWrapper)
        self.FIRMWAREVersion.setObjectName("FIRMWAREVersion")
        self.minorCommands.addWidget(self.FIRMWAREVersion)
        self.secondaryButtonsReading = QtWidgets.QHBoxLayout()
        self.secondaryButtonsReading.setObjectName("secondaryButtonsReading")
        self.buttonGET1 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonGET1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonGET1.setObjectName("buttonGET1")
        self.secondaryButtonsReading.addWidget(self.buttonGET1)
        self.buttonGET2 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonGET2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonGET2.setObjectName("buttonGET2")
        self.secondaryButtonsReading.addWidget(self.buttonGET2)
        self.buttonGET3 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonGET3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonGET3.setObjectName("buttonGET3")
        self.secondaryButtonsReading.addWidget(self.buttonGET3)
        self.minorCommands.addLayout(self.secondaryButtonsReading)
        self.secondaryButtonsRecording = QtWidgets.QHBoxLayout()
        self.secondaryButtonsRecording.setObjectName("secondaryButtonsRecording")
        self.buttonPUT1 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonPUT1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonPUT1.setObjectName("buttonPUT1")
        self.secondaryButtonsRecording.addWidget(self.buttonPUT1)
        self.buttonPUT2 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonPUT2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonPUT2.setObjectName("buttonPUT2")
        self.secondaryButtonsRecording.addWidget(self.buttonPUT2)
        self.buttonPUT3 = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonPUT3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonPUT3.setObjectName("buttonPUT3")
        self.secondaryButtonsRecording.addWidget(self.buttonPUT3)
        self.minorCommands.addLayout(self.secondaryButtonsRecording)
        self.secondaryButtonsProtection = QtWidgets.QHBoxLayout()
        self.secondaryButtonsProtection.setObjectName("secondaryButtonsProtection")
        self.buttonRESWP = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonRESWP.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonRESWP.setObjectName("buttonRESWP")
        self.secondaryButtonsProtection.addWidget(self.buttonRESWP)
        self.buttonSETWP = QtWidgets.QPushButton(parent=self.globalWrapper)
        self.buttonSETWP.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buttonSETWP.setObjectName("buttonSETWP")
        self.secondaryButtonsProtection.addWidget(self.buttonSETWP)
        self.minorCommands.addLayout(self.secondaryButtonsProtection)
        self.executiveButtons.addLayout(self.minorCommands)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.executiveButtons.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.executiveButtons)
        spacerItem5 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem5)
        self.footer = QtWidgets.QHBoxLayout()
        self.footer.setObjectName("footer")
        self.operationStatus = QtWidgets.QLabel(parent=self.globalWrapper)
        self.operationStatus.setObjectName("operationStatus")
        self.footer.addWidget(self.operationStatus)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.footer.addItem(spacerItem6)
        self.footerListVersion = QtWidgets.QHBoxLayout()
        self.footerListVersion.setObjectName("footerListVersion")
        self.GUIVersion = QtWidgets.QLabel(parent=self.globalWrapper)
        self.GUIVersion.setObjectName("GUIVersion")
        self.footerListVersion.addWidget(self.GUIVersion)
        self.footer.addLayout(self.footerListVersion)
        self.verticalLayout.addLayout(self.footer)
        MainWindow.setCentralWidget(self.globalWrapper)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.recordSize.setText(_translate("MainWindow", "Размер записи/считывания"))
        self.shiftAddress.setText(_translate("MainWindow", "Адрес сдвига"))
        self.titleSecond.setText(_translate("MainWindow", "Программирование бинарного файла"))
        self.verification.setText(_translate("MainWindow", "Верефикация"))
        self.openingButton.setText(_translate("MainWindow", "Открыть..."))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.buttonReadVersion.setText(_translate("MainWindow", "Версия ПО FIRMWARE"))
        self.buttonReadVersion.setShortcut(_translate("MainWindow", "V"))
        self.buttonReadKey.setText(_translate("MainWindow", "Чтение ключа"))
        self.buttonReadKey.setShortcut(_translate("MainWindow", "R"))
        self.buttonWriteKey.setText(_translate("MainWindow", "Запись ключа"))
        self.buttonWriteKey.setShortcut(_translate("MainWindow", "W"))
        self.buttonWriteProtection.setText(_translate("MainWindow", "Защита от записи"))
        self.buttonWriteProtection.setShortcut(_translate("MainWindow", "P"))
        self.FIRMWAREVersion.setText(_translate("MainWindow", "Заглушка ну или тут будет отображаться версия FW"))
        self.buttonGET1.setText(_translate("MainWindow", "GET1"))
        self.buttonGET2.setText(_translate("MainWindow", "GET2"))
        self.buttonGET3.setText(_translate("MainWindow", "GET3"))
        self.buttonPUT1.setText(_translate("MainWindow", "PUT1"))
        self.buttonPUT2.setText(_translate("MainWindow", "PUT2"))
        self.buttonPUT3.setText(_translate("MainWindow", "PUT3"))
        self.buttonRESWP.setText(_translate("MainWindow", "RESWP"))
        self.buttonSETWP.setText(_translate("MainWindow", "SETWP"))
        self.operationStatus.setText(_translate("MainWindow", "СТАТУС"))
        self.GUIVersion.setText(_translate("MainWindow", f"FIRMWARE {version()}"))

def version():
    g = git.cmd.Git()
    blob = g.ls_remote('https://github.com/Rooplok/project', sort='-v:refname', tags=True)
    return blob.split('\n')[0].split('/')[-1]

def checkVersion():
    newText = version()
    ui.GUIVersion.setText(f"FIRMWARE {newText}")
    return

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.buttonReadVersion.clicked.connect(checkVersion)
    sys.exit(app.exec())

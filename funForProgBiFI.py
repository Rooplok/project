# shiftAddress - объект QLabel - просто подпись 'Адрес сдвига'
# recordSize - объект QLabel - просто подпись 'Размер записи/считывания'
import struct
import responder
from progBiFi import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QComboBox, QMessageBox
import sys, re, binascii
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

crc32 = -1
flag_to_get = False #НАДО ДОРАБОТАТЬ ФЛАГ (ЕСЛИ ФЛАГ FALSE ТО ВТОРОСТЕПЕННЫЕ КНОПКИ НЕ ДОЛЖНЫ РАБОТАТЬ)



def save_file():
    global crc32
    print('Зашли в сохранение')
    if check_content():
        print('Зашли в чек контент')
        verifi()
        data = read_value()
        result = ''

        for el in data:
            result = result + el + ', '
        print('Вывели переменную')
        result += str(crc32)
        print(result)

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]

            with open(selected_file, 'w') as file:
                file.write(result)

def read_value():
    print('Зашли в рид')
    shiftAddress = ui.shiftAddress_txt.toPlainText()
    recordSize = ui.recordSize_txt.toPlainText()

    list = [shiftAddress, recordSize]
    print(list)
    return list

def verifi():
    global crc32
    print('Зашли в верифи')
    data = read_value()
    print('После дата верифи')
    crc32_checksum = 0xFFFFFFFF

    for line in data:
        crc32_checksum = binascii.crc32(line.encode('utf-8'), crc32_checksum)

    crc32_checksum ^= 0xFFFFFFFF
    crc32 = crc32_checksum

    #     QMessageBox.information(None, 'Информация', "Верефикация пройдена успешно")
    #     QMessageBox.information(None, 'Информация', "Верефикация пройдена не успешно")

def open_file():
    print('зашли в openFromFile')
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    if file_dialog.exec():
        print('зашли в условие openFromFile')
        selected_file = file_dialog.selectedFiles()[0]
        with open(selected_file, 'r') as file:
            data = file.read()

        QMessageBox.information(None, "Ключ открыт", data)
        matches = data.split(', ')

        myList = [match for match in matches]
        write_data(myList)
        verifi()
        if crc32 != int(myList[2]):
            print(crc32)
            QMessageBox.information(None, 'Информация', "Верефикация пройдена не успешно")

def write_data(my_list):
    ui.shiftAddress_txt.setPlainText(my_list[0])
    ui.recordSize_txt.setPlainText(my_list[1])

def check_content():
    print('Зашли в чек контент')
    list = read_value()
    index = 0
    flag = 0
    while index < 2:
        print(list[index])
        if list[index] == '' or not list[index].isdigit():
            return False
        index += 1
    return True

def reading_version():
    print(responder.V())


def reading_key(kls):
    global flag_to_get
    responsered_key = kls()
    ui.operationStatus.setText(responsered_key.key())
    # Запаковываем данные
    # Отправляем в функцию crc32
    peremennaya = read_value()
    peremennaya_2 = responsered_key.crc32(int(peremennaya[0]),int(peremennaya[1]))
    peremennaya_3 = struct.pack("!II", int(peremennaya[0]), int(peremennaya[1]))
    crc32_data = struct.unpack("!I", peremennaya_2)[0]
    if crc32_data == binascii.crc32(peremennaya_3) & 0xFFFFFFFF:
        flag_to_get = True
    else:
        print('Не прошли проверку')

def get(name_function):
    responder_get = responder.R()
    peremenaya_get1 = getattr(responder_get, name_function)
    peremenaya_kakaya = peremenaya_get1()
    data = peremenaya_kakaya[:-4]
    crc32_data = struct.unpack("!I", peremenaya_kakaya[-4:])[0]
    ui.operationStatus.setText(data.decode('utf-8'))
    print(data)
    print(crc32_data)

def put():
    responder_put = responder.W()
    peremenaya_put1 = responder_put.put(ui.shiftAddress_txt.toPlainText().encode('utf-8'))
    print(peremenaya_put1)

def protection_key():
    responsered_key = responder.P()
    ui.operationStatus.setText(responsered_key.key())

def set_res_wp(klx):
    responsered_setwp = responder.P()
    ui.operationStatus.setText(responsered_setwp.protection(klx))


# Включение всех кнопок из группы

# buttonGET1 = ui.buttonGET1
# buttonGET2 = ui.buttonGET2
# buttonGET3 = ui.buttonGET3
#
# button_group = ui.minorCommands()
# button_group.addButton(buttonGET1, 1)
# button_group.addButton(buttonGET2, 2)
# button_group.addButton(buttonGET3, 3)
def enable_buttons():
    set_buttons_state(True)

def disable_buttons(button_id):
    for button in button_group.buttons():
        if button.id() != button_id:
            button.setEnabled(False)
            button.setStyleSheet("background-color: gray;")
        else:
            button.setEnabled(True)
            button.setStyleSheet("background-color: #317AA4;"
                                 "color: #69B7E5")

def set_buttons_state(state):
    for button in button_group.buttons():
        button.setEnabled(state)
        button.setStyleSheet("background-color: gray;")

ui.buttonWriteKey.clicked.connect(enable_buttons)
button_group.clicked[int].connect(disable_buttons)

set_buttons_state(False)

ui.buttonSETWP.clicked.connect(lambda: set_res_wp('SETWP'))
ui.buttonRESWP.clicked.connect(lambda: set_res_wp('RESWP'))
ui.buttonWriteProtection.clicked.connect(protection_key)
ui.buttonGET1.clicked.connect(lambda: get('get1'))
ui.buttonGET2.clicked.connect(lambda: get('get2'))
ui.buttonGET3.clicked.connect(lambda: get('get3'))
ui.buttonWriteKey.clicked.connect(lambda: reading_key(responder.R))
ui.buttonReadKey.clicked.connect(lambda: reading_key(responder.W))
ui.buttonPUT1.clicked.connect(put)
ui.buttonReadVersion.clicked.connect(reading_version)
ui.openingButton.clicked.connect(open_file)
ui.saveButton.clicked.connect(save_file)
ui.verification.clicked.connect(verifi)

sys.exit(app.exec())

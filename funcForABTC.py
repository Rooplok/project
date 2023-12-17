from ABTC import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QComboBox, QMessageBox
import sys, re, binascii
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def save_file():
    print('Зашли в сохранение')
    if check_content():
        print('Зашли в чек контент')
        verifi()
        check_sum = ui.crc32_txt.text()
        data = read_value()
        result = ''

        for el in data:
            result = result + el + ', '
        print('Вывели переменную')
        result += check_sum

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()[0]

            with open(selected_file, 'w') as file:
                file.write(result)

def read_value():
    print('Зашли в рид')
    module_type = ui.module_txt.currentText()
    module_number = ui.system_num_txt.toPlainText()
    station_number = ui.station_num_txt.toPlainText()
    path_number = ui.way_num_txt.toPlainText()
    rack_number = ui.rack_num_txt.toPlainText()
    crate_number = ui.crate_num_txt.toPlainText()
    crate_place = ui.crate_place_txt.toPlainText()
    rec_code_1 = ui.rec_code1_txt.toPlainText()
    rec_code_2 = ui.rec_code2_txt.toPlainText()
    rec_code_3 = ui.rec_code3_txt.toPlainText()
    rec_code_4 = ui.rec_code4_txt.toPlainText()
    list = [module_type, module_number, station_number, path_number, rack_number, crate_number, crate_place, rec_code_1,
            rec_code_2, rec_code_3, rec_code_4]
    print(list)
    return list

def verifi():
    print('Зашли в верифи')
    data = read_value()
    print('После дата верифи')
    crc32_checksum = 0xFFFFFFFF

    for line in data:
        crc32_checksum = binascii.crc32(line.encode('utf-8'), crc32_checksum)

    crc32_checksum ^= 0xFFFFFFFF

    ui.crc32_txt.setText(str(crc32_checksum))
    print('Вывели переменную')

# QMessageBox.information(None, 'Информация', "Верефикация пройдена не успешно")
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
        if ui.crc32_txt.text() != myList[11]:
            print(ui.crc32_txt.text())
            QMessageBox.information(None, 'Информация', "Верефикация пройдена не успешно")


def write_data(my_list):
    ui.module_txt.setCurrentIndex(ui.module_txt.findText(my_list[0]))
    ui.system_num_txt.setPlainText(my_list[1])
    ui.station_num_txt.setPlainText(my_list[2])
    ui.way_num_txt.setPlainText(my_list[3])
    ui.rack_num_txt.setPlainText(my_list[4])
    ui.crate_num_txt.setPlainText(my_list[5])
    ui.crate_place_txt.setPlainText(my_list[6])
    ui.rec_code1_txt.setPlainText(my_list[7])
    ui.rec_code2_txt.setPlainText(my_list[8])
    ui.rec_code3_txt.setPlainText(my_list[9])
    ui.rec_code4_txt.setPlainText(my_list[10])
    ui.crc32_txt.setText(my_list[11])

def check_content():
    print('Зашли в чек контент')
    list = read_value()
    index = 0
    flag = 0
    while index < 11:
        print(list[index])
        if list[index] != '':
            if index == 0:
                if list[index] == '':
                    QMessageBox.information(None, 'Информация', 'Обязательно выберите тип модуля')
                    return False
            elif index == 2:
                if int(list[index]) > 65535 or int(list[index]) < 0:
                    QMessageBox.information(None, 'Информация',
                                            'Ошибка: значение в поле № станции не в диапазоне от 0 до 65535')
                    return False
            elif int(list[index]) > 255 or int(list[index]) < 0:
                QMessageBox.information(None, 'Информация', f'Ошибка: значение в поле {index} не в диапазоне от 0 до 255')
                return False
        else:
            return False
        index += 1
    return True

ui.openingButton.clicked.connect(open_file)
ui.saveButton.clicked.connect(save_file)
ui.verification.clicked.connect(verifi)

sys.exit(app.exec())

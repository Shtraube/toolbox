import os
import sys
import keyboard
import shutil
import pyautogui as pg
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog,
                               QMessageBox, QSystemTrayIcon, QMenu)
from PySide6.QtGui import QAction, QIcon
from UI.ui_mainwindow import Ui_MainWindow


x, y = pg.size()
X_DEFAULT = x // 2
Y_DEFAULT = y // 2
KEYS_DEFAULT = 'Alt+1'
basedir = os.path.dirname(__file__) + '/icons'


def file_name_change(root_path: str, curr_path: str,
                     file_name: str, file_ext: str) -> str:
    """Функция, генерирующая новое имя файла."""
    counter = 1
    test_name = (root_path + '/' + file_ext + '/' + file_name + str(counter)
                 + '.' + file_ext)
    while True:
        if os.path.exists(test_name):
            counter += 1
            test_name = (root_path + '/' + file_ext + '/'
                         + file_name + str(counter) + '.' + file_ext)
        else:
            new_name = (curr_path + '/' + file_name
                        + str(counter) + '.' + file_ext)
            break
    return new_name


def sort_files(start_dir: str, second_dir='') -> bool:
    """Функция, производящая сортировку файлов."""
    new_dirs = {}
    root_dir = start_dir
    if second_dir:
        start_dir = second_dir

    if not os.access(start_dir, os.R_OK | os.W_OK | os.X_OK):
        return False

    current_files = [file for file in os.listdir(start_dir)
                     if os.path.isfile(os.path.join(start_dir, file))]
    current_dirs = [dir for dir in os.listdir(start_dir)
                    if os.path.isdir(os.path.join(start_dir, dir))]

    for file in current_files:
        f_name_split = file.rsplit('.', 1)
        curr_extension = f_name_split[-1] if len(f_name_split) > 1 else 'OTHER'
        root_destination = os.path.join(root_dir, curr_extension)
        if curr_extension not in new_dirs:
            new_dirs[curr_extension] = root_destination
            if not os.path.exists(root_destination):
                os.mkdir(new_dirs[curr_extension])
        if not os.path.exists(os.path.join(root_dir, curr_extension, file)):
            shutil.move(os.path.join(start_dir, file), root_destination)
        else:
            new_file_name = file_name_change(root_dir, start_dir,
                                             f_name_split[0], curr_extension)
            os.rename(os.path.join(start_dir, file), new_file_name)
            shutil.move(new_file_name, root_destination)

    for dir in current_dirs:
        dir_path = os.path.join(start_dir, dir)
        sort_files(root_dir, dir_path)
        os.rmdir(dir_path)

    return True


class Settings:
    """Класс, управляющий чтением и записью настроек."""
    def __init__(self):
        """Конструктор класса."""
        self.read_settings()

    def read_settings(self):
        """Метод, отвечающий за чтение настроек из файла json."""
        try:
            with open('hsettings.json', 'r') as hsettings:
                sett_list = json.load(hsettings)
                if sett_list.get('x_position') is None:
                    self.set_default()
                else:
                    self.x_position = sett_list['x_position']
                    self.y_position = sett_list['y_position']
                    self.keys = sett_list['keys']
        except FileNotFoundError:
            self.set_default()

    def write_settings(self):
        """Метод, отвечающий за перезапись настроек в файл."""
        positions = {
                'x_position': self.x_position,
                'y_position': self.y_position,
                'keys': self.keys
            }
        with open('hsettings.json', 'w') as hsettings:
            json.dump(positions, hsettings, indent=4)

    def set_default(self):
        """Метод, восстанавливающий настройки по умолчанию."""
        self.x_position = X_DEFAULT
        self.y_position = Y_DEFAULT
        self.keys = KEYS_DEFAULT


class MouseMover:
    """Класс, управляющий курсором мыши."""
    def __init__(self):
        """Конструктор класса."""

    def move_mouse(self, x_position, y_position):
        """Перемещение указателя мыши в указанные координаты."""
        pg.moveTo(x_position, y_position)


class MainWindow(QMainWindow):
    """Класс главного окна приложения."""
    def __init__(self, parent=None):
        """Конструктор класса."""
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Ящик')
        self.setWindowIcon(QIcon(os.path.join(basedir,
                                 'wooden-box-label.ico')))

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(os.path.join(basedir,
                                     'wooden-box-label.ico')))
        self.tray_menu = QMenu()
        exit_action = QAction('Закрыть приложение', self)
        exit_action.triggered.connect(self.quit)
        self.tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.activate)

        self.ui.pushButton.clicked.connect(self.quit)
        self.ui.toolButton.clicked.connect(self.choose_dir)
        # self.ui.toolButton.setShortcut('Ctrl+Alt+Left')
        self.ui.pushButton_2.clicked.connect(self.file_sort)

        self.my_settings = Settings()
        self.mover = MouseMover()
        self.mover.move_mouse(self.my_settings.x_position,
                              self.my_settings.y_position)

        self.ui.spinBox.setValue(self.my_settings.x_position)
        self.ui.spinBox_2.setValue(self.my_settings.y_position)
        self.ui.spinBox.valueChanged.connect(self.update_settings)
        self.ui.spinBox_2.valueChanged.connect(self.update_settings)
        self.ui.keySequenceEdit.setKeySequence(self.my_settings.keys)
        self.ui.keySequenceEdit.keySequenceChanged.connect(
                                                self.update_settings)

        self._global_keyPressEvent()

    def _global_keyPressEvent(self):
        """Метод обработки нажатия комбинации клавиш."""
        keyboard.add_hotkey(self.my_settings.keys,
                            lambda: self.mover.move_mouse(
                                self.my_settings.x_position,
                                self.my_settings.y_position))

    def update_settings(self):
        """Метод обновления полей класса, хранящих настройки."""
        self.my_settings.keys = (self.ui.keySequenceEdit.
                                 keySequence().toString())
        self.my_settings.x_position = self.ui.spinBox.value()
        self.my_settings.y_position = self.ui.spinBox_2.value()
        keyboard.clear_all_hotkeys()
        keyboard.add_hotkey(self.my_settings.keys,
                            lambda: self.mover.move_mouse(
                                self.my_settings.x_position,
                                self.my_settings.y_position))

    def choose_dir(self):
        """Метод выбора директории для упорядочивания."""
        folder_path = QFileDialog.getExistingDirectory(self,
                                                       caption='', dir='')
        self.ui.lineEdit.setText(folder_path)

    def file_sort(self):
        """Метод, запускающий сортировку файлов."""
        if self.ui.lineEdit.text():
            result = sort_files(self.ui.lineEdit.text())
            if result:
                QMessageBox.information(self, 'Задача выполнена',
                                        'Сортировка и перенос файлов по'
                                        ' адресу '
                                        f'{self.ui.lineEdit.text()}'
                                        ' завершены.')
                self.ui.lineEdit.setText('')
            else:
                QMessageBox.information(self, 'Задача не выполнена',
                                        'Сортировка и перенос файлов по'
                                        ' адресу '
                                        f'{self.ui.lineEdit.text()}'
                                        ' запрещены правами доступа.')

    def quit(self):
        """Метод выхода из приложения."""
        button = QMessageBox.question(self, 'Выход из приложения',
                                      'Вы действительно хотите выйти?')
        if button == QMessageBox.Yes:
            self.my_settings.write_settings()
            self.tray_icon.hide()
            QApplication.quit()

    def closeEvent(self, event):
        """Метод обработки закрытия главного окна приложения."""
        # Прячем вместо закрытия: можно опустить, если не нужно сообщение
        event.ignore()
        self.hide()
        self.tray_icon.showMessage(
            'System Tray',
            'Приложение свёрнуто в трей.',
            QSystemTrayIcon.MessageIcon.Information,
            2000
        )

    def activate(self, reason):
        """Метод восстановления главного окна из системного трея."""
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.showNormal()
                self.activateWindow()


def main():
    """Главная функция приложения, создание и запуск главного окна."""
    app = QApplication()
    app.setWindowIcon(QIcon(os.path.join(basedir, 'wooden-box-label.ico')))
    app.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

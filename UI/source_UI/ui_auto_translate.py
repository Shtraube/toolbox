import os
import re


def translate_ui_to_py(path: str):
    files = os.listdir(path)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for file in files:
        if pattern.match(file):
            ui_list.append(file)

    for file in ui_list:
        file_path = os.path.join(path, file)
        file_name = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} > {path}{os.sep}{file_name}.py'
        os.popen(cmd)


if __name__ == '__main__':
    translate_ui_to_py(os.path.dirname((os.path.abspath(__file__))))
from template.base import ConfigurationsApp


class CodeWriter(ConfigurationsApp):
    def __init__(self, config_json_file_path):
        super(CodeWriter, self).__init__(config_json_file_path)
        self.code_file_path = f"codes/{self.image_name}.py"
        with open(self.code_file_path, 'a') as code:
            code.write(f'# Importing important libraries\n')
            code.write(f'import sys\n')
            code.write(f'from PyQt5 import QtWidgets\n')
            code.write(f'from PyQt5.QtWidgets import *\n')
            code.write(f'from PyQt5.QtGui import QPixmap\n')
            code.write(f'from PIL import Image\n')
            code.write(f'import io\n')
            code.write(f'from folium import folium\n')
            code.write(f'from PyQt5.QtWebEngineWidgets import QWebEngineView\n')
            code.write(f'from PyQt5.QtCore import Qt\n')
            code.write(f'\n###################################\n')
            code.write(f'\n# Set up the application\n')
            code.write(f'app = QApplication(sys.argv)\n')
            code.write(f'# Set up the main window \n')
            code.write(f'curr_window = QtWidgets.QWidget()\n')
            code.write(f'curr_window.setGeometry({0}, {0}, {self.width}, {self.height})\n')

    def final_touch(self):
        with open(self.code_file_path, 'a') as code:
            code.write(f'\nif __name__ == "__main__":\n\tcurr_window.show()\n\tsys.exit(app.exec_())')



from uiElements.common import Common
from PyQt5.QtWidgets import QPushButton


class OnOffSwitch(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(OnOffSwitch, self).__init__(bounds, curr_window, img_name)
        self.ofb = None

    def getOnOffSwitch(self):
        self.ofb = QPushButton(self.curr_window)
        self.ofb.setCheckable(True)
        self.ofb.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        self.ofb.clicked.connect(self.changeBackgroundColor)
        self.ofb.setStyleSheet("background-color : lightgrey")

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the on/off switch: TODO\n')
            code.write(f'ofb = QPushButton(curr_window)\n')
            code.write(f'ofb.setCheckable(True)\n')
            code.write(f'ofb.setStyleSheet("background-color : lightgrey")\n')
            code.write(f'ofb.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

    def changeBackgroundColor(self):
        if self.ofb.isChecked():
            self.ofb.setStyleSheet("background-color : lightblue")
        else:
            self.ofb.setStyleSheet("background-color : lightgrey")

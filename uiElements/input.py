from uiElements.common import Common
from PyQt5.QtWidgets import *


class InputCodes(Common):
    def __init__(self, bounds, curr_window):
        super().__init__(bounds, curr_window)

    def getInput(self):
        inpt = QLineEdit(self.curr_window)
        inpt.setText("There is some text here")
        inpt.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        inpt.setMaximumSize(self.size[0],self.size[1])
        return self.curr_window

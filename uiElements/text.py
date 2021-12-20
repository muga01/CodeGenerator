from uiElements.common import Common
from PyQt5.QtWidgets import *


class TextCodes(Common):
    def __init__(self, bounds, curr_window):
        super().__init__(bounds, curr_window)

    def getText(self):
        label = QLabel(self.curr_window)
        label.setText("There is some text here")
        label.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        label.setMaximumSize(self.size[0],self.size[1])
        return self.curr_window

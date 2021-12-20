from uiElements.common import Common
from PyQt5.QtWidgets import *


class TextButton(Common):
    def __init__(self, bounds, curr_window):
        super().__init__(bounds, curr_window)

    def getTextButton(self):
        tbutton = QPushButton(self.curr_window)
        tbutton.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        tbutton.setText("Click Me")
        # TODO: Check the best way to set the sizes
        tbutton.setMaximumSize(self.size[0], self.size[1])
        return self.curr_window

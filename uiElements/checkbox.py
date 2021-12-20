from uiElements.common import Common
from PyQt5.QtWidgets import QCheckBox


class CheckBox(Common):
    def __init__(self, bounds, curr_window):
        super(CheckBox, self).__init__(bounds, curr_window)

    def getCheckBox(self):
        cb = QCheckBox(self.curr_window)
        cb.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        return self.curr_window

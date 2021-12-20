from uiElements.common import Common
from PyQt5.QtWidgets import QRadioButton


class RadioButton(Common):
    def __init__(self, bounds, curr_window):
        super(RadioButton, self).__init__(bounds, curr_window)

    def getRadioButton(self):
        rb = QRadioButton(self.curr_window)
        rb.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        return self.curr_window

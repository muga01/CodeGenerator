from uiElements.common import Common
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class Slider(Common):
    def __init__(self, bounds, curr_window):
        super(Slider, self).__init__(bounds, curr_window)

    def getSlider(self):
        sl = QSlider(Qt.Horizontal, self.curr_window)
        sl.setFocusPolicy(Qt.StrongFocus)
        sl.setTickPosition(QSlider.TicksBothSides)
        sl.setTickInterval(10)
        sl.setSingleStep(1)
        sl.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        return self.curr_window

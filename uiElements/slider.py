from uiElements.common import Common
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class Slider(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(Slider, self).__init__(bounds, curr_window, img_name)

    def getSlider(self):
        sl = QSlider(Qt.Horizontal, self.curr_window)
        sl.setFocusPolicy(Qt.StrongFocus)
        sl.setTickPosition(QSlider.TicksBothSides)
        sl.setTickInterval(10)
        sl.setSingleStep(1)
        sl.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the slider button\n')
            code.write(f'sl = QSlider(Qt.Horizontal, curr_window)\n')
            code.write(f'sl.setFocusPolicy(Qt.StrongFocus)\n')
            code.write(f'sl.setTickPosition(QSlider.TicksBothSides)\n')
            code.write(f'sl.setTickInterval({10})\n')
            code.write(f'sl.setSingleStep({1})\n')
            code.write(f'sl.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

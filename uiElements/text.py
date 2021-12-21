from uiElements.common import Common
from PyQt5.QtWidgets import *


class TextCodes(Common):
    def __init__(self, bounds, curr_window, img_name):
        super().__init__(bounds, curr_window, img_name)

    def getText(self):
        label = QLabel(self.curr_window)
        label.setText("There is some text here")
        label.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        label.setMaximumSize(self.size[0], self.size[1])

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the text field\n')
            code.write(f'label = QLabel(curr_window)\n')
            code.write(f'label.setText("There is some text here")\n')
            code.write(f'label.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
            code.write(f'label.setMaximumSize({self.size[0]}, {self.size[1]})\n')
        return self.curr_window

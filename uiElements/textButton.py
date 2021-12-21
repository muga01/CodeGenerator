from uiElements.common import Common
from PyQt5.QtWidgets import *


class TextButton(Common):
    def __init__(self, bounds, curr_window, img_name):
        super().__init__(bounds, curr_window, img_name)

    def getTextButton(self):
        tbutton = QPushButton(self.curr_window)
        tbutton.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        tbutton.setText("Click Me")
        # TODO: Check the best way to set the sizes
        tbutton.setMaximumSize(self.size[0], self.size[1])

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the text button\n')
            code.write(f'tbutton = QPushButton(curr_window)\n')
            code.write(f'tbutton.setText("Click Me")\n')
            code.write(f'tbutton.setGeometry({self.x_min}, {self.y_min}, {self.x_max}, {self.y_max})\n')
            code.write(f'# TODO: Check the best way to set the sizes\n')
            code.write(f'tbutton.setMaximumSize({self.size[0]}, {self.size[1]})\n')
        return self.curr_window

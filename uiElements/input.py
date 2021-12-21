from uiElements.common import Common
from PyQt5.QtWidgets import *


class InputCodes(Common):
    def __init__(self, bounds, curr_window, img_name):
        super().__init__(bounds, curr_window, img_name)

    def getInput(self):
        inpt = QLineEdit(self.curr_window)
        inpt.setText("There is some text here")
        inpt.setGeometry(self.x_min, self.y_min, self.x_max, self.y_max)
        inpt.setMaximumSize(self.size[0], self.size[1])

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the input field\n')
            code.write(f'inpt = QLineEdit(curr_window)\n')
            code.write(f'inpt.setText("There is some text here")\n')
            code.write(f'inpt.setGeometry({self.x_min}, {self.y_min}, {self.x_max}, {self.y_max})\n')
            code.write(f'inpt.setMaximumSize({self.size[0]}, {self.size[1]})\n')

        return self.curr_window

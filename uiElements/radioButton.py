from uiElements.common import Common
from PyQt5.QtWidgets import QRadioButton


class RadioButton(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(RadioButton, self).__init__(bounds, curr_window, img_name)

    def getRadioButton(self):
        rb = QRadioButton(self.curr_window)
        rb.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the radio button\n')
            code.write(f'rb = QRadioButton(curr_window)\n')
            code.write(f'rb.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

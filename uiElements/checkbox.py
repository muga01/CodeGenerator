from uiElements.common import Common
from PyQt5.QtWidgets import QCheckBox


class CheckBox(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(CheckBox, self).__init__(bounds, curr_window, img_name)

    def getCheckBox(self):
        cb = QCheckBox(self.curr_window)
        cb.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the Checkbox\n')
            code.write(f'cb = QCheckBox(curr_window)\n')
            code.write(
                f'cb.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

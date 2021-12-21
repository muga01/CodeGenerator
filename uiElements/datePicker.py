from uiElements.common import Common
from PyQt5.QtWidgets import QCalendarWidget


class DatePicker(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(DatePicker, self).__init__(bounds, curr_window, img_name)

    def getDatePicker(self):
        cal = QCalendarWidget(self.curr_window)
        cal.setGridVisible(True)
        # cal.clicked[QtCore.QDate].connect(self.showDate)
        cal.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the date picker\n')
            code.write(f'cal = QCalendarWidget(curr_window)\n')
            code.write(f'cal.setGridVisible(True)\n')
            code.write(f'cal.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

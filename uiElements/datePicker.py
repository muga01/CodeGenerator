from uiElements.common import Common
from PyQt5.QtWidgets import QCalendarWidget


class DatePicker(Common):
    def __init__(self, bounds, curr_window):
        super(DatePicker, self).__init__(bounds, curr_window)

    def getDatePicker(self):
        cal = QCalendarWidget(self.curr_window)
        cal.setGridVisible(True)
        # cal.clicked[QtCore.QDate].connect(self.showDate)
        cal.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        return self.curr_window

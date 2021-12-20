from PyQt5.QtGui import QPixmap
from uiElements.common import Common
from PIL import Image
from PyQt5.QtWidgets import *


class ImageCodes(Common):
    def __init__(self, bounds, curr_window):
        super().__init__(bounds, curr_window)
        # Generate empty image dimension (w and h)
        # self.size = (int(self.x_max - self.x_min), int(self.y_max - self.y_min))

    def getImage(self, id):
        Image.new(mode="RGB", size=self.size, color=0).save(f"images/img_{id}.jpg")
        label = QLabel(self.curr_window)
        label.setGeometry(self.x_min, self.y_min, self.x_max-self.x_min, self.y_max-self.y_min)
        label.setPixmap(QPixmap(f"images/img_{id}.jpg"))
        return self.curr_window

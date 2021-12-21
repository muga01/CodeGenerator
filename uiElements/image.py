from PyQt5.QtGui import QPixmap
from uiElements.common import Common
from PIL import Image
from PyQt5.QtWidgets import *


class ImageCodes(Common):
    def __init__(self, bounds, curr_window, img_name):
        super().__init__(bounds, curr_window, img_name)
        # Generate empty image dimension (w and h)
        # self.size = (int(self.x_max - self.x_min), int(self.y_max - self.y_min))

    def getImage(self, id):
        Image.new(mode="RGB", size=self.size, color=0).save(f"images/img_{id}.jpg")
        label = QLabel(self.curr_window)
        label.setGeometry(self.x_min, self.y_min, self.x_max-self.x_min, self.y_max-self.y_min)
        label.setPixmap(QPixmap(f"images/img_{id}.jpg"))
        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the image placeholder\n')
            code.write(f'Image.new(mode="RGB", size={self.size}, color={0}).save(f"images/img_{id}.jpg")\n')
            code.write(f'label = QLabel(curr_window)\n')
            code.write(f'label.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
            code.write(f'label.setPixmap(QPixmap(f"images/img_{id}.jpg"))\n')
        return self.curr_window

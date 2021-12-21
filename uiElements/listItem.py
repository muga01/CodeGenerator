from uiElements.common import Common
from template.base import ConfigurationsApp as basicConfig
from PyQt5.QtWidgets import QListWidget


class ListItem(Common, basicConfig):
    def __init__(self, bounds, curr_window, img_name):
        super(ListItem, self).__init__(bounds, curr_window, img_name)
        # self.boundbox = bounds

    def getListItem(self):
        mainList = QListWidget(self.curr_window)
        mainList.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)
        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the list item field\n')
            code.write(f'mainList = QListWidget(curr_window)\n')
            code.write(f'mainList.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

    # def findListMembers(self):
    #     l = self.boundbox
    #     items = self.bounds.copy()
    #     itemsWithin = []
    #     for i in range(len(items)):
    #         if self.itemIsinList(items[i], l):
    #             itemsWithin.append((self.classes_names[self.classes[i]], items[i]))
    #             del self.bounds[i]
    #             del self.classes[i]
    #     return itemsWithin
    #
    # def itemIsinList(self, i, l):
    #     return (i[0] > l[0]) and (i[1] > l[1]) and (i[2] < l[2]) and (i[3] < l[3])

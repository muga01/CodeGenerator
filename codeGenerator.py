from template.base import ConfigurationsApp as confApp
from uiElements.image import ImageCodes
from uiElements.textButton import TextButton
from uiElements.text import TextCodes
from uiElements.input import InputCodes
from uiElements.datePicker import DatePicker
from uiElements.slider import Slider
from uiElements.radioButton import RadioButton
from uiElements.checkbox import CheckBox
from uiElements.listItem import ListItem
from uiElements.mapView import MapView
from uiElements.onOffSwitch import OnOffSwitch
from codeWriter import CodeWriter
import sys
from PyQt5 import QtWidgets


class Window(confApp):
    def __init__(self, config_json_file_path):
        super().__init__(config_json_file_path)
        self.app = QtWidgets.QApplication(sys.argv)
        self.cur_window = QtWidgets.QWidget()
        self.cur_window.setGeometry(0, 0, self.width, self.height)

    def addUiElements(self):
        for i in range(len(self.bounds)):
            name = self.classes_names[int(self.classes[i])]
            if name == 'Image':
                self.cur_window = ImageCodes(self.bounds[i], self.cur_window, self.image_name).getImage(i)
            elif name == 'Text Button':
                self.cur_window = TextButton(self.bounds[i], self.cur_window, self.image_name).getTextButton()
            elif name == 'Text':
                self.cur_window = TextCodes(self.bounds[i], self.cur_window, self.image_name).getText()
            elif name == 'Input':
                self.cur_window = InputCodes(self.bounds[i], self.cur_window, self.image_name).getInput()
            elif name == 'Date Picker':
                self.cur_window = DatePicker(self.bounds[i], self.cur_window, self.image_name).getDatePicker()
            elif name == 'Slider':
                self.cur_window = Slider(self.bounds[i], self.cur_window, self.image_name).getSlider()
            elif name == 'Radio Button':
                self.cur_window = RadioButton(self.bounds[i], self.cur_window, self.image_name).getRadioButton()
            elif name == 'Checkbox':
                self.cur_window = CheckBox(self.bounds[i], self.cur_window, self.image_name).getCheckBox()
            elif name == 'List Item':
                self.cur_window = ListItem(self.bounds[i], self.cur_window, self.image_name).getListItem()
            elif name == 'Map View':
                self.cur_window = MapView(self.bounds[i], self.cur_window, self.image_name).getMapView()
            elif name == 'On/Off Switch':
                self.cur_window = OnOffSwitch(self.bounds[i], self.cur_window, self.image_name).getOnOffSwitch()


if __name__ == '__main__':
    cd_writer = CodeWriter("data/37815.json")
    mainWindow = Window("data/37815.json")
    mainWindow.addUiElements()
    cd_writer.final_touch()
    mainWindow.cur_window.show()
    sys.exit(mainWindow.app.exec_())

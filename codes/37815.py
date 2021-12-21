# Importing important libraries
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL import Image
import io
from folium import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt

###################################

# Set up the application
app = QApplication(sys.argv)
# Set up the main window 
curr_window = QtWidgets.QWidget()
curr_window.setGeometry(0, 0, 1080, 1920)

# Codes for the text button
tbutton = QPushButton(curr_window)
tbutton.setText("Click Me")
tbutton.setGeometry(334.11181640625, 1182.1376953125, 749.0859985351562, 1331.3250732421875)
# TODO: Check the best way to set the sizes
tbutton.setMaximumSize(414, 149)

# Codes for the image placeholder
Image.new(mode="RGB", size=(311, 312), color=0).save(f"images/img_1.jpg")
label = QLabel(curr_window)
label.setGeometry(388.0303649902344, 270.0096130371094, 311.8858337402344, 312.6153869628906)
label.setPixmap(QPixmap(f"images/img_1.jpg"))

# Codes for the input field
inpt = QLineEdit(curr_window)
inpt.setText("There is some text here")
inpt.setGeometry(44.32017517089844, 681.015625, 1019.3448486328125, 791.6260986328125)
inpt.setMaximumSize(975, 110)

# Codes for the text field
label = QLabel(curr_window)
label.setText("There is some text here")
label.setGeometry(221.13853454589844, 488.7744445800781, 108.08876037597656, 54.557830810546875)
label.setMaximumSize(108, 54)

# Codes for the text button
tbutton = QPushButton(curr_window)
tbutton.setText("Click Me")
tbutton.setGeometry(35.48167419433594, 811.7689819335938, 1036.3602294921875, 962.6156616210938)
# TODO: Check the best way to set the sizes
tbutton.setMaximumSize(1000, 150)

# Codes for the text field
label = QLabel(curr_window)
label.setText("There is some text here")
label.setGeometry(758.8883056640625, 488.48968505859375, 98.9130859375, 56.18023681640625)
label.setMaximumSize(98, 56)

# Codes for the text field
label = QLabel(curr_window)
label.setText("There is some text here")
label.setGeometry(456.9095764160156, 131.16812133789062, 162.72927856445312, 54.54579162597656)
label.setMaximumSize(162, 54)

# Codes for the text field
label = QLabel(curr_window)
label.setText("There is some text here")
label.setGeometry(47.46356964111328, 841.9312744140625, 173.29959869384766, 43.52178955078125)
label.setMaximumSize(173, 43)

# Codes for the image placeholder
Image.new(mode="RGB", size=(70, 79), color=0).save(f"images/img_8.jpg")
label = QLabel(curr_window)
label.setGeometry(239.55747985839844, 379.04608154296875, 70.79231262207031, 79.68795776367188)
label.setPixmap(QPixmap(f"images/img_8.jpg"))

# Codes for the image placeholder
Image.new(mode="RGB", size=(70, 78), color=0).save(f"images/img_9.jpg")
label = QLabel(curr_window)
label.setGeometry(771.3008422851562, 381.44281005859375, 70.46978759765625, 78.27020263671875)
label.setPixmap(QPixmap(f"images/img_9.jpg"))

# Codes for the text button
tbutton = QPushButton(curr_window)
tbutton.setText("Click Me")
tbutton.setGeometry(87.84736633300781, 990.1185302734375, 1021.8140258789062, 1121.52783203125)
# TODO: Check the best way to set the sizes
tbutton.setMaximumSize(933, 131)

# Codes for the text field
label = QLabel(curr_window)
label.setText("There is some text here")
label.setGeometry(43.42705535888672, 885.0758056640625, 288.9849624633789, 57.2061767578125)
label.setMaximumSize(288, 57)

if __name__ == "__main__":
	curr_window.show()
	sys.exit(app.exec_())
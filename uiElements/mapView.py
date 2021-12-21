import io
from folium import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from uiElements.common import Common


class MapView(Common):
    def __init__(self, bounds, curr_window, img_name):
        super(MapView, self).__init__(bounds, curr_window, img_name)

    def getMapView(self):
        # you can change this coordinate or make it be imported from a common/base/setup file
        coordinates = (51.74677969131641, 19.450116091689516)
        m = folium.Map(
            location=coordinates,
            zoom_start=13
        )
        data = io.BytesIO()
        m.save(data, close_file=False)
        mapview = QWebEngineView(self.curr_window)
        mapview.setHtml(data.getvalue().decode())
        mapview.setGeometry(self.x_min, self.y_min, self.x_max - self.x_min, self.y_max - self.y_min)

        # Let's write these codes to our bare codes file
        with open(f"codes/{self.image_name}.py", 'a') as code:
            code.write(f'\n# Codes for the mapview field\n')
            code.write(f'coordinates = (51.74677969131641, 19.450116091689516)\n')
            code.write(f'm = folium.Map(location={coordinates},zoom_start={13})\n')
            code.write(f'data = io.BytesIO()\n')
            code.write(f'm.save(data, close_file=False)\n')
            code.write(f'mapview = QWebEngineView(curr_window)\n')
            code.write(f'mapview.setGeometry({self.x_min}, {self.y_min}, {self.x_max - self.x_min}, {self.y_max - self.y_min})\n')
        return self.curr_window

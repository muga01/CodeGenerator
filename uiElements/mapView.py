import io
from folium import folium
from PyQt5.QtWebEngineWidgets import QWebEngineView
from uiElements.common import Common


class MapView(Common):
    def __init__(self, bounds, curr_window):
        super(MapView, self).__init__(bounds, curr_window)

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
        return self.curr_window

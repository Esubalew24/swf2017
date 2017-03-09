from kivy.app import App
from kivy.garden.mapview import MapView

# fola test
# this is the map
class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        return mapview

MapViewApp().run()
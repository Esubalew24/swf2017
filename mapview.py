from kivy.garden.mapview import MapView
from kivy.app import App

class MapViewApp(App):
    def build(self):
        mapview = MapView(zoom=17, lat=65.0593, lon=25.4663)
        return mapview

MapViewApp().run()
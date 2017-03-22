from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
import multiprocessing
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from test import MainApp

class CustomPopup(Popup):
    pass

class Welcome(Screen):
    pass

class SecondScreen(Screen):
    pass

class MapScreen(Screen):
    def launchMainApp(self):
        app = MainApp()
        p = multiprocessing.Process(target=app.run)
        p.start()

class CongratulationScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    Welcome:
    SecondScreen:
    MapScreen:
    CongratulationScreen:

<Welcome>:
    name: 'welcome'
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'logo.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'Go to second screen'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'Go to Map Screen'
                font_size: 30
                on_release: app.root.current = 'third'

<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'

        Image:
            source: 'welcome.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'Go to first screen'
                font_size: 30
                on_release: app.root.current = 'welcome'
            Button:
                text: 'Go to Map Screen'
                font_size: 30
                on_release: app.root.current = 'third'

<MapScreen>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        MapView:
            zoom: 17
            lat: 65.0593
            lon: 25.4663
        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'Go to first screen'
                font_size: 30
                on_release: app.root.current = 'welcome'
            Button:
                text: 'Launch Mini Game 1'
                font_size: 30
                on_release: root.launchMainApp()
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
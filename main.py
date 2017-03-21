from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class Wellcome(Screen):
    pass

class SecondScreen(Screen):
    pass

class MapScreen(Screen):
   pass



class CongratulationScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    Wellcome:
    SecondScreen:
    MapScreen:
    CongratulationScreen:

<Wellcome>:
    name: 'wellcome'
    BoxLayout:
        orientation: 'vertical'
        Image:
            source: 'logo.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'goto second screen'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'Go to third page'
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
                on_release: app.root.current = 'wellcome'
            Button:
                text: 'go to third page'
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
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'wellcome'
            Button:
                text: 'Go to the forth page'
                font_size: 30
                on_release: app.root.current = 'forth'

<CongratulationScreen>:
    name: 'forth'
    BoxLayout:
        orientation: 'vertical'

        Image:
            source: 'congratulation.png'
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'goto welcome screen'
                font_size: 30
                on_release: app.root.current = 'wellcome'
            Button:
                text: 'Go to the second page'
                font_size: 30
                on_release: app.root.current = 'second'


''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
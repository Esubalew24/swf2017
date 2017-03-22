from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from minigame1.play import game1
import multiprocessing
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from test import MainApp

class CustomPopup(Popup):
    pass

class Wellcome(Screen):
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
                on_release: app.root.current = 'wellcome'
            Button:
                text: 'go to Map Screen'
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
                text: 'Launch Mini Game 1'
                font_size: 30
                on_release: root.launchMainApp()
''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
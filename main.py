from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class CustomPopup(Popup):
    pass

class Wellcome(Screen):
    pass

class SecondScreen(Screen):
    pass

class MapScreen(Screen):

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

     #def fn(self, value):
     #   execfile("hello.py")





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

            Button:
                text: "Open Popup"
                on_press: root.open_popup()

            Button:
                text: "Open second Popup"
                on_press: root.open_popup()


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


<CustomPopup>:
    size_hint: .75, .75
    auto_dismiss: False
    title: "Minigame 1"
    Button:
        text: "Close"
        on_press: root.dismiss()


''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
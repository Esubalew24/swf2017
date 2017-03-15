from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.mapview import MapView
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from minigame1.main import Pairs
Builder.load_string('''
<map>:
    MapView:
        zoom: 17
        lat: 65.0593
        lon: 25.4663
    Button:
        text: 'Click to play game'
        size: 150, 150
        pos: 400, 400
''')

#class game(App):
#    def build(self):
#        return Pairs()

class map(Widget):
    def build(self):
        map = MapView()
        button = Button()
        map.add_widget(button)

class main(App):
    def build(self):
        return map()

main().run()
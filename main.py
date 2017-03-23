from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from play import DrawInput
from question import QuestionAnswer
from minigame3.main import TicTacToe
from drawing import Painter

class CustomPopup(Popup):
    pass

class Welcome(Screen):
    pass

class SecondScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class Game(Screen):
    pass

class Question(Screen):
    pass

class Minigame3(Screen):
    pass

class Drawing(Screen):
    pass

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
    Game:
    Question:
    Minigame3:
    Drawing:
    CongratulationScreen:

<Welcome>:
    name: 'welcome'
    FloatLayout:
        orientation: 'vertical'
        Image:
            source: 'logo.png'
            allow_stretch: True
            keep_ratio: False
        FloatLayout:
            size_hint: 1, None
            Button:
                text: 'Next'
                size_hint: 0.3, 0.6
                pos_hint: {'x': 0.35, 'y': 0.2}
                font_size: 30
                on_release: app.root.current = 'second'

<SecondScreen>:
    name: 'second'
    FloatLayout:
        orientation: 'vertical'

        Image:
            source: 'welcome.png'
            allow_stretch: True
            keep_ratio: False
        FloatLayout:
            size_hint: 1, None
            Button:
                text: 'Map'
                size_hint: 0.3, 0.6
                pos_hint: {'x': 0.35, 'y': 0.2}
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
            MapMarker:
                title: "Restaurant"
                lat: 65.0600012
                lon: 25.4645286
                on_release: app.root.current = 'minigame3'

            MapMarker:
                title: "Somewhere"
                lat: 65.0593177
                lon: 25.466293500000006
                on_release: app.root.current = 'question'

            MapMarker:
                title: "Ravintola Stories"
                lat: 65.05820786309047
                lon: 25.466705560684204
                on_release: app.root.current = 'drawing'

            MapMarker:
                title: "Oulun Yliopisto Kauppakorkeakoulu"
                lat: 65.06031611340609
                lon: 25.468658208847046
                on_release: app.root.current = 'minigame3'

        BoxLayout:
            size_hint: 1, None
            Button:
                text: 'Play Games'
                font_size: 30
                on_release: app.root.current = 'question'
<Game>:
    name:'game'
    BoxLayout:
        orientation: 'vertical'
        DrawInput:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
<Question>:
    name: 'question'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswer:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
<Minigame3>:
    name: 'minigame3'
    BoxLayout:
        orientation: 'vertical'
        TicTacToe:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
<Drawing>:
    name: 'drawing'
    BoxLayout:
        orientation: 'vertical'
        Painter:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
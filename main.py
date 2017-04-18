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
                size_hint: 0.3, 1.0
                pos_hint: {'x': 0.35, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
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
                text: 'Back'
                size_hint: 0.3, 1.0
                pos_hint: {'x': 0.05, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
                on_release: app.root.current = 'welcome'   
            
            Button:
                text: 'Next'
                size_hint: 0.3, 1.0
                pos_hint: {'x': 0.65, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
                on_release: app.root.current = 'third'    
            
<MapScreen>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        RelativeLayout:
            MapView:
                lat: 65.0593
                lon: 25.4663
                zoom: 17
                
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
    
               
                MapMarkerPopup:
                    name: 'Tellus'
                    lat: 65.058824
                    lon: 25.467081
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Tellus.png"
                                mipmap: True
                            Label:
                                text: "[b]Tellus Innovation Arena[/b]\\n Tellus Innovation Arena is a brand new, \\n inspiring open space for learning, collaboration and \\n entrepreneurship at Uni of Oulu"
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'minigame3'
                                
                                
                MapMarkerPopup:
                    name: 'Student_Center'
                    lat: 65.059813
                    lon: 25.465233
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "student_center.png"
                                mipmap: True
                            Label:
                                text: "[b]Student Center[/b] \\n Student Center provides comprehensive \\n services for students starting with \\n registration to the university and going  \\n all the way to alumni services."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question'
                
                
                MapMarkerPopup:
                    name: 'OYY'
                    lat: 65.059053
                    lon: 25.46596
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "OYY.png"
                                mipmap: True
                            Label:
                                text: "[b]OYY[/b]\\n OYY supervises the interests of its \\n members at the University, in the City \\n of Oulu and at the national level."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                
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
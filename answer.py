import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
class Answer(Screen):
    pass

Builder.load_string('''
<Answer>:
    name: 'answer'
    BoxLayout:
        Button:
            text: "Correct"
            on_release: app.root.current = 'third'                       

     ''')


class Answer(BoxLayout):
    pass
    Window.clearcolor = (0, 0.5, 0.5, 0.5)



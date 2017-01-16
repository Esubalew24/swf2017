import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.button import Label

class HelloKivy(App):
    def build(self):
        return Label(text="Welcome to University of Oulu")
        return Label(text="Play a tour game to University of Oulu")
helloKivy = HelloKivy()

helloKivy.run()

from kivy.app import App
from kivy.uix.button import Button

from test2 import ChildApp

import multiprocessing

#ass

class MainApp(App):

    def build(self):
        b = Button(text='Launch Child App')
        b.bind(on_press=self.launchChild)
        return b

    def launchChild(self, button):
        app = ChildApp()
        p = multiprocessing.Process(target=app.run)
        p.start()

if __name__ == '__main__':
    MainApp().run()
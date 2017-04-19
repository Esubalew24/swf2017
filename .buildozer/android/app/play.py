from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.properties import ObjectProperty

# Used to display popup
class CustomPopup(Popup):
    pass

class DrawInput(Widget):

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    # For radio buttons
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    # Opens Popup when called
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()


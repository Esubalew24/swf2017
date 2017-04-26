import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder
Builder.load_string('''
#: import CheckBox kivy.uix.checkbox
<CustLabel@Label>:
    color: 0, 0, 0, 1
<QuestionAnswerOyy>:
    name: 'ToggleButton'
    GridLayout:
        orientation: "vertical"
        cols: 1
        rows: 5
        spacing: '28dp'
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: 'Choice 1'
            font_size: 50
            
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'A'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'B'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'C'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'D'
            group: 'g1'
     ''')
# Used to display popup
#class ResultPopup(Popup):
 #   pass
class QuestionAnswerOyy(BoxLayout):
    # For checkbox
    checkbox_is_active = ObjectProperty(False)
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
   # def open_popup(self):
    #    the_popup = ResultPopup()
     #   the_popup.open()
    Window.clearcolor = (0, 0.5, 0.5, 0.5)
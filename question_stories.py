import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''


<QuestionAnswerStories>:
    name: 'ToggleButton'
    GridLayout:
        orientation: "vertical"
        cols: 1
        rows: 8
        spacing: '45dp'
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: 'Faculty of Technology focuses on science with:'
            font_size: '15sp'
            text_size: self.size
            halign: 'left'
            valign:'middle'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Winter attitude'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Sea attitude'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Finland attitude'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Arctic attitude'
            group: 'g1'
     ''')


# Used to display popup
#class ResultPopup(Popup):
 #   pass


class QuestionAnswerStories(BoxLayout):
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



import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''

<QuestionAnswerStudentCenter>:
    name: 'ToggleButton'
    GridLayout:
        orientation: "vertical"
        cols: 1
        rows: 8
        spacing: '42dp'
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: 'Student Center provides comprehensive services for students. They provide these services except:'
            text_size: 38
            text_size: self.size
            halign: 'left'
            valign:'middle'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Student affairs'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'ICT services for students'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Admission and internship'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Borrow and return books'
            group: 'g1'
     ''')

# Used to display popup
#class ResultPopup(Popup):
 #   pass


class QuestionAnswerStudentCenter(BoxLayout):
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


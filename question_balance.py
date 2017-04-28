import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''


<QuestionAnswerBalance>:
    name: 'ToggleButton'
    GridLayout:
        orientation: "vertical"
        cols: 1
        rows: 8
        spacing: '45dp'
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: 'Faculty of Humanities  possesses a definite \\ncharacter of its own, two subjects having \\nthe only professorial chair in Finland. \\nOne of them is:'
            font_size: '15sp'
            text_size: self.size
            halign: 'left'
            valign:'middle'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'The History of Science and Ideas'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Language and linguistics'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Finnish culture studies'
            group: 'g1'
        ToggleButton:
            size_hint_y: None
            height: '48dp'
            text: 'Gender study'
            group: 'g1'
     ''')


# Used to display popup
#class ResultPopup(Popup):
 #   pass


class QuestionAnswerBalance(BoxLayout):
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



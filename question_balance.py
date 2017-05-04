import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''


<ResultPopupBalance>:
    id: popup
    title: 'Result'
    auto_dismiss: False
    size_hint: .70, .35
    BoxLayout:
        id: contentbox
        orientation: "vertical"
        Label:
            id: content_text
            
            height: self.texture_size[1]
            text: "Your Answer is Correct"
            text_size: None, None
            line_height: 1.5
            valign: "middle"
                
        Button:
            text: "Close"
            size_hint_y: None
            height: "40dp"
            on_press: root.dismiss()


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
            text: 'Faculty of Humanities  possesses a definite character of its own, two subjects having the only professorial chair in Finland. One of them is:'
            text_size: 38
            text_size: self.size
            halign: 'left'
            valign:'middle'
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'The History of Science and Ideas'
            group: 'g1'
            on_press: root.open_popup()
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Language and linguistics'
            group: 'g1'
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Finnish culture studies'
            group: 'g1'
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Gender study'
            group: 'g1'
     ''')


class ResultPopupBalance(Popup):
    pass


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

    def open_popup(self):
        the_popup = ResultPopupBalance()
        the_popup.open()

    Window.clearcolor = (0, 0.5, 0.5, 0.5)



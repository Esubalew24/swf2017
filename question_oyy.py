import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder

Builder.load_string('''

<ResultPopupOyy>:
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


<QuestionAnswerOyy>:
    name: 'ToggleButton'
    GridLayout:
        orientation: "vertical"
        cols: 1
        rows: 8
        spacing: '45dp'
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: 'All students can become members of the University Student union OYY and they can get these benefits except:'
            font_size: '15sp'
            text_size: 38
            text_size: self.size
            halign: 'left'
            valign:'middle'
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Diary'
            group: 'g1'
            
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Loan service'
            group: 'g1'
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Free membership fee'
            group: 'g1'
            on_press: root.open_popup()
        Button:
            size_hint_y: None
            height: '48dp'
            text: 'Legal guidance'
            group: 'g1'
     ''')


class ResultPopupOyy(Popup):
    pass


class QuestionAnswerOyy(BoxLayout):
    # For checkbox
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox Checked")
        else:
            print("Checkbox Unchecked")

    # Opens Popup when called

    def open_popup(self):
        the_popup = ResultPopupOyy()
        the_popup.open()


    Window.clearcolor = (0, 0.5, 0.5, 0.5)
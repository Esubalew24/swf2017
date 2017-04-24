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

<ResultPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: "The Popup"
    Button:
        text: "Close"
        on_press: root.dismiss()


<QuestionAnswerZoologicalMuseum>:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # ---------- Holds CheckBox and RadioBox ----------
    BoxLayout:
        orientation: "vertical"
        height: 30

        BoxLayout:
            orientation: "vertical"
            size_hint_x: .22
            CustLabel:
                text: "Are you over 20 - Zoological Museum "
                size_hint_x: .80
            CheckBox:
                on_active: root.checkbox_18_clicked(self, self.active)
                size_hint_x: .20
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .55
            CustLabel:
                text: " Favorite Color?"
                color: 0, 0, 0, 1
                size_hint_x: .265
            CheckBox:
                group: "fav_color"
                value: root.blue
                size_hint_x: .05
            CustLabel:
                text: " Blue"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.red
                size_hint_x: .05
            CustLabel:
                text: " Red"
                color: 0, 0, 0, 1
                size_hint_x: .15
            CheckBox:
                group: "fav_color"
                value: root.green
                size_hint_x: .05
            CustLabel:
                text: " Green"
                color: 0, 0, 0, 1
                size_hint_x: .15

    # ---------- Holds Slider & Switch ----------
    BoxLayout:
        orientation: "horizontal"
        height: 30


     ''')


# Used to display popup
#class ResultPopup(Popup):
 #   pass


class QuestionAnswerZoologicalMuseum(BoxLayout):
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



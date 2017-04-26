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

<QuestionAnswerTellus>:
    
    BoxLayout:
        orientation: "vertical"
        CustLabel:
            text: "Which international cultures and cooperation event is celebrated by Tellus innovation arena?  "
            color: 0, 0, 0, 1
        CheckBox:
            group: "fav_color"
            value: root.blue
        CustLabel:
            text: "International avenue"
            color: 0, 0, 0, 1
        CheckBox:
            group: "fav_color"
            value: root.blue
        CustLabel:
            text: " Polar bear pitching"
            color: 0, 0, 0, 1
        CheckBox:
            group: "fav_color"
            value: root.blue
        CustLabel:
            text: " International food festival"
            color: 0, 0, 0, 1
        CheckBox:
            group: "fav_color"
            value: root.blue
        CustLabel:
            text: " Start-up week"
            color: 0, 0, 0, 1   
                   
            
            

     ''')


# Used to display popup
#class ResultPopup(Popup):
 #   pass


class QuestionAnswerTellus(BoxLayout):
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



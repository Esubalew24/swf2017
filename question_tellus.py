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
    orientation: "vertical"
    padding: 10
    

    # ---------- Holds CheckBox and RadioBox ----------
    BoxLayout:
        orientation: "vertical"
        height: 30
        BoxLayout:
            orientation: "horizontal"
            CustLabel:
                text: " Favorite Color? "
                color: 0, 0, 0, 1
                size_hint_x: .265
               
        
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .10
            size_hint_y: .30
            CheckBox:
                group: "fav_color"
                value: root.blue
            CustLabel:
                text: " Blue"
                color: 0, 0, 0, 1
            
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .10
            size_hint_y: .30
            CheckBox:
                group: "fav_color"
                value: root.blue
                
              
            CustLabel:
                text: " Red"
                color: 0, 0, 0, 1       
            
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .10
            size_hint_y: .30
            CheckBox:
                group: "fav_color"
                value: root.blue
              
            CustLabel:
                text: " Yellow"
                color: 0, 0, 0, 1 
        BoxLayout:
            orientation: "horizontal"
            size_hint_x: .10
            size_hint_y: .30
            CheckBox:
                group: "fav_color"
                value: root.blue
              
            CustLabel:
                text: " Whatever"
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



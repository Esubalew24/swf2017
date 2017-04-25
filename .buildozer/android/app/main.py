from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.garden.mapview import MapView, MapMarker
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from play import DrawInput
from question import QuestionAnswer
from question_tellus import QuestionAnswerTellus
from question_student_center import QuestionAnswerStudentCenter
from question_balance import QuestionAnswerBalance
from question_oyy import QuestionAnswerOyy
from question_library import QuestionAnswerLibrary
from question_datagarage import QuestionAnswerDatagarage
from question_fablab import QuestionAnswerFablab
from question_zoological_museum import QuestionAnswerZoologicalMuseum
from question_saalasti_hall import QuestionAnswerSaalastiHall
from question_faculity_of_education import QuestionAnswerFaculityOfEducation
from question_stories import QuestionAnswerStories
from question_faculty_of_science import QuestionAnswerFaculityOfScience
from question_aava import QuestionAnswerAava
from question_psoas import QuestionAnswerPsoas

from minigame3.main import TicTacToe
from drawing import Painter

class CustomPopup(Popup):
    pass

class Welcome(Screen):
    pass

class SecondScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class Game(Screen):
    pass

class Question(Screen):
    pass

class Question_tellus(Screen):
    pass

class Question_student_center(Screen):
    pass

class Question_balance(Screen):
    pass

class Question_datagarage(Screen):
    pass

class Question_fablab(Screen):
    pass

class Question_library(Screen):
    pass

class Question_oyy(Screen):
    pass

class Question_zoological_museum(Screen):
    pass

class Question_saalasti_hall(Screen):
    pass

class Question_faculity_of_education(Screen):
    pass

class Question_stories(Screen):
    pass

class Question_faculity_of_science(Screen):
    pass

class Question_aava(Screen):
    pass

class Question_psoas(Screen):
    pass

class Minigame3(Screen):
    pass

class Drawing(Screen):
    pass

class CongratulationScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

root_widget = Builder.load_string('''

#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    Welcome:
    SecondScreen:
    MapScreen:
    Game:
    Question:
    Question_tellus:
    Question_student_center:
    Question_balance:
    Question_oyy:
    Question_library:
    Question_datagarage:
    Question_fablab:
    Question_zoological_museum:
    Question_saalasti_hall:
    Question_faculity_of_education:
    Question_stories:
    Question_faculity_of_science:
    Question_aava:
    Question_psoas:
    
    Minigame3:
    Drawing:
    CongratulationScreen:

<Welcome>:
    name: 'welcome'
    FloatLayout:
        orientation: 'vertical'
        Image:
            source: 'logo.png'
            allow_stretch: True
            keep_ratio: False
        FloatLayout:
            size_hint: 1, None
            Button:
                text: 'Next'
                size_hint: 0.3, 1.3
                pos_hint: {'x': 0.35, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
                on_release: app.root.current = 'second'

<SecondScreen>:
    name: 'second'
    FloatLayout:
        orientation: 'vertical'

        Image:
            source: 'welcome.png'
            allow_stretch: True
            keep_ratio: False
        FloatLayout:
            size_hint: 1, None
                
            Button:
                text: 'Back'
                size_hint: 0.3, 1.3
                pos_hint: {'x': 0.05, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
                on_release: app.root.current = 'welcome'   
            
            Button:
                text: 'Next'
                size_hint: 0.3, 1.3
                pos_hint: {'x': 0.65, 'y': 1.0}
                font_size: 70
                background_color: (0.0, 0.0, 1.0, 0.5)
                on_release: app.root.current = 'third'    
            
<MapScreen>:
    name: 'third'
    BoxLayout:
        orientation: 'vertical'
        RelativeLayout:
            MapView:
                lat: 65.0593
                lon: 25.4663
                zoom: 17
                
                
               
                MapMarkerPopup:
                    name: 'Tellus'
                    lat: 65.058824
                    lon: 25.467081
                    popup_size: dp(380), dp(250)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Tellus.png"
                                mipmap: True
                            Label:
                                text: "[b]Tellus Innovation Arena[/b]\\n Tellus Innovation Arena \\n is a brand new, inspiring \\n open space for learning, \\n collaboration and \\n entrepreneurship at the Uni."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_tellus'
                                
                                
                MapMarkerPopup:
                    name: 'Student_Center'
                    lat: 65.059813
                    lon: 25.465233
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "student_center.png"
                                mipmap: True
                            Label:
                                text: "[b]Student Center[/b] \\n Student Center provides comprehensive \\n services for students starting with \\n registration to the university and going  \\n all the way to alumni services."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_student_center'
                
                
                MapMarkerPopup:
                    name: 'oyy'
                    lat: 65.059053
                    lon: 25.46596
                    popup_size: dp(400), dp(250)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "OYY.png"
                                mipmap: True
                            Label:
                                text: "[b]OYY[/b]\\n OYY supervises the interests of its \\n members at the University, in the City \\n of Oulu and at the national level."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                
                                font_size: 30
                                on_release: app.root.current = 'question_oyy'   
                
                MapMarkerPopup:
                    name: 'Library'
                    lat: 65.061484
                    lon: 25.466539
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Library.png"
                                mipmap: True
                            Label:
                                text: "[b]Library[/b]\\n Oulu University Library is a \\n scientific library, the task of \\n which is to provide library \\n and information services for the \\n researchers, teachers and students \\n of the University of Oulu."
                                markup: True
                                halign: "left"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                
                                font_size: 30
                                on_release: app.root.current = 'question_library'
                
                
                MapMarkerPopup:
                    name: 'Fab_Lab'
                    lat: 65.058953
                    lon: 25.466985
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "fab lab.png"
                               
                            Label:
                                text: "[b]Fab_Lab[/b]\\n Fab Lab Oulu is a small digital \\n manufacturing working area (fabrication laboratory)  \\n that complies with open innovation \\n concept developed by MIT in the United States."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_fablab'                
                
                MapMarkerPopup:
                    name: 'Faculty of ITEE'
                    lat: 65.057949
                    lon: 25.468455
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Faculty of ITEE.png"
                               
                            Label:
                                text: "[b]Faculty of ITEE[/b]\\n The mission of the ITEE faculty is to \\n advance internationally top-level \\n research on information technology \\n and education based on it and  \\n generate new knowledge of information \\n technology and apply it to the needs \\n of the society, people and industries."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_oyy'                    
                
                
                MapMarkerPopup:
                    name: 'Zoological_Museum'
                    lat: 65.060597
                    lon: 25.466931
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "zoological_museum.png"
                               
                            Label:
                                text: "[b]Zoological Museum[/b]\\n Fab Lab Oulu is a small digital \\n manufacturing working area (fabrication laboratory)  \\n that complies with open innovation \\n concept developed by MIT in the United States."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_oyy'            
                
                MapMarkerPopup:
                    name: 'Balance'
                    lat: 65.061035
                    lon: 25.468079
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Faculty of Humanities.png"
                               
                            Label:
                                text: "[b]Balance[/b]\\n The Faculty of Humanities provided \\n teaching and research in practically \\n all the academic disciplines concerned \\n with achievements in the humanities: \\n history, language and linguistics, \\n cultural studies and literature."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_balance'
                
                
                
                MapMarkerPopup:
                    name: 'Saalasti Hall'
                    lat: 65.056928
                    lon: 25.468709
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Salastti_hall.png"
                            Label:
                                text: "[b]Saalasti Hall[/b] is the place\\nwhich graduation ceremonies\\nare held every month"
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_saalasti_hall'
                
                MapMarkerPopup:
                    name: 'KTK112'
                    lat: 65.061765
                    lon: 25.469892
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Faculty of education.png"
                            Label:
                                text: "[b]The Faculty of Education[/b]\\nis multidisciplinary expert\\norganisation for training,\\nresearch and development\\nin the field of education\\naand teaching."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_faculity_of_education'    
                            
                MapMarkerPopup:
                    name: 'Stories'
                    lat: 65.058493
                    lon: 25.466995
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Faculty of technology and story.png"
                            Label:
                                text: "[b]The Faculty of Technology[/b]\\noperates in the field of\\nMechanical Engineering\\nEnvironmental Engineering\\nand Industrial Engineering\\nand Management."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_stories'
                            
                MapMarkerPopup:
                    name: 'L6'
                    lat: 65.059941
                    lon: 25.466303
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "faculty of science.png"
                            Label:
                                text: "[b]The Faculty of Science[/b]\\nis the second biggest\\neducational unit\\nin Sciences in Finland"
                                markup: True
                                halign: "center"
                                
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_faculity_of_science'
                MapMarkerPopup:
                    name: 'Aava'
                    lat:  65.060479
                    lon:  25.46656
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "aava and restaurant.png"
                            Label:
                                text: "Student prices for\\n the meals are:\\n basic student lunch EUR 2.60\\nsoup lunch EUR 2.25\\ngrill portion EUR 4.95\\nand the special lunch EUR 4.85"
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_aava'
                
                MapMarkerPopup:
                    name: 'PSOAS'
                    lat: 65.05733
                    lon: 25.467344
                    popup_size: dp(430), dp(280)
                    Bubble:
                        BoxLayout:
                            orientation: "horizontal"
                            padding: "5dp"
                            AsyncImage:
                                source: "Psoas.png"
                               
                            Label:
                                text: "[b]PSOAS[/b]\\n The main duty of PSOAS is \\n to offer inexpensive living \\n quarters to the areas."
                                markup: True
                                halign: "center"
                            
                            Button:
                                text: 'Play'
                                size_hint: 0.4, 0.25
                                font_size: 30
                                on_release: app.root.current = 'question_psoas'
        
<Game>:
    name:'game'
    BoxLayout:
        orientation: 'vertical'
        DrawInput:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
            
<Question>:
    name: 'question_OYY'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswer:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
            
<Question_tellus>:
    name: 'question_tellus'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerTellus:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
            
<Question_student_center>:
    name: 'question_student_center'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerStudentCenter:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'            

<Question_oyy>:
    name: 'question_oyy'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerOyy:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'             

<Question_library>:
    name: 'question_library'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerLibrary:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'             

<Question_balance>:
    name: 'question_balance'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerBalance:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'             

<Question_datagarage>:
    name: 'question_datagarage'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerDatagarage:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'             

<Question_fablab>:
    name: 'question_fablab'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerFablab:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'    
                
<Question_zoological_museum>:
    name: 'question_zoological_museum'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerZoologicalMuseum:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 
            
<Question_saalasti_hall>:
    name: 'question_saalasti_hall'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerSaalastiHall:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 

<Question_faculity_of_education>:
    name: 'question_faculity_of_education'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerFaculityOfEducation:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
            
<Question_stories>:
    name: 'question_stories'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerStories:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 

<Question_faculity_of_science>:
    name: 'question_faculity_of_science'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerFaculityOfScience:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 

<Question_aava>:
    name: 'question_aava'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerAava:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 

<Question_psoas>:
    name: 'question_psoas'
    BoxLayout:
        orientation: 'vertical'
        QuestionAnswerPsoas:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third' 


    
<Minigame3>:
    name: 'minigame3'
    BoxLayout:
        orientation: 'vertical'
        TicTacToe:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'
<Drawing>:
    name: 'drawing'
    BoxLayout:
        orientation: 'vertical'
        Painter:
            orientation: "vertical"
            padding: 50
            spacing: 50
        Button:
            text: 'Back'
            size_hint: 1, None
            font_size: 30
            on_release: app.root.current = 'third'

''')

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()
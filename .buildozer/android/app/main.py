from kivy.app import App
from plyer import gps
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock, mainthread
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
class ResultPopup(Popup):
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

kv = '''

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
        MapView:
            lat: 65.0593
            lon: 25.4663
            zoom: 17

            MapMarker:
                lat: app.app_lat
                lon: app.app_lon
                source: 'character.png'

            MapMarkerPopup:
                name: 'Tellus'
                lat: 65.058824
                lon: 25.467081
                source: 'info.png'
                popup_size: dp(340), dp(250)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Tellus.png"
                            mipmap: True
                        Label:
                            
                            text: "[b]Tellus Innovation Arena[/b]\\nTellus Innovation Arena is a brand new, inspiring open space for learning, collaboration and entrepreneurship at the Uni."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                        
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250,100
                                valign: 'middle'
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/tellusarena/")   
                            
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250,15
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/tellusarena-fi/")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_tellus'
                            
                            
            MapMarkerPopup:
                name: 'Student_Center'
                lat: 65.059813
                lon: 25.465233
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "student_center.png"
                            mipmap: True
                        Label:
                            text: "[b]Student Center[/b] \\nStudent Center provides comprehensive services for students starting with registration to the university and going  all the way to alumni services."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                        
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250,100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/university/node/34985")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250,15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/yliopisto/opiskelijakeskus")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_student_center'
            
            
            MapMarkerPopup:
                name: 'oyy'
                lat: 65.059053
                lon: 25.46596
                source: 'info.png'
                popup_size: dp(340), dp(250)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "OYY.png"
                            mipmap: True
                        Label:
                            text: "[b]OYY[/b]\\nOYY supervises the interests of its members at the University, in the City of Oulu and at the national level."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250,100
                                align:'center'
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oyy.fi/en/")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align:'center'
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oyy.fi/")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_oyy'   
            
            MapMarkerPopup:
                name: 'Library'
                lat: 65.061484
                lon: 25.466539
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Library.png"
                            mipmap: True
                        Label:
                            text: "[b]Library[/b] \\nOulu University Library is a scientific library, the task of which is to provide library and information services for the researchers, teachers and students of the University of Oulu."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/library/")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/kirjasto/")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            
                            font_size: 30
                            on_release: app.root.current = 'question_library'
            
            
            MapMarkerPopup:
                name: 'Fab_Lab'
                lat: 65.058953
                lon: 25.466985
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "fab lab.png"
                           
                        Label:
                            text: "[b]Fab_Lab[/b]\\nFab Lab Oulu is a small digital manufacturing working area (fabrication laboratory)  that complies with open innovation concept developed by MIT in the United States."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/fablab/")   
                            
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_fablab'                
            
            MapMarkerPopup:
                name: 'Faculty of ITEE'
                lat: 65.057949
                lon: 25.468455
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Faculty of ITEE.png"
                           
                        Label:
                            text: "[b]Faculty of ITEE[/b]\\nThe mission of the ITEE faculty is to  advance internationally top-level  research on information technology and education based on it and  generate new knowledge of information technology and apply it to the needs of the society, people and industries."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 200, 200
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/itee/node/6413")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/tst/node/24248")
                                    
                            Label:
                                text: '[ref=] More Info - Video [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/itee/node/44049")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_datagarage'                    
            
            
            MapMarkerPopup:
                name: 'Zoological_Museum'
                lat: 65.060597
                lon: 25.466931
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "zoological_museum.png"
                           
                        Label:
                            text: "[b]Zoological Museum & Oulu Business School [/b]\\nFab Lab Oulu is a small digital manufacturing working area (fabrication laboratory)  that complies with open innovation concept developed by MIT in the United States."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/oulubusinessschool/studying")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/kauppakorkeakoulu/opiskelu")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_zoological_museum'            
            
            MapMarkerPopup:
                name: 'Balance'
                lat: 65.061035
                lon: 25.468079
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "faculty of humanities.jpg"
                           
                        Label:
                            text: "[b]Faculty of Humanities[/b]\\nThe Faculty of Humanities provided teaching and research in practically all the academic disciplines concerned with achievements in the humanities: history, language and linguistics, cultural studies and literature."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/biodiversityunit/node/16772")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/biodiversiteettiyksikko/node/1372")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_balance'
            
                        
            MapMarkerPopup:
                name: 'Saalasti Hall'
                lat: 65.056928
                lon: 25.468709
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Salastti_hall.png"
                        Label:
                            text: "[b]Saalasti Hall[/b]is the place which graduation ceremonies are held every month"
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/edu/admissions")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/ktk/opiskelijavalinta")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_saalasti_hall'
            
            MapMarkerPopup:
                name: 'KTK112'
                lat: 65.061765
                lon: 25.469892
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Faculty of education.png"
                        Label:
                            text: "[b]The Faculty of Education[/b]\\nis multidisciplinary expert organisation for training, research and development in the field of education and teaching."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/edu/admissions")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/ktk/opiskelijavalinta")
                            
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_faculity_of_education'    
                        
            MapMarkerPopup:
                name: 'Stories'
                lat: 65.058493
                lon: 25.466995
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Faculty of technology and story.png"
                        Label:
                            text: "[b]The Faculty of Technology[/b]\\noperates in the field of Mechanical Engineering Environmental Engineering and Industrial Engineering and Management."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/tech/node/6412")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/ttk/hae")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_stories'
                        
            MapMarkerPopup:
                name: 'L6'
                lat: 65.059941
                lon: 25.466303
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "faculty of science.png"
                        Label:
                            text: "[b]The Faculty of Science[/b]\\nis the second biggest educational unit in Sciences in Finland"
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/university/")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/university/")
                            
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_faculity_of_science'
            MapMarkerPopup:
                name: 'Aava'
                lat:  65.060479
                lon:  25.46656
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "aava and restaurant.png"
                        Label:
                            text: "[b] Restaurant [/b]\\nStudent prices for the meals are: basic student lunch EUR 2.60 soup lunch EUR 2.25 grill portion EUR 4.95 and the special lunch EUR 4.85"
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/university/")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/university/")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
                            font_size: 30
                            on_release: app.root.current = 'question_aava'
            
            MapMarkerPopup:
                name: 'PSOAS'
                lat: 65.05733
                lon: 25.467344
                source: 'info.png'
                popup_size: dp(340), dp(280)
                Bubble:
                    BoxLayout:
                        orientation: "horizontal"
                        padding: "5dp"
                        spacing: 10
                        AsyncImage:
                            source: "Psoas.png"
                           
                        Label:
                            text: "[b]PSOAS[/b]\\nThe main duty of PSOAS is to offer inexpensive living quarters to the areas."
                            markup: True
                            text_size: self.size
                            halign: 'center'
                            valign:'middle'
                            
                            Label:
                                text: '[ref=] More Info in English [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 100
                                align: "center"
                                on_ref_press:
                                    import webbrowser
                                    webbrowser.open("http://www.oulu.fi/university/")   
                                
                            Label:
                                text: '[ref=] More Info In Finnish [/ref]'
                                markup: True
                                color: 1,0,1,1
                                pos: 250, 15
                                align: "center"
                                on_ref_press:
                                    import webbrowser                                
                                    webbrowser.open("http://www.oulu.fi/university/")
                        
                        Button:
                            text: 'Play'
                            size_hint: 0.5, 0.15
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
'''

class ScreenManagerApp(App):

    app_lat = NumericProperty(0)
    app_lon = NumericProperty(0)
    gps_location = StringProperty()
    gps_status = StringProperty('Click Start to get GPS location updates')

    def build(self):
        try:
            gps.configure(on_location=self.on_location,
                          on_status=self.on_status)
        except NotImplementedError:
            import traceback
            traceback.print_exc()
            self.gps_status = 'NO GPS'

        return Builder.load_string(kv)

    def start(self, minTime, minDistance):
        gps.start(minTime, minDistance)

    def stop(self):
        gps.stop()

    @mainthread
    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])
        self.app_lat = kwargs.get('lat')
        self.app_lon = kwargs.get('lon')

    @mainthread
    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def on_pause(self):
        gps.stop()
        return True

    def on_resume(self):
        gps.start(1000, 0)
        pass

if __name__ == '__main__':
    ScreenManagerApp().run()

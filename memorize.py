from kivy.app import App
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.vector import Vector
import random
import time
import sys
from kivy.clock import Clock

class MemorizeGame(GridLayout):
    def __init__(self, **kwargs):
        super(MemorizeGame, self).__init__(**kwargs)
        self.challenge = []
        self.round = 1
        self.cols = 2
        self.userSelectedList = []
        self.userModeEnabled = False

        #create buttons                                                                                                                                                                                                            
        self.button1 = Button(text='', background_color=(0,0,1,1))
        self.button2 = Button(text='', background_color=(0,1,1,1))
        self.button3 = Button(text='', background_color=(1,0,1,1))
        self.button4 = Button(text='', background_color=(0,1,0,1))
        self.startBtn = Button(text='Start Round')
        self.quitBtn = Button(text="Quit")
        self.buttonList = [self.button1, self.button2, self.button3, self.button4]

        self.startBtn.bind(on_press=self.buildChallenge)
        self.quitBtn.bind(on_press=self.quit)

        #add buttons to the screen                                                                                                                                                                                                 
        for button in self.buttonList:
            self.add_widget(button)
            button.bind(on_press=self.getClickedButton)

        self.add_widget(self.startBtn)
        self.add_widget(self.quitBtn)
        Clock.schedule_interval(self.blinkStart, 1 / 1.)

    def blinkSquare(self, targetButton, delay):
        '''
        changes the squares color to 1,1,1,1 then changes it back after .3 seconds.
        delay tells the clock how long ot wait before blinking the next square
        see buildChallenge() for delay usage
        '''
        originalColor = targetButton.background_color
        def set_color(*args):
            targetButton.background_color = (1, 1, 1, 0)
        def reset_color(*args):
            targetButton.background_color = (originalColor)

        Clock.schedule_once(set_color, delay)
        delay += .3
        Clock.schedule_once(reset_color, delay)

    def blinkStart(self, dt):
        if self.userModeEnabled == False:
            self.blinkSquare(self.startBtn, .5)

    def getClickedButton(self, instance):
        #check to see if what the user pressed is the right button
        self.userSelectedList.append(instance)
        self.userModeEnabled = True
        print instance

    def buildChallenge(self, instance):
        delay = 0
        lengthOfChallenge = self.round + 1
        choice = random.choice(self.buttonList)
        self.challenge.append(choice)

        #play the challenge to the player
        print "round:", self.round
        for x in self.challenge:
            delay += .5
            self.blinkSquare(x,delay)
            print x

        self.userMode()

    def compareChallenge(self, dt):
        #This will test the users entry against the challenge array
        #User Mode will be disabled if the user finishes all successfully
        #or if they fail
        x = 0
        roundWon = False
        limit = len(self.challenge)

        if self.userModeEnabled == True:
            for userAnswer in self.userSelectedList:
                if userAnswer == self.challenge[x]:
                    x += 1
                    self.userModeEnabled = True
                else:
                    self.userModeEnabled = False
                    self.gameOver()
                    return False

            #check to see if the challenge is complete
            if x == limit:
                print "Round Won!"
                self.userModeEnabled = False
                roundWon = True
                return False

    def userMode(self):
        #Enable user mode. This is where the user tries to repeat the pattern displayed to him
        self.userModeEnabled = True
        self.userSelectedList = []
        Clock.schedule_interval(self.compareChallenge, 1 / 30.)

    def gameOver(self):
        print "Game Over"
        self.remove_widget(self.startBtn)
        self.remove_widget(self.quitBtn)
        for x in self.buttonList:
            self.remove_widget(x)
        quitButton = Button(text='Quit Game', font_size=14)
        quitButton.bind(on_press=self.quit)
        self.add_widget(quitButton)

    def quit(self, instance):
        sys.exit()


class MemorizeApp(App):

    def build(self):
        self.title = "Memorize"
        game = MemorizeGame()

        return game

if __name__ == "__main__":
    MemorizeApp().run()


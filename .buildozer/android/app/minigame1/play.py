import os.path as op
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.image import Image
from random import randint, shuffle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_string('''
<Game>:
    Menu:
        name: 'menu'
    Play:
        name: 'play'
<Menu@Screen>:
    BoxLayout:
        size_hint: 0.5,0.5
        pos_hint: {'center_x':0.5,'center_y':0.5}
        orientation: 'vertical'
        BoxLayout:
            Label:
                id: cols
                text: '4'
            Label:
                text: 'x'
            Label:
                id: rows
                text: '4'

        Button:
            text: 'Play'
            on_release: root.manager.current = 'play'
            on_release: root.parent.startgame(root.ids.cols, root.ids.rows)
        Button:
            text: 'Exit'
            on_release: exit()
<Play>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: 1, None
            height: min(self.parent.size[0]*0.1,self.parent.size[1]*0.1)
            pos: self.pos[0], self.parent.size[1]-self.size[1]
            Button:
                text: 'Exit'
                on_release: exit()
            Label:
                text: 'Score'
            Label:
                id: score
                text: '0'
            Button:
                text: 'Reset'
                on_release: root.reset()
        FloatLayout:
            GridLayout:
                size_hint: None, None
                width: min(self.parent.size[0]*0.9,self.parent.size[1]*0.9)
                height: self.width
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                spacing: '10dp'
                id: content
<Item>:
    on_release: self.choose(self, self.pair)
''')


class Game(ScreenManager):
    '''Main widget for menu and game screens.'''

    def __init__(self, **kw):
        '''__init__() here is used mostly to let other classes access
        the class itself and its properties/widgets.'''

        self.app = App.get_running_app()
        self.app.game = self
        super(Game, self).__init__(**kw)

    def startgame(self, width, height):
        '''First create a list of random unique numbers in range of
        width*height/2 (i.e. pairs/2). If a random number is already
        in the list, loop over few times until the unique number is found.
        Then duplicate the list, randomize the order of items in new list,
        join these lists and add widgets with unique numbers to
        GridLayout.'''

        x = []
        y = []
        r = int(width.text)*int(height.text)/2
        self.app.r = r
        self.content = self.app.play.ids.content
        for i in xrange(r):
            rand = randint(0, r)
            if rand not in x:
                x.append(rand)
            else:
                for j in xrange(max(len(x), len(x)+20)):
                    specialrand = rand+randint(j*r**2, 10*j*r**2)
                    if specialrand not in x:
                        x.append(specialrand)
                        break
        y = list(x)
        self.content.cols = int(width.text)
        self.content.rows = int(height.text)
        shuffle(y)
        order = x + y
        for i in order:
            self.content.add_widget(Item(pair=i))

    def resetgame(self):
        '''Reset stats, widgets and return to the menu screen.'''

        self.app.selected = -1
        self.app.selitems = []
        self.app.play.ids.score.text = '0'
        self.app.play.ids.content.clear_widgets()
        self.current = 'menu'


class Play(Screen):
    '''An actual game board with simple Score + points labels at the top.
    The size of a square is set directly in kv taking the parent's size
    min(width, height), so it will stay a square regardless of display
    orientation.
    A GridLayout is used because of its good effect on making even
    count of children. FloatLayout only centers the board.'''

    def __init__(self, **kw):
        self.app = App.get_running_app()
        self.app.play = self
        self.reset = self.app.game.resetgame
        super(Play, self).__init__(**kw)


class Item(ButtonBehavior, Image):
    '''The image on the pair grid with default cover picture.'''

    def __init__(self, **kw):
        '''At the beginning a special tint is created from the unique id that
        pairs share so that a player can identificate them. One of five
        shapes is assigned to the item by the remainder of unique pair id
        divided by count of the shapes.'''

        self.app = App.get_running_app()
        self.path = self.app.path
        self.score = self.app.play.ids.score
        self.pair = kw['pair']
        r = self.app.r
        self.srcclose = self.path+'/cover.png'
        self.srcopen = self.path+'/'+str(self.pair % 5)+'.png'
        self.source = self.srcclose
        self.clr = self.tint(r)
        super(Item, self).__init__(**kw)

    def choose(self, widget, pair):
        '''When clicked, real tinted picture takes place instead of cover
        picture, unique id of pairs is placed in a variable and if another
        clicked item shares the same id, pictures will stay opened and score
        increases. Otherwise pictures will change to cover picture and
        variable resets.
        Selected items are placed inside a list for better access.'''

        self.source = self.srcopen
        self.color = self.clr
        if self.app.selected == -1:
            self.app.selected = pair
            self.app.selitems.append(widget)
        else:
            if self not in self.app.selitems:
                self.app.selitems.append(widget)
                if pair == self.app.selected:
                    self.score.text = str(int(self.score.text)+2)
                    for item in self.app.selitems:
                        item.disabled = True
                        # change only alpha, preserve original color
                        item.color = item.color[:3]+[0.8]
                    self.app.selected = -1
                    self.app.selitems = []
                else:
                    self.source = self.srcopen
                    Clock.schedule_once(self.close, 0.5)
            else:
                self.close()

    def close(self, t):
        for item in self.app.selitems:
            item.source = item.srcclose
            item.color = (1, 1, 1, 1)
        self.app.selected = -1
        self.app.selitems = []

    def tint(self, r):
        '''Tint an image'''

        if self.pair < r/3.0:
            return (int(self.pair/255.0)+0.02, 1, 1, 1)
        elif self.pair < 2.0*r/3.0:
            return (1, int(self.pair/255.0)+0.02, 1, 1)
        else:
            return (1, 1, int(self.pair/255.0)+0.02, 1)


class game1(App):
    '''Main class connecting other classes.'''

    selected = -1
    selitems = []
    path = op.dirname(op.abspath(__file__))

    def on_pause(self):
        return True

    def build(self):
        return Game()

if __name__ == '__main__':
   game1().run()
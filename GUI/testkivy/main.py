import kivy
kivy.require('1.9.0')
from cheesepoofs.kerplunk import script

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout

Builder.load_string('''
<Marvel>
  Label:
    id: loki
    text: 'loki: I AM YOUR GOD!'
  Button:
    id: hulk
    text: "press to smash loki"
    on_release: root.hulk_smash()
''')


class Marvel(BoxLayout):

    def hulk_smash(self):
        self.ids.hulk.text = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!"  # alternative syntax
        script.install_script()

class AutoPen(App):
    def build(self):
        with open("tips.txt", "r") as stream:
            labeltext = stream.read()
        label = Label(text=labeltext, markup=True)
        box = BoxLayout()
        marvell = Marvel()
        box.add_widget(marvell)
        box.add_widget(label)
        return box

class Anima(App):
    def build(self):
        floater = FloatLayout()
        self.widget = Button(text='herpderp', pos = (200,200), size_hint=(0.2,0.2))
        self.backbutton = Button(text='back', pos=(0,0), size_hint =(0.1,0.2))
        self.widget.bind(on_press=self.animate)
        self.backbutton.bind(on_press=self.back)
        floater.add_widget(self.widget)
        floater.add_widget(self.backbutton)
        return floater

    def animate(self, widgetself):
        anim = Animation(x=100, y=100)
        anim.start(self.widget)

    def back(self,widgetself):
        anim = Animation(x=200,y=200)
        anim.start(self.widget)

if __name__ == "__main__":
    AutoPen().run()






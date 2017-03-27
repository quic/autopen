import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class AutoPen(App):

    def build(self):
        mainpage = FloatLayout()
        car = Image(source='file.gif')

        dropdown = DropDown()
        btn = Button(text='cheese puffs and cowbells', size_hint_y=None, height=24)
        btn.bind(on_release=lambda btn: dropdown.select(btn.text))
        dropdown.add_widget(btn)
        btn2 = Button(text='froofy noopers', size_hint_y=None, height=24)
        btn2.bind(on_release=lambda btn2: dropdown.select(btn.text))
        dropdown.add_widget(btn2)
        dropdownception = DropDown()
        btn3 = Button(text='i am your father', size_hint_y=None, height=24, pos=(30,30))
        btn3.bind(on_release=lambda btn3: dropdown.select(btn.text))
        dropdownception.add_widget(btn3)
        btn2.bind(on_release=dropdownception.open)

        canbutton = Button(text='hello', size_hint=(0.2, 0.12), border=(20, 20, 20, 20), pos_hint={'top':0.9, 'right':0.2}, font_size='20sp')
        canbutton.bind(on_release=dropdown.open)

        dropdown = DropDown()
        for index in range(10):
            btn1 = Button(text='cheese puffs and cowbells', size_hint_y=None, height=24)
            btn1.bind(on_release=lambda btn1: dropdown.select(btn1.text))
            dropdown.add_widget(btn1)
        wifibutton = Button(text='hello', size_hint=(0.2, 0.12), border=(20, 20, 20, 20), pos_hint={'top':0.2, 'right':0.2}, font_size='20sp')
        wifibutton.bind(on_release=dropdown.open)

        mainpage.add_widget(car)
        mainpage.add_widget(canbutton)
        mainpage.add_widget(wifibutton)
        return mainpage

if __name__ == "__main__":
    AutoPen().run()
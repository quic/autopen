import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

from kivy.uix.label import Label

from kivy.lang import Builder


Builder.load_string('''
<Container>:
	FloatLayout:
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size

<OtherGoodies>:
	ListItemButton:
		selected_color: 0.5, 0.5, 0.5, 1
		deselected_color: 0.7, 0.7, 0.7, 1


''')

#:layout FloatLayout()



class AutoPen(App):
	def build(self):

		self.mainpage = FloatLayout()

		#btn = Button(text='Back', on_release=self.callback, size_hint=(0.15, 0.1), pos_hint={'x': 0, 'y': .9})
		car = Image(source='AutoPen.png')


		def canPage(instance):
			self.mainpage.remove_widget(can)
			self.mainpage.remove_widget(wifi)
			self.mainpage.remove_widget(bluetooth)
			self.mainpage.remove_widget(SDR)

			#l = Label(text='CAN Tools', font_size='20sp', halign='left', valign='top', size=(2,2))
			can_title = Button(text='CAN Tools', size_hint=(.2,.1), pos_hint={'x':.1,'y':.85}, background_color=[1,0,1,0])
			self.mainpage.add_widget(can_title)

			canutils = Button(text='Canutils', size_hint=(.2,.1), pos_hint={'x':.1,'y':.75})
			c0f = Button(text='c0f', size_hint=(.2,.1), pos_hint={'x':.1, 'y':.65})
			kayak = Button(text='Kayak', size_hint=(.2,.1), pos_hint={'x':.1, 'y':.55})

			self.mainpage.add_widget(canutils)
			self.mainpage.add_widget(c0f)
			self.mainpage.add_widget(kayak)




		#def MainPage(self):

		can = Button(text='CAN', size_hint=(.2, .1), pos_hint={'x':.1, 'y':.2})
		wifi = Button(text='Wi-fi', size_hint=(.2, .1), pos_hint = {'x':.1, 'y':.6})
		bluetooth = Button(text='Bluetooth', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.2})
		SDR = Button(text='SDR', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.6})
		back = Button(text='Back', size_hint=(.1,.05), pos_hint={'x':0, 'y':0})

		#adding buttons to main tools
		self.mainpage.add_widget(can)
		self.mainpage.add_widget(wifi)
		self.mainpage.add_widget(bluetooth)
		self.mainpage.add_widget(SDR)

		can.bind(on_press=canPage)

		return self.mainpage


#layout.add_widget(MainToolsScreen())

if __name__ == "__main__":
	AutoPen().run()


#def main_page():
	#main tools buttons
'''

<MainToolsScreen>:
	FloatLayout:
		Button:
			id: 'can'
			text: 'CAN'
			size_hint: (.2, .1)
			pos_hint: {'x':.1, 'y':.2}
			on_release: root.callback()
		Button: 
			id: 'wifi'
			text: 'Wi-fi'
			size_hint: (.2, .1)
			pos_hint: {'x':.1, 'y':.6}
'''




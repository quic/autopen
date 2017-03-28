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

	'''
	def __init__(self, **kwargs):
		super(App, self).__init__(**kwargs)
		with self.canvas:
			welcome = Label(text='Welcome to Autopen', size_hint=(.6,.3), pos_hint={'x':.2,'y':.7}, background_color=[1,0,1,0])
			self.mainpage.add_widget(welcome)
	'''

	def build(self):

		self.mainpage = FloatLayout()

		#btn = Button(text='Back', on_release=self.callback, size_hint=(0.15, 0.1), pos_hint={'x': 0, 'y': .9})
		car = Image(source='AutoPen.png')


		def MainPage(instance):
			self.mainpage.clear_widgets()	#going to have to overwrite this function later
			self.can = Button(text='CAN', size_hint=(.2, .1), pos_hint={'x':.1, 'y':.2})
			self.wifi_SDR = Button(text='Wi-fi/SDR', size_hint=(.2, .1), pos_hint = {'x':.1, 'y':.6})
			self.bluetooth = Button(text='Bluetooth', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.2})
			self.miscellaneous = Button(text='Miscellaneous', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.6})
			self.back = Button(text='Back', size_hint=(.1,.05), pos_hint={'x':0, 'y':0})

			#adding buttons to main tools
			self.mainpage.add_widget(self.can)
			self.mainpage.add_widget(self.wifi_SDR)
			self.mainpage.add_widget(self.bluetooth)
			self.mainpage.add_widget(self.miscellaneous)
			self.mainpage.add_widget(self.back)

			self.can.bind(on_press=canPage)
			self.bluetooth.bind(on_press=bluetoothPage)
			self.wifi_SDR.bind(on_press=wifi_SDRPage)
			self.miscellaneous.bind(on_press=miscellaneousPage)


		def databasePage(instance):
			self.mainpage.remove_widget(self.welcome)
			self.mainpage.remove_widget(self.database)
			self.mainpage.remove_widget(self.tools)

			database_title = Button(text='Database', size_hint=(.6,.3), pos_hint={'x':.2,'y':.7}, background_color=[1,0,0,1])
			self.mainpage.add_widget(database_title)

			cont = Button(text='Continue', size_hint=(.1,.05), pos_hint={'x':.9, 'y':0})
			self.mainpage.add_widget(cont)
			cont.bind(on_press=MainPage)

		self.welcome = Button(text='Welcome to Autopen', size_hint=(.6,.3), pos_hint={'x':.2,'y':.7}, background_color=[1,0,1,1])
		self.mainpage.add_widget(self.welcome)

		self.howto = Button(text='How-To', size_hint=(.3,.1), pos_hint={'x':.3, 'y':.4})
		self.tools = Button(text='Search', size_hint=(.3,.1), pos_hint={'x':.3, 'y':.3})
		self.terms = Button(text='Terms and Conditions', size_hint=(.3,.1), pos_hint={'x':.3, 'y':.2})

		self.mainpage.add_widget(self.howto)
		self.mainpage.add_widget(self.tools)
		self.mainpage.add_widget(self.terms)

		self.database = Button(text='Register Vehicle', size_hint=(.3,.1), pos_hint={'x':.3, 'y':.6})
		self.mainpage.add_widget(self.database)
		self.database.bind(on_press=databasePage)

		self.tools = Button(text='Tools', size_hint=(.3,.1), pos_hint={'x':.3, 'y':.5})
		self.mainpage.add_widget(self.tools)
		self.tools.bind(on_press=MainPage)



		def canPage(instance):
			self.mainpage.remove_widget(self.can)
			self.mainpage.remove_widget(self.wifi_SDR)
			self.mainpage.remove_widget(self.bluetooth)
			self.mainpage.remove_widget(self.miscellaneous)

			tools_title = Button(text='Tools', size_hint=(.6,.3), pos_hint={'x':.2,'y':.8}, background_color=[1,0,1,0])
			self.mainpage.add_widget(tools_title)

			#l = Label(text='CAN Tools', font_size='20sp', halign='left', valign='top', size=(2,2))
			can_title = Button(text='CAN Tools', size_hint=(.2,.1), pos_hint={'x':.05,'y':.85}, background_color=[1,0,0,0.5])
			self.mainpage.add_widget(can_title)

			canutils = Button(text='Can-utils', size_hint=(.2,.1), pos_hint={'x':.05,'y':.75})
			canbus_utils = Button(text='Canbus-utils', size_hint=(.2,.1), pos_hint={'x':.05,'y':.65})
			kayak = Button(text='Kayak', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.55})
			caringcaribou = Button(text='Caring Caribou', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.45})
			c0f = Button(text='c0f', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.35})
			UDSim = Button(text='UDSim', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.25})
			DO = Button(text='PyOBD',size_hint=(.2,.1), pos_hint={'x':.05,'y':.15})
			O2OO = Button(text='O2OO', size_hint=(.2,.1), pos_hint={'x':.05, 'y':.05})



			self.mainpage.add_widget(canutils)
			self.mainpage.add_widget(canbus_utils)
			self.mainpage.add_widget(c0f)
			self.mainpage.add_widget(kayak)
			self.mainpage.add_widget(caringcaribou)
			self.mainpage.add_widget(UDSim)
			self.mainpage.add_widget(DO)
			self.mainpage.add_widget(O2OO)

			self.back.bind(on_press=MainPage)

		def bluetoothPage(instance):
			self.mainpage.remove_widget(self.can)
			self.mainpage.remove_widget(self.wifi_SDR)
			self.mainpage.remove_widget(self.bluetooth)
			self.mainpage.remove_widget(self.miscellaneous)

			tools_title = Button(text='Tools', size_hint=(.6,.3), pos_hint={'x':.2,'y':.8}, background_color=[1,0,1,0])
			self.mainpage.add_widget(tools_title)

			bluetooth_title = Button(text='Bluetooth Tools', size_hint=(.25,.1), pos_hint={'x':.05,'y':.85}, background_color=[1,0,1,0])
			self.mainpage.add_widget(bluetooth_title)

			bluelog = Button(text='Bluelog', size_hint=(.25,.1), pos_hint={'x':.05,'y':.75})
			bluemaho = Button(text='Bluemaho', size_hint=(.25,.1), pos_hint={'x':.05,'y':.65})
			btscanner = Button(text='BTScanner', size_hint=(.25,.1), pos_hint={'x':.05, 'y':.55})
			bluetooth_tools = Button(text='Bluetooth Tools Package', size_hint=(.25,.1), pos_hint={'x':.05, 'y':.45})

			self.mainpage.add_widget(bluelog)
			self.mainpage.add_widget(bluemaho)
			self.mainpage.add_widget(btscanner)
			self.mainpage.add_widget(bluetooth_tools)

			self.back.bind(on_press=MainPage)

		def wifi_SDRPage(instance):
			self.mainpage.remove_widget(self.can)
			self.mainpage.remove_widget(self.wifi_SDR)
			self.mainpage.remove_widget(self.bluetooth)
			self.mainpage.remove_widget(self.miscellaneous)

			tools_title = Button(text='Tools', size_hint=(.6,.3), pos_hint={'x':.2,'y':.8}, background_color=[1,0,1,0])
			self.mainpage.add_widget(tools_title)

			title = Button(text='Wi-fi/SDR Tools', size_hint=(.25,.1), pos_hint={'x':.05,'y':.85}, background_color=[1,0,1,0])
			self.mainpage.add_widget(title)

			aircrack = Button(text='Aircrack-ng', size_hint=(.25,.1), pos_hint={'x':.05,'y':.75})
			gnuradio = Button(text='GNU Radio', size_hint=(.25,.1), pos_hint={'x':.05,'y':.65})

			self.mainpage.add_widget(aircrack)
			self.mainpage.add_widget(gnuradio)

			self.back.bind(on_press=MainPage)

		def miscellaneousPage(instance):
			self.mainpage.remove_widget(self.can)
			self.mainpage.remove_widget(self.wifi_SDR)
			self.mainpage.remove_widget(self.bluetooth)
			self.mainpage.remove_widget(self.miscellaneous)

			tools_title = Button(text='Tools', size_hint=(.6,.3), pos_hint={'x':.2,'y':.8}, background_color=[1,0,1,0])
			self.mainpage.add_widget(tools_title)

			miscel_title = Button(text='Miscellaneous Tools', size_hint=(.25,.1), pos_hint={'x':.05,'y':.85}, background_color=[1,0,1,0])
			self.mainpage.add_widget(miscel_title)

			katoolin = Button(text='Katoolin', size_hint=(.25,.1), pos_hint={'x':.05,'y':.75})
			romraider = Button(text='Romraider', size_hint=(.25,.1), pos_hint={'x':.05,'y':.65})

			self.mainpage.add_widget(katoolin)
			self.mainpage.add_widget(romraider)

			self.back.bind(on_press=MainPage)

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




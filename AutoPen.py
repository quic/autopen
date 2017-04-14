import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

import install
import open_
from text import *

Builder.load_string("""

<WelcomePage>:
	id: welcome 
	FloatLayout:
		id: welcome_float
		canvas.before:
			Rectangle:
				source: 'welcome_background.jpg'
				pos: self.pos
				size: self.size
		Label:
			id: autopen
			text: '[i][b][color=3388dd]Welcome to Autopen![/color][/b][/i]'
			markup: True
			font_size: '35sp'
			text_size: (500,300)
			pos_hint: {'x':0.5, 'y':0.9}
			size_hint: None, None
		Button:
			text: 'Tools'
			size_hint: .25, .1
			pos_hint: {'x':.55, 'y':.5}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'tools'
		Button:
			text: 'How-To'
			size_hint: .25, .1
			pos_hint: {'x':.55, 'y':.4}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'howto'
		Button:
			text: 'About AutoPen'
			size_hint: .25, .1
			pos_hint: {'x':.55, 'y':.3}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'about'
		Button:
			text: 'Terms and Conditions'
			size_hint: .25, .1
			pos_hint: {'x':.55, 'y':.2}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'terms'

<ToolsPage>:
	id: tools_main
	FloatLayout:
		id: main_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		Label:
			text: '[i][b][color=3388dd]Tools[/color][/b][/i]'
			underline: True
			markup: True
			font_size: '40sp'
			size_hint: .25, .1
			pos_hint: {'x': .4, 'y': .8}

		Button:
			text: 'CAN'
			size_hint: .25, .1
			pos_hint: {'x':.1, 'y':.6}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'can'
		Button:
			text: 'Bluetooth/Wi-fi'
			size_hint: .25, .1
			pos_hint: {'x':.7, 'y':.2}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'bw'
		Button:
			text: 'SDR'
			size_hint: .25, .1
			pos_hint: {'x':.7, 'y':.6}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'sdr'
		Button:
			text: 'Miscellaneous'
			size_hint: .25, .1
			pos_hint: {'x':.1, 'y':.2}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'miscellaneous'
		Button:
			id: seeall
			text: 'See All Tools'
			size_hint: .25, .1
			pos_hint: {'x':.40, 'y':0.05}
			on_press:
				root.manager.transition.direction = "left"
				root.manager.transition.duration = .5
				root.manager.current = "seeall"
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "welcome"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}
		TextInput:
			id: search
			multiline: False
			keyboard_suggestions: True
			focus: True
			pos_hint: {'x':.65, 'top':0.99}
			size_hint: (0.24,0.05)
		Button:
			id: searchbutton
			text: 'Search Tools'
			font_size: 10
			pos_hint: {'x':.89, 'top':0.99}
			size_hint: (0.1,0.05)
			on_press: root.find()

		Image:
			source: "AutoPenBlack.png"
			size_hint: 0.1,0.1
			pos_hint: {'x':0, 'y':0.88}

<CanPage>:
	id: can_main
	FloatLayout:
		id: can_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			id: bt_box
			orientation: 'vertical'
			spacing: 10
			padding: [5,5,5,60]
			Label:
				text: '[i][b][color=3388dd]CAN Tools[/color][/b][/i]'
				underline: True
				markup: True
				font_size: '25sp'
				size_hint: .25, .1
			Button:
				id: can_utils
				text: 'CAN-utils'
				size_hint: .25, .1
				on_release: root.can_utils()
			Button:
				id: canbus_utils
				text: 'CANbus-utils'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: can_utils_x
				text: 'CAN-utils-X'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: can_utils_j1939
				text: 'CAN-utils-j1939'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: canbadger
				text: 'CANBadger'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: caring_caribou
				text: 'Caring Caribou'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: kayak
				text: 'Kayak'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: c0f
				text: 'c0f'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: udsim
				text: 'UDSim'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: pyobd
				text: 'PyOBD'
				size_hint: .25, .1
				on_press: root.can()
			Button:
				id: o2oo
				text: 'O2OO'
				size_hint: .25, .1
				on_press: root.can()
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "tools"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}
		ScrollableLabel:
			pos_hint:{'x': 0.28, 'top': 0.9}
			size_hint: (0.35, 0.7)
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
		ScrollableLabel:
			pos_hint:{'x': 0.65, 'top': 0.9}
			size_hint:(0.3,0.7)
			Label:
				id: label2
				size_hint_y: None
				height: label2.texture_size[1]
				text_size: label2.width, None
				text: ''
				font_size: 14
				markup: True
				valign:'middle'

<BluetoothWifiPage>:
	id: bt_main
	FloatLayout:
		id: bt_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			id: bt_box
			orientation: 'vertical'
			spacing: 10
			padding: [5,5,5,60]
			Label:
				text: '[i][b][color=3388dd]Bluetooth/Wifi Tools[/color][/b][/i]'
				underline: True
				markup: True
				font_size: '20sp'
				size_hint: .25, .1
			Button:
				text: 'aircrack-ng'
				size_hint: .25, .1
			Button:
				text: 'Bluelog'
				size_hint: .25, .1
			Button:
				text: 'Bluemaho'
				size_hint: .25, .1
			Button:
				text: 'BTscanner'
				size_hint: .25, .1
			Button:
				text: 'Bluetooth Tools Package'
				size_hint: .25, .1
			Button:
				text: 'tshark'
				size_hint: .25, .1
			Button:
				text: 'Wireshark'
				size_hint: .25, .1
				on_press: root.wireshark()

		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "tools"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}
		ScrollableLabel:
			pos_hint:{'x': 0.28, 'top': 0.9}
			size_hint:0.35, 0.7
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
		ScrollableLabel:
			pos_hint:{'x': 0.65, 'top': 0.9}
			size_hint:(0.3,0.7)
			Label:
				id: label2
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'

<SDRPage>:
	id: sdr_main
	FloatLayout:
		id: sdr_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			orientation: 'vertical'
			spacing: 10
			padding: [5,5,5,60]
			Label:
				text: '[i][b][color=3388dd]SDR[/color][/b][/i]'
				underline: True
				markup: True
				font_size: '25sp'
				size_hint: .25, .1
			Button:
				text: 'GNU Radio'
				size_hint: .25, .1
			Button:
				text: 'gqrx'
				size_hint: .25, .1
			Button:
				text: ''
				background_color: 0,0,0,0
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "tools"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}
		ScrollableLabel:
			pos_hint:{'x': 0.28, 'top': 0.9}
			size_hint:0.35, 0.7
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
		ScrollableLabel:
			pos_hint:{'x': 0.65, 'top': 0.9}
			size_hint:(0.3,0.7)
			Label:
				id: label2
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
<MiscellaneousPage>
	id: mis
	FloatLayout:
		id: mis_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		BoxLayout:
			orientation: 'vertical'
			spacing: 10
			padding: [5,5,5,60]
			Label:
				text: '[i][b][color=3388dd]Miscellaneous[/color][/b][/i]'
				underline: True
				markup: True
				font_size: '25sp'
				size_hint: .25, .1
			Button:
				text: 'Katoolin'
				size_hint: .25, .1
			Button:
				text: 'Dojge'
				size_hint: .25, .1
			Button:
				text: ''
				background_color: 0,0,0,0
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "tools"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}
		ScrollableLabel:
			pos_hint:{'x': 0.28, 'top': 0.9}
			size_hint:0.35, 0.7
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
		ScrollableLabel:
			pos_hint:{'x': 0.65, 'top': 0.9}
			size_hint:(0.3,0.7)
			Label:
				id: label2
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: ''
				font_size: 20
				markup: True
				valign:'middle'
<SeeAllPage>:
	id: seeall
	FloatLayout:
		id: seeall_float
		canvas.before:
			Rectangle:
				source: 'background.jpg'
				pos: self.pos
				size: self.size
		Label:
			text: '[i][b][color=3388dd]All Tools[/color][/b][/i]'
			underline: True
			markup: True
			font_size: '25sp'
			size_hint: .25, .1
			pos_hint: {'x': .35, 'y': .9}
		GridLayout:
			cols: 3
			rows: 8
			spacing: 10
			padding: [50,50,50,90]
			Button:
				text: 'O2OO'
				size_hint: .30, .1
			Button:
				text: 'aircrack-ng'
				size_hint: .30, .1
			Button:
				text: 'Bluelog'
				size_hint: .30, .1
			Button:
				text: 'Bluemaho'
				size_hint: .30, .1
			Button:
				text: 'Bluetooth Tools Package'
				size_hint: .30, .1
			Button:
				text: 'BTscanner'
				size_hint: .30, .1
			Button:
				text: 'c0f'
				size_hint: .30, .1
			Button:
				text: 'CANBadger'
				size_hint: .30, .1
			Button:
				text: 'CANbus-utils'
				size_hint: .30, .1
			Button:
				text: 'CAN-utils'
				size_hint: .30, .1
			Button:
				text: 'CAN-utils-j1939'
				size_hint: .30, .1
			Button:
				text: 'CAN-utils-X'
				size_hint: .30, .1
			Button:
				text: 'Caring Caribou'
				size_hint: .30, .1
			Button:
				text: 'Dojge'
				size_hint: .30, .1
			Button:
				text: 'GNU Radio'
				size_hint: .30, .1
			Button:
				text: 'gqrx'
				size_hint: .30, .1
			Button:
				text: 'Katoolin'
				size_hint: .30, .1
			Button:
				text: 'Kayak'
				size_hint: .30, .1
			Button:
				text: 'PyOBD'
				size_hint: .30, .1
			Button:
				text: 'tshark'
				size_hint: .30, .1
			Button:
				text: 'UDSim'
				size_hint: .30, .1
			Button:
				text: 'Wireshark'
				size_hint: .30, .1

		Button:
			text: 'Install'
			size_hint: .25, .1
			pos_hint: {'x':.3, 'y': .1}

		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "tools"
		Button:
			id: help
			text: 'Help'
			size_hint: .1, .05
			pos_hint: {'x':.9, 'y':0}

""")

class ScrollableLabel(ScrollView):
	text = StringProperty('')

class WelcomePage(Screen):
	pass

class HowTo(Screen):
	pass

class About(Screen):
	pass

class Terms(Screen):
	pass

class ToolsPage(Screen):

	def find(self):	#doing this atm, but will fix functionality later
		t = (self.ids['search'].text).lower()
		can = ['o2oo', 'c0f', 'canbadger', 'canbus-utils', 'can-utils', 'can-utils-j1939', 'can-utils-x', 'caring caribou', 'pyobd', 'kayak', 'udsim']
		b_w = ['aircrack-ng', 'bluelog', 'bluemaho', 'bluetooth tools', 'btscanner', 'tshark', 'wireshark']
		sdr = ['gnu radio', 'gqrx']
		mis = ['katoolin']
		
		if t in can:
			screen_manager.current = 'can'
		elif t in b_w:
			screen_manager.current = 'bw'
		elif t in sdr:
			screen_manager.current = 'sdr'
		elif t in mis:
			screen_manager.current = 'miscellaneous'
	
		#make it pop up suggestions?		
	pass

class CanPage(Screen):

	def can_utils(widget):

		def open_callback(self):	#this functionality will be a little different
			box = FloatLayout()
			box.add_widget(Label(text='Candump', size_hint=(.25,.1), pos_hint={'x':0,'y':.8}))
			box.add_widget(TextInput(text=u'enter the name of interface', multiline=False, font_size=10,  size_hint=(.75, .1), pos_hint={'x':.25, 'y':.8}))
			box.add_widget(Label(text='Canread', size_hint=(.25,.1)))

			#asc2log, bcmserver, canbusload, can-calc-bit-timing, candump, canfdtest, cangen, cangw, canlogserver, canplayer, cansend, cansniffer, isotpdump, isotprecv, isotpperf, isotpsend, isotpserver, isotpsniffer, isotptun, log2asc, log2long, slcan_attach, slcand and slcanpty

			popup = Popup(title='Please Select a program to run', content=box, size_hint=(.5, .5), size=(400,400))
			popup.open()

			rc_o = install.test('open')
			print (rc_o)

		def install_callback(self):
			rc_i = install.test('water')
			if rc_i == 0:
				widget.remove_widget(i)
				o = Button(text='Open', size_hint= (.20, .075), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				u = Button(text= 'Update', size_hint= (.20,.075), pos_hint= {'x':.5, 'y':.075}, background_color=[0,0,1,.65])
				widget.add_widget(o)
				widget.add_widget(u)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		i = Button(text='Install', size_hint= (.20, .075), pos_hint= {'x':.4, 'y':.075})
		widget.add_widget(i)
		i.bind(on_press=install_callback)

		with open("text/canutilsx.txt", "r") as stream:
			labeltext1 = stream.read()
		widget.ids["label1"].text = labeltext1
		with open("text/canutilsxexample.txt", "r") as stream:
			labeltext2 = stream.read()
		widget.ids["label2"].text = labeltext2


		#with open('installed.txt', 'r') as stream:
		#	tls = stream.readlines()
		#if 'can_utils' in tls:
		#	widget.remove_widget(i)	
		#	o = Button(text='Open', size_hint= (.25, .1), pos_hint= {'x':.3, 'y':.1}, background_color=[0,1,0,.65])#this should be green
		#	u = Button(text= 'Update', size_hint= (.25,.1), pos_hint= {'x':.4, 'y':.1})

	pass


class BluetoothWifiPage(Screen):

	def wireshark(widget):
		def callback(self):
			install.install('wireshark')

		i = Button(text='Install', size_hint= (.15, .05), pos_hint= {'x':.3, 'y':.1})
		o = Button(text='Open', size_hint=(.15, .05), pos_hint={'x':.5, 'y':.1})
		widget.add_widget(i)
		widget.add_widget(o)
		i.bind(on_press=callback)

	pass

class SDRPage(Screen):
	pass

class MiscellaneousPage(Screen):
	pass

class SeeAllPage(Screen):
	pass


screen_manager = ScreenManager()
screen_manager.add_widget(WelcomePage(name='welcome'))
screen_manager.add_widget(ToolsPage(name='tools'))
screen_manager.add_widget(HowTo(name='howto'))
screen_manager.add_widget(About(name='about'))
screen_manager.add_widget(Terms(name='terms'))
screen_manager.add_widget(BluetoothWifiPage(name='bw'))
screen_manager.add_widget(CanPage(name='can'))
screen_manager.add_widget(SDRPage(name='sdr'))
screen_manager.add_widget(MiscellaneousPage(name='miscellaneous'))
screen_manager.add_widget(SeeAllPage(name='seeall'))
class potentApp(App):

	def build(self):

		title = 'AutoPen'

		return screen_manager

if __name__ == "__main__":
	potentApp().run()

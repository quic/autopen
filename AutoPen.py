import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.properties import OptionProperty

#import install_basics
import install
import open_
import uninstall
#from text import *

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
				id: can-utils
				text: 'CAN-utils'
				size_hint: .25, .1
				on_release: root.can('can-utils')
			Button:
				id: canbus-utils
				text: 'CANbus-utils'
				size_hint: .25, .1
				on_press: root.can('canbus-utils')
			Button:
				id: can-utils-x
				text: 'CAN-utils-X'
				size_hint: .25, .1
				on_press: root.can('can-utils-x')
			Button:
				id: j1939
				text: 'CAN-utils-j1939'
				size_hint: .25, .1
				on_press: root.can('j1939')
			Button:
				id: canbadger-hw
				text: 'CANBadger-HW'
				size_hint: .25, .1
				on_press: root.can('canbadger-hw')
			Button:
				id: canbadger-sw
				text: 'CANBadger-SW'
				size_hint: .25, .1
				on_press: root.can('canbadger-sw')
			Button:
				id: caringcaribou
				text: 'Caring Caribou'
				size_hint: .25, .1
				on_press: root.can('caringcaribou')
			Button:
				id: kayak
				text: 'Kayak'
				size_hint: .25, .1
				on_press: root.can('kayak')
			Button:
				id: c0f
				text: 'c0f'
				size_hint: .25, .1
				on_press: root.can('c0f')
			Button:
				id: udsim
				text: 'UDSim'
				size_hint: .25, .1
				on_press: root.can('udsim')
			Button:
				id: pyobd
				text: 'PyOBD'
				size_hint: .25, .1
				on_press: root.can('pyobd')
			Button:
				id: o2oo
				text: 'O2OO'
				size_hint: .25, .1
				on_press: root.can('o2oo')
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
				on_press: root.bw('aircrack-ng')
			Button:
				text: 'Bluelog'
				size_hint: .25, .1
				on_press: root.bw('bluelog')
			Button:
				text: 'Bluemaho'
				size_hint: .25, .1
				on_press: root.bw('bluemaho')
			Button:
				text: 'BTscanner'
				size_hint: .25, .1
				on_press: root.bw('btscanner')
			Button:
				text: 'bluez Package'
				size_hint: .25, .1
				on_press: root.bw('bluez')
			Button:
				text: 'tshark'
				size_hint: .25, .1
				on_press: root.bw('tshark')
			Button:
				text: 'Wireshark'
				size_hint: .25, .1
				on_press: root.bw('wireshark')

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
				on_press: root.sdr('gnuradio')
			Button:
				text: 'gqrx'
				size_hint: .25, .1
				on_press: root.sdr('gqrx')
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
				on_press: root.mis('katoolin')
			Button:
				text: 'Tio'
				size_hint: .25, .1
				on_press: root.mis('tio')
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
			padding: [90,90,90,90]
			ToggleButton:
				id: 'o2oo'
				text: 'O2OO'
				size_hint: .30, .1
			ToggleButton:
				id: 'aircrack-ng'
				text: 'aircrack-ng'
				size_hint: .30, .1
			ToggleButton:
				text: 'Bluelog'
				size_hint: .30, .1
			ToggleButton:
				text: 'Bluemaho'
				size_hint: .30, .1
			ToggleButton:
				text: 'bluez Package'
				size_hint: .30, .1
			ToggleButton:
				text: 'BTscanner'
				size_hint: .30, .1
			ToggleButton:
				text: 'c0f'
				size_hint: .30, .1
			ToggleButton:
				text: 'CANBadger-HW'
				size_hint: .30, .1
			ToggleButton:
				text: 'CANBadger-SW'
			ToggleButton:
				text: 'CANbus-utils'
				size_hint: .30, .1
			ToggleButton:
				text: 'CAN-utils'
				size_hint: .30, .1
			ToggleButton:
				text: 'CAN-utils-j1939'
				size_hint: .30, .1
			ToggleButton:
				text: 'CAN-utils-X'
				size_hint: .30, .1
			ToggleButton:
				text: 'Caring Caribou'
				size_hint: .30, .1
			ToggleButton:
				text: 'Dojge'
				size_hint: .30, .1
			ToggleButton:
				text: 'GNU Radio'
				size_hint: .30, .1
			ToggleButton:
				text: 'gqrx'
				size_hint: .30, .1
			ToggleButton:
				text: 'Katoolin'
				size_hint: .30, .1
			ToggleButton:
				text: 'Kayak'
				size_hint: .30, .1
			ToggleButton:
				text: 'PyOBD'
				size_hint: .30, .1
			ToggleButton:
				text: 'tshark'
				size_hint: .30, .1
			ToggleButton:
				text: 'UDSim'
				size_hint: .30, .1
			ToggleButton:
				text: 'Wireshark'
				size_hint: .30, .1
		Button:
			text: 'Install'
			size_hint: .3, .07
			pos_hint: {'x':.35, 'y': .05}
			on_press: root.install_all()
		Button:
			text: 'Install All'
			size_hint: .3, .07
			pos_hint: {'x':.65, 'y': .05}
			on_press: root.install_all()

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


try:
	already_installed = open('installed.txt', 'r')
	installed_tools = []
	for i in already_installed.readlines():
		installed_tools.append(i.strip('\n'))
except FileNotFoundError:
	pass

can = ['o2oo', 'c0f', 'canbadger-hw', 'canbadger-sw', 'canbus-utils', 'can-utils', 'can-utils-j1939', 'can-utils-x', 'caringcaribou', 'pyobd', 'kayak', 'udsim']
b_w = ['aircrack-ng', 'bluelog', 'bluemaho', 'bluez', 'btscanner', 'tshark', 'wireshark']
sdr = ['gnu radio', 'gqrx']
mis = ['katoolin']

maybe = []


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

	def can(widget, value):

		v = value

		print (installed_tools)

		for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
			if i in can:
				widget.ids[i].background_color = [1,1,1,.65]


		if v == 'can-utils-x':
			with open("canutilsx.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("canutilsx_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'canbadger':
			with open("canbadger.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("canbadger_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'kayak':
			with open("kayak.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("kayak_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'udsim':
			with open("udsim.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("udsim_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'pyobd':
			with open("pyobd.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("pyobd_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'o2oo':
			with open("o2oo.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("o2oo_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'c0f':
			with open("c0f.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("c0f_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'can-utils':
			with open("canutils.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("canutils_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'canbus-utils':
			with open("canbus_utils.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("canbus_utils_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'caringcaribou':
			with open("caringcaribou.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("caringcaribou_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'j1939':
			with open("j1939.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("j1939_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2



		#opens the tool on enter with the appropriate arguments
		def open_callback(self):
			if v == 'can-utils-x':
				rc_o = open_.test('can-utils-x')
			elif v == 'canbadger':
				rc_o = open_.test('canbadger-hw')
			elif v == 'canbadger-sw':
				rc_o = open_.test('canbadger-sw')
			elif v == 'kayak':
				rc_o = open_.test('kayak')
			elif v == 'udsim':
				rc_o = open_.test('udsim')
			elif v == 'pyobd':
				rc_o = open_.test('pyobd')
			elif v == 'o2oo':
				rc_o = open_.test('o2oo')
			elif v == 'c0f':
				rc_o = open_.test('c0f')
			elif v == 'can-utils':
				rc_o = open_.test('can-utils')
			elif v == 'canbus-utils':
				rc_o = open_.test('canbus-utils')
			elif v == 'caringcaribou':
				rc_o = open_.test('caringcaribou')
			elif v == 'j1939':
				rc_o = open_.test('j1939')

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def uninstall_callback(self):
			rc_u = uninstall.test(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.remove_widget(o)
				widget.remove_widget(up)
				widget.remove_widget(un)
				widget.add_widget(i)

		#this if the function that executes when install in pressed
		def install_callback(self): 
			rc_i = install.test(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.add_widget(o)
				widget.add_widget(up)
				widget.add_widget(un)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'


		if v in installed_tools:
			widget.ids[v].background_color = [1,1,1,.65]

			o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
			o.bind(on_press=open_callback)
			up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
			un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
			un.bind(on_press=uninstall_callback)

			widget.add_widget(o)
			widget.add_widget(up)
			widget.add_widget(un)
		else:
			i = Button(text='Install', size_hint= (.20, .075), pos_hint= {'x':.4, 'y':.075})
			widget.add_widget(i)
			i.bind(on_press=install_callback)


	pass


class BluetoothWifiPage(Screen):

	def bw(widget, value):	#for buttons that do not use a popup

		v = value

		if v == 'aircrack-ng':
			with open("aircrack_ng.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("aircrack_ng_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'bluelog':
			with open("bluelog.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("bluelog_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'bluemaho':
			with open("bluemaho.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("bluemaho.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'btscanner':
			with open("btscanner.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("btscanner_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'package':
			with open("package.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("package_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'tshark':
			with open("tshark.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("tshark_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'wireshark':
			with open("wireshark.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("wireshark_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		#opens the tool on enter with the appropriate arguments
		def open_callback(self):

			if v == 'aircrack-ng':
				rc_o = open_.test('aircrack-ng')
			elif v == 'bluelog':
				rc_o = open_.test('bluelog')
			elif v == 'btscanner':
				rc_o = open_.test('btscanner')
			elif v == 'bluez':
				rc_o = open_.test('bluez')
			elif v == 'tshark':
				rc_o = open_.test('tshark')
			elif v == 'wireshark':
				rc_o = open_.test('wireshark')

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def uninstall_callback(self):
			rc_u = uninstall.test(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.remove_widget(o)
				widget.remove_widget(up)
				widget.remove_widget(un)
				widget.add_widget(i)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.test(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.add_widget(o)
				widget.add_widget(up)
				widget.add_widget(un)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'


		if v in installed_tools:
			o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
			o.bind(on_press=open_callback)
			up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
			un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
			un.bind(on_press=uninstall_callback)

			widget.add_widget(o)
			widget.add_widget(up)
			widget.add_widget(un)
		else:
			i = Button(text='Install', size_hint= (.20, .075), pos_hint= {'x':.4, 'y':.075})
			widget.add_widget(i)
			i.bind(on_press=install_callback)

	pass

class SDRPage(Screen):

	def sdr(widget, value):

		if v == 'gnuradio':
			with open("gnuradio.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("gnuradio_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'gqrx':
			with open("gqrx.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("gqrx_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		def open_callback(self):	#this functionality will be a little different

			if v == 'gnuradio':
				rc_o = open_.test('gnuradio')
			elif v == 'gqrx':
				rc_o = open_.test('gqrx')

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def uninstall_callback(self):
			rc_u = uninstall.test(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.remove_widget(o)
				widget.remove_widget(up)
				widget.remove_widget(un)
				widget.add_widget(i)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.test(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.add_widget(o)
				widget.add_widget(up)
				widget.add_widget(un)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		if v in installed_tools:
			o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
			o.bind(on_press=open_callback)
			up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
			un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
			un.bind(on_press=uninstall_callback)

			widget.add_widget(o)
			widget.add_widget(up)
			widget.add_widget(un)
		else:
			i = Button(text='Install', size_hint= (.20, .075), pos_hint= {'x':.4, 'y':.075})
			widget.add_widget(i)
			i.bind(on_press=install_callback)

	pass

class MiscellaneousPage(Screen):

	def mis(widget,value):

		if v == 'katoolin':
			with open("katoolin.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("katoolin.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'tio':
			with open("tio.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("tio_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		def open_callback(self):	#this functionality will be a little different

			if v == 'katoolin':
				rc_o = open_.test('katoolin')
			elif v == 'tio':
				rc_o = open_.test('tio')

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def uninstall_callback(self):
			rc_u = uninstall.test(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.remove_widget(o)
				widget.remove_widget(up)
				widget.remove_widget(un)
				widget.add_widget(i)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.test(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.add_widget(o)
				widget.add_widget(up)
				widget.add_widget(un)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		if v in installed_tools:
			o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
			o.bind(on_press=open_callback)
			up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
			un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
			un.bind(on_press=uninstall_callback)

			widget.add_widget(o)
			widget.add_widget(up)
			widget.add_widget(un)
		else:
			i = Button(text='Install', size_hint= (.20, .075), pos_hint= {'x':.4, 'y':.075})
			widget.add_widget(i)
			i.bind(on_press=install_callback)

	pass

class SeeAllPage(Screen, Widget):

	def to_install(widget, name, value):

		if value == 'down':
			maybe.append(name)
		else:
			maybe.remove(name)

	def install_all(widget):

		for i in maybe:
			print (i)

		

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

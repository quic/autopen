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

import install_basics
import install
import open_
import uninstall
import update
#from text import *

Builder.load_string("""

<WelcomePage>:
	id: welcome 
	FloatLayout:
		id: welcome_float
		canvas.before:
			Rectangle:
				source: 'images/background_side.jpg'
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
			text: 'go to class name page'
			size_hint: .25, .1
			pos_hint: {'x':.55, 'y':.5}
			on_press:
				root.manager.transition.direction = 'left'
				root.manager.transition.duration = .5
				root.manager.current = 'shortened_classname'	

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

<HowTo>:
	id: howto
	FloatLayout:
		id: howto_float
		canvas.before:
			Rectangle:
				source: 'images/background_side.jpg'
				pos: self.pos
				size: self.size
		Label:
			pos_hint:{'center_x': 0.5, 'top': 0.96}
			size_hint: (0.5,0.05)
			text: "[b][color=3388dd]How To[/color][/b]"
			font_size: 32
			markup: True
		ScrollableLabel:
			pos_hint:{'center_x': 0.5, 'top': 0.9}
			size_hint:(0.8,0.8)
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: root.alter_text()
				font_size: 18
				markup: True
				valign:'middle'
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0} 
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "welcome"

<Terms>:
	id: terms
	FloatLayout:
		id: terms_float
		canvas.before:
			Rectangle:
				source: 'images/background_side.jpg'
				pos: self.pos
				size: self.size
		Label:
			pos_hint:{'center_x': 0.5, 'top': 0.96}
			size_hint: (0.5,0.05)
			text: "[b][color=3388dd]Terms and Conditions[/color][/b]"
			font_size: 32
			markup: True
		ScrollableLabel:
			pos_hint:{'center_x': 0.5, 'top': 0.9}
			size_hint:(0.8,0.8)
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: root.alter_text()
				font_size: 18
				markup: True
				valign:'middle'
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0}
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "welcome"

<About>:
	id: about
	FloatLayout:
		id: about_float
		canvas.before:
			Rectangle:
				source: 'images/background_side.jpg'
				pos: self.pos
				size: self.size
		Label:
			pos_hint:{'center_x': 0.5, 'top': 0.96}
			size_hint: (0.5,0.05)
			text: "[b][color=3388dd]About AutoPen[/color][/b]"
			font_size: 32
			markup: True
		ScrollableLabel:
			pos_hint:{'center_x': 0.5, 'top': 0.9}
			size_hint:(0.8,0.8)
			Label:
				id: label1
				size_hint_y: None
				height: label1.texture_size[1]
				text_size: label1.width, None
				text: root.alter_text()
				font_size: 18
				markup: True
				valign:'middle'
		Button:
			text: 'Back'
			size_hint: .1, .05
			pos_hint: {'x':0, 'y': 0}
			on_press:
				root.manager.transition.direction = "right"
				root.manager.transition.duration = .5
				root.manager.current = "welcome"

<ToolsPage>:
	id: tools_main
	FloatLayout:
		id: main_float
		canvas.before:
			Rectangle:
				source: 'images/background_front.jpg'
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
			source: "images/AutoPenBlack.png"
			size_hint: 0.1,0.1
			pos_hint: {'x':0, 'y':0.88}

<CanPage>:
	id: can_main
	FloatLayout:
		id: can_float
		canvas.before:
			Rectangle:
				source: 'images/background_off_side.jpg'
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
			size_hint:(0.3,0.6)
			Label:
				id: label2
				size_hint_y: None
				height: label2.texture_size[1]
				text_size: label2.width, None
				text: ''
				font_size: 14
				markup: True
				valign:'middle'
	FloatLayout:
		id: dynbutton

<BluetoothWifiPage>:
	id: bt_main
	FloatLayout:
		id: bt_float
		canvas.before:
			Rectangle:
				source: 'images/background_off_side.jpg'
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
				id: aircrack-ng
				text: 'aircrack-ng'
				size_hint: .25, .1
				on_press: root.bw('aircrack-ng')
			Button:
				id: bluelog
				text: 'Bluelog'
				size_hint: .25, .1
				on_press: root.bw('bluelog')
			Button:
				id: bluemaho
				text: 'Bluemaho'
				size_hint: .25, .1
				on_press: root.bw('bluemaho')
			Button:
				id: btscanner
				text: 'BTscanner'
				size_hint: .25, .1
				on_press: root.bw('btscanner')
			Button:
				id: tshark
				text: 'tshark'
				size_hint: .25, .1
				on_press: root.bw('tshark')
			Button:
				id: wireshark
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
			size_hint:(0.3,0.6)
			Label:
				id: label2
				size_hint_y: None
				height: label2.texture_size[1]
				text_size: label2.width, None
				text: ''
				font_size: 14
				markup: True
				valign:'middle'
	FloatLayout:
		id: dynbutton

<SDRPage>:
	id: sdr_main
	FloatLayout:
		id: sdr_float
		canvas.before:
			Rectangle:
				source: 'images/background_off_side.jpg'
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
				id: gnuradio
				text: 'GNU Radio'
				size_hint: .25, .1
				on_press: root.sdr('gnuradio')
			Button:
				id: gqrx
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
			size_hint:(0.3,0.6)
			Label:
				id: label2
				size_hint_y: None
				height: label2.texture_size[1]
				text_size: label2.width, None
				text: ''
				font_size: 14
				markup: True
				valign:'middle'
	FloatLayout:
		id: dynbutton

<MiscellaneousPage>
	id: mis
	FloatLayout:
		id: mis_float
		canvas.before:
			Rectangle:
				source: 'images/background_off_side.jpg'
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
				id: katoolin
				text: 'Katoolin'
				size_hint: .25, .1
				on_press: root.mis('katoolin')
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
			size_hint:(0.3,0.6)
			Label:
				id: label2
				size_hint_y: None
				height: label2.texture_size[1]
				text_size: label2.width, None
				text: ''
				font_size: 14
				markup: True
				valign:'middle'
	FloatLayout:
		id: dynbutton

<SeeAllPage>:
	id: seeall
	FloatLayout:
		id: seeall_float
		canvas.before:
			Rectangle:
				source: 'images/background_off_side.jpg'
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
				id: o2oo
				text: 'O2OO'
				size_hint: .30, .1
				on_press: root.to_install('o2oo')
			ToggleButton:
				id: aircrack-ng
				text: 'aircrack-ng'
				size_hint: .30, .1
				on_press: root.to_install('aircrack-ng')
			ToggleButton:
				id: bluelog
				text: 'Bluelog'
				size_hint: .30, .1
				on_press: root.to_install('bluelog')
			ToggleButton:
				id: bluemaho
				text: 'Bluemaho'
				size_hint: .30, .1
				on_press: root.to_install('bluemaho')
			ToggleButton:
				id: btscanner
				text: 'BTscanner'
				size_hint: .30, .1
				on_press: root.to_install('btscanner')
			ToggleButton:
				id: c0f
				text: 'c0f'
				size_hint: .30, .1
				on_press: root.to_install('c0f')
			ToggleButton:
				id: canbadger-hw
				text: 'CANBadger-HW'
				size_hint: .30, .1
				on_press: root.to_install('canbadger-hw')
			ToggleButton:
				id: canbadger-sw
				text: 'CANBadger-SW'
				size_hint: .30, .1
				on_press: root.to_install('canbadger-sw')
			ToggleButton:
				id: canbus-utils
				text: 'CANbus-utils'
				size_hint: .30, .1
				on_press: root.to_install('canbus-utils')
			ToggleButton:
				id: can-utils
				text: 'CAN-utils'
				size_hint: .30, .1
				on_press: root.to_install('can-utils')
			ToggleButton:
				id: j1939
				text: 'CAN-utils-j1939'
				size_hint: .30, .1
				on_press: root.to_install('j1939')
			ToggleButton:
				id: can-utils-x
				text: 'CAN-utils-X'
				size_hint: .30, .1
				on_press: root.to_install('can-utils-x')
			ToggleButton:
				id: caringcaribou
				text: 'Caring Caribou'
				size_hint: .30, .1
				on_press: root.to_install('caringcaribou')
			ToggleButton:
				id: tio
				text: 'Tio'
				size_hint: .30, .1
				on_press: root.to_install('tio')
			ToggleButton:
				id: gnu-radio
				text: 'GNU Radio'
				size_hint: .30, .1
				on_press: root.to_install('gnu-radio')
			ToggleButton:
				id: gqrx
				text: 'gqrx'
				size_hint: .30, .1
				on_press: root.to_install('gqrx')
			ToggleButton:
				id: katoolin
				text: 'Katoolin'
				size_hint: .30, .1
				on_press: root.to_install('katoolin')
			ToggleButton:
				id: kayak
				text: 'Kayak'
				size_hint: .30, .1
				state: 'normal'
				on_press: root.to_install('kayak')
			ToggleButton:
				id: pyobd
				text: 'PyOBD'
				size_hint: .30, .1
				state: 'normal'
				on_press: root.to_install('pyobd')
			ToggleButton:
				id: tshark
				text: 'tshark'
				size_hint: .30, .1
				state: 'normal'
				on_press: root.to_install('tshark')
			ToggleButton:
				id: udsim
				text: 'UDSim'
				size_hint: .30, .1
				state: 'normal'
				on_press: root.to_install('udsim')
			ToggleButton:
				id: wireshark
				text: 'Wireshark'
				size_hint: .30, .1
				state: 'normal'
				on_press: root.to_install('wireshark')
		Button:
			text: 'Install'
			size_hint: .3, .07
			pos_hint: {'x':.35, 'y': .05}
			on_press: root.install_selected()
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


<ClassName>
	id: shortened_classname
	someLayout:
		etc. 

""")

installed_tools = []

try:
	already_installed = open('installed.txt', 'r')
	for i in already_installed.readlines():
		installed_tools.append(i.strip('\n'))
except FileNotFoundError:
	
	pass

can = ['o2oo', 'c0f', 'canbadger-hw', 'canbadger-sw', 'canbus-utils', 'can-utils', 'can-utils-j1939', 'can-utils-x', 'caringcaribou', 'pyobd', 'kayak', 'udsim']
b_w = ['aircrack-ng', 'bluelog', 'bluemaho', 'btscanner', 'tshark', 'wireshark']
sdr = ['gnu radio', 'gqrx']
mis = ['katoolin']
all_tools = can + b_w + sdr + mis

tools_to_install = []
broken = []

class ScrollableLabel(ScrollView):
	text = StringProperty('')

class WelcomePage(Screen):
	pass

class HowTo(Screen):
	def alter_text(self):
		with open("info/howto.txt", "r") as stream:
			labeltext1 = stream.read()
		return labeltext1
	pass

class About(Screen):
	def alter_text(self):
		with open("info/about.txt", "r") as stream:
			labeltext1 = stream.read()
		return labeltext1
	pass

class Terms(Screen):
	def alter_text(self):
		with open("info/TandC.txt", "r") as stream:
			labeltext1 = stream.read()
		return labeltext1
	pass

class ToolsPage(Screen):

	def find(self):	#doing this atm, but will fix functionality later
		t = (self.ids['search'].text).lower()

		if t in can:
			screen_manager.current = 'can'
			screen_manager.current_screen.can(t)
		elif t in b_w:
			screen_manager.current = 'bw'
			screen_manager.current_screen.bw(t)
		elif t in sdr:
			screen_manager.current = 'sdr'
			screen_manager.current_screen.sdr(t)
		elif t in mis:
			screen_manager.current = 'miscellaneous'
			screen_manager.current_screen.mis(t)
	
		#make it pop up suggestions?		
	pass

class CanPage(Screen):

	def can(widget, value):

		v = value

		for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
			if i in can:
				widget.ids[i].background_color = [1,1,1,.65]


		if v == 'can-utils-x':
			with open("text/canutilsx.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/canutilsx_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'canbadger':
			with open("text/canbadger.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/canbadger_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'kayak':
			with open("text/kayak.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/kayak_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'udsim':
			with open("text/udsim.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/udsim_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'pyobd':
			with open("text/pyobd.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/pyobd_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'o2oo':
			with open("text/o2oo.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/o2oo_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'c0f':
			with open("text/c0f.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/c0f_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'can-utils':
			with open("text/canutils.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/canutils_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'canbus-utils':
			with open("text/canbus_utils.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/canbus_utils_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'caringcaribou':
			with open("text/caringcaribou.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/caringcaribou_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'j1939':
			with open("text/j1939.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/j1939_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2



		#opens the tool on enter with the appropriate arguments
		def open_callback(self):
			rc_o = open_.open_(v)

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def update_callback(self):
			layout = FloatLayout()
			rc_up = update.update(v)

			if rc_up != 0:
				popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center'), size_hint=(None,None), size=(300,200))
			else:
				popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)))

			popup.open()

		def uninstall_callback(self):
			rc_u = uninstall.uninstall(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.ids.dynbutton.remove_widget(o)
				widget.ids.dynbutton.remove_widget(up)
				widget.ids.dynbutton.remove_widget(un)
				widget.ids.dynbutton.add_widget(i)
				installed_tools.remove(v)
				i.bind(on_press=install_callback)

		#fixes the problem for when buttons were being recreated and never removed when clicked
		# for child in widget.children:
		# 	if isinstance(child,Button):
		# 		widget.ids.dynbutton.remove_widget(child)
		# widget.ids.dynbutton.clear_widgets()
		
		#this if the function that executes when install in pressed


		o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])  # this should be green
		up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
		un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},	background_color=[0, 0, 1, .75])
		i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
		
		def install_callback(self): 
			rc_i = install.install(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.ids.dynbutton.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				up.bind(on_press=update_callback)
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.ids.dynbutton.add_widget(o)
				widget.ids.dynbutton.add_widget(up)
				widget.ids.dynbutton.add_widget(un)
				installed_tools.append(v)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'


		widget.ids.dynbutton.clear_widgets()

		#tryme = Button(pos_hint={'x': 0.65, 'top': 0.3}, size_hint=(0.3,0.1), text= 'Try Me!')

		if v in installed_tools:
			widget.ids[v].background_color = [1,1,1,.65]
			o.bind(on_press=open_callback)
			un.bind(on_press=uninstall_callback)
			up.bind(on_press=update_callback)

			widget.ids.dynbutton.add_widget(o)
			widget.ids.dynbutton.add_widget(up)
			widget.ids.dynbutton.add_widget(un)
			#widget.ids.dynbutton.add_widget(tryme)
		else:
			widget.ids.dynbutton.add_widget(i)
			i.bind(on_press=install_callback)
			#widget.ids.scroll2.remove_widget(widget.ids.label2)

	pass


class BluetoothWifiPage(Screen):

	def bw(widget, value):	#for buttons that do not use a popup

		v = value

		for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
			if i in b_w:
				widget.ids[i].background_color = [1,1,1,.65]

		if v == 'aircrack-ng':
			with open("text/aircrack_ng.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/aircrack_ng_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'bluelog':
			with open("text/bluelog.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/bluelog_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'bluemaho':
			with open("text/bluemaho.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/bluemaho.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'btscanner':
			with open("text/btscanner.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/btscanner_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'package':
			with open("text/package.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/package_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'tshark':
			with open("text/tshark.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/tshark_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'wireshark':
			with open("text/wireshark.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/wireshark_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		#opens the tool on enter with the appropriate arguments
		def open_callback(self):

			rc_o = open_.open_(v)

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def update_callback(self):
			layout = FloatLayout()
			rc_up = update.update(v)

			if rc_up != 0:
				popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center'), size_hint=(None,None), size=(300,200))
			else:
				popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)))

			popup.open()

		def uninstall_callback(self):
			rc_u = uninstall.uninstall(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.ids.dynbutton.remove_widget(o)
				widget.ids.dynbutton.remove_widget(up)
				widget.ids.dynbutton.remove_widget(un)
				widget.ids.dynbutton.add_widget(i)
				installed_tools.remove(v)
				i.bind(on_press=install_callback)

		# for child in widget.children:
		# 	if isinstance(child,Button):
		# 		widget.ids.dynbutton.remove_widget(child)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.install(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.ids.dynbutton.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				up.bind(on_press=update_callback)
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.ids.dynbutton.add_widget(o)
				widget.ids.dynbutton.add_widget(up)
				widget.ids.dynbutton.add_widget(un)
				installed_tools.append(v)

			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		widget.ids.dynbutton.clear_widgets()

		o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])  # this should be green
		up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
		un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},	background_color=[0, 0, 1, .75])
		i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
		#tryme = Button(pos_hint={'x': 0.65, 'top': 0.3}, size_hint=(0.3,0.1), text= 'Try Me!')
		if v in installed_tools:
			widget.ids[v].background_color = [1,1,1,.65]
			o.bind(on_press=open_callback)
			un.bind(on_press=uninstall_callback)
			up.bind(on_press=update_callback)

			widget.ids.dynbutton.add_widget(o)
			widget.ids.dynbutton.add_widget(up)
			widget.ids.dynbutton.add_widget(un)
			#widget.ids.dynbutton.add_widget(tryme)
		else:
			widget.ids.dynbutton.add_widget(i)
			i.bind(on_press=install_callback)
			#widget.ids.scroll2.remove_widget(widget.ids.label2)
	pass

class SDRPage(Screen):

	def sdr(widget, value):

		v = value

		for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
			if i in sdr:
				widget.ids[i].background_color = [1,1,1,.65]

		if v == 'gnuradio':
			with open("text/gnuradio.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/gnuradio_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		elif v == 'gqrx':
			with open("text/gqrx.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/gqrx_example.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		def open_callback(self):	#this functionality will be a little different

			rc_o = open_.open_(v)

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def update_callback(self):
			layout = FloatLayout()
			rc_up = update.update(v)

			if rc_up != 0:
				popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center'), size_hint=(None,None), size=(300,200))
			else:
				popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)))

			popup.open()

		def uninstall_callback(self):
			rc_u = uninstall.uninstall(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.ids.dynbutton.clear_widgets()
				widget.ids.dynbutton.add_widget(i)
				i.bind(on_press=install_callback)
				installed_tools.remove(v)
				i.bind(on_press=install_callback)

		# for child in widget.children:
		# 	if isinstance(child,Button):
		# 		widget.ids.dynbutton.remove_widget(child)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.install(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.ids.dynbutton.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				up.bind(on_press=update_callback)
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.ids.dynbutton.add_widget(o)
				widget.ids.dynbutton.add_widget(up)
				widget.ids.dynbutton.add_widget(un)
				installed_tools.append(v)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		widget.ids.dynbutton.clear_widgets()

		o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])  # this should be green
		up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
		un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},	background_color=[0, 0, 1, .75])
		i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
		#tryme = Button(pos_hint={'x': 0.65, 'top': 0.3}, size_hint=(0.3,0.1), text= 'Try Me!')
		if v in installed_tools:
			widget.ids[v].background_color = [1,1,1,.65]
			o.bind(on_press=open_callback)
			un.bind(on_press=uninstall_callback)
			up.bind(on_press=update_callback)

			widget.ids.dynbutton.add_widget(o)
			widget.ids.dynbutton.add_widget(up)
			widget.ids.dynbutton.add_widget(un)
			#widget.ids.dynbutton.add_widget(tryme)
		else:
			widget.ids.dynbutton.add_widget(i)
			i.bind(on_press=install_callback)
			#widget.ids.scroll2.remove_widget(widget.ids.label2)

	pass

class MiscellaneousPage(Screen):

	def mis(widget,value):

		v = value

		for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
			if i in mis:
				widget.ids[i].background_color = [1,1,1,.65]

		if v == 'katoolin':
			with open("text/katoolin.txt", "r") as stream:
				labeltext1 = stream.read()
			widget.ids["label1"].text = labeltext1
			with open("text/katoolin.txt", "r") as stream:
				labeltext2 = stream.read()
			widget.ids["label2"].text = labeltext2

		def open_callback(self):	#this functionality will be a little different

			rc_o = open_.open_(v)

			if rc_o != 0:
				o.background_color = [1,0,0,.65]
				o.text = 'Failed to install'

		def update_callback(self):
			layout = FloatLayout()
			rc_up = update.update(v)

			if rc_up != 0:
				popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center'), size_hint=(None,None), size=(300,200))
			else:
				popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)))

			popup.open()

		def uninstall_callback(self):
			rc_u = uninstall.uninstall(v)

			if rc_u != 0:
				un.background_color = [1,0,0,.65]
				un.text = 'Failed to uninstall'
			else:
				un.background_color = [0,1,0,.65]
				widget.ids.dynbutton.remove_widget(o)
				widget.ids.dynbutton.remove_widget(up)
				widget.ids.dynbutton.remove_widget(un)
				widget.ids.dynbutton.add_widget(i)
				installed_tools.remove(v)
				i.bind(on_press=install_callback)

		# for child in widget.children:
		# 	if isinstance(child,Button):
		# 		widget.ids.dynbutton.remove_widget(child)

		#this if the function that executes when install in pressed
		def install_callback(self): 

			rc_i = install.install(v)

			#this needs to be wrapped around an exception incase for some reason the correct name isn't passed
			if rc_i == 0:
				widget.ids.dynbutton.remove_widget(i)
				o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])#this should be green
				o.bind(on_press=open_callback)
				up = Button(text= 'Update', size_hint= (.15,.07), pos_hint= {'x':.45, 'y':.075}, background_color=[0,0,1,.65])
				up.bind(on_press=update_callback)
				un = Button(text= 'Uninstall', size_hint= (.15, .07), pos_hint= {'x':.60, 'y':.075}, background_color=[0,0,1,.75])
				un.bind(on_press=uninstall_callback)

				widget.ids.dynbutton.add_widget(o)
				widget.ids.dynbutton.add_widget(up)
				widget.ids.dynbutton.add_widget(un)
				installed_tools.append(v)
			elif rc_i != 0:
				i.background_color = [1,0,0,.65]
				i.text = 'Failed to Install'

		widget.ids.dynbutton.clear_widgets()

		o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])  # this should be green
		up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
		un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},	background_color=[0, 0, 1, .75])
		i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
		#tryme = Button(pos_hint={'x': 0.65, 'top': 0.3}, size_hint=(0.3,0.1), text= 'Try Me!')
		if v in installed_tools:
			widget.ids[v].background_color = [1,1,1,.65]
			o.bind(on_press=open_callback)
			un.bind(on_press=uninstall_callback)
			up.bind(on_press=update_callback)

			widget.ids.dynbutton.add_widget(o)
			widget.ids.dynbutton.add_widget(up)
			widget.ids.dynbutton.add_widget(un)
			#widget.ids.dynbutton.add_widget(tryme)
		else:
			widget.ids.dynbutton.add_widget(i)
			i.bind(on_press=install_callback)
			#widget.ids.scroll2.remove_widget(widget.ids.label2)
	pass

class SeeAllPage(Screen):
#mention that they need to navigate to the page in order to open the tool

	# for i in installed_tools:	#if we cant get this to work , add a "see what tools are installed" button
	# 	if i in all_tools:
	# 		widget.ids[i].background_color = [1,1,1,.65]

	def to_install(widget, name):
		print (widget.ids[name].state)

		if widget.ids[name].state == 'down' and name not in tools_to_install:
			widget.ids[name].state = 'normal'
			print (widget.ids[name].state)
			tools_to_install.append(name)
		else:
			widget.ids[name].state = 'down'
			try:
				tools_to_install.remove(name)
			except:
				pass

	def install_selected(widget):

		print (tools_to_install)
		for i in tools_to_install:
			print (i)
			rc_i = install.test(i)
			if rc_i != 0:
				broken.append(i)
			if rc_i == 0:
				installed_tools.append(i)

	def install_all(widget):
		for i in all_tools:
			#just for this tool, need to change the name to be consistent with the backend. In the list it is can-utils-j1939 because it is used for the search functionality
			if i is 'can-utils-j1939':
				i = 'j1939'
			rc_i = install.test(i)
			if rc_i != 0:
				broken.append(i)
			if rc_i == 0:
				installed_tools.append(i)
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





class AutoPenApp(App):

	def build(self):

		title = 'AutoPen'

		return screen_manager

if __name__ == "__main__":
	AutoPenApp().run()
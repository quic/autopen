import sys
sys.argv[1:] = []
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
import update
#from text import *

try:
    builder_fh = open('gui_builder_text.txt', 'r')
except IOError as io_error:
    print 'Could not open file', builder_fh.name
    print io_error
    exit(1)
Builder.load_string(builder_fh.read())

installed_tools = []

try:
    already_installed_fh = open('installed.txt', 'r')
    for i in already_installed_fh.readlines():
        installed_tools.append(i.strip('\n'))
except IOError as io_error:
    print 'Could not open file', already_installed_fh.name
    print io_error

can = ('o2oo', 'c0f', 'canbadger-hw', 'canbadger-sw', 'canbus-utils', 'can-utils', 'can-utils-j1939', 'can-utils-x', 'caringcaribou', 'pyobd', 'kayak', 'udsim')
b_w = ('aircrack-ng', 'bluelog', 'bluemaho', 'btscanner', 'tshark', 'wireshark')
sdr = ('gnu radio', 'gqrx')
mis = ('katoolin')
all_tools = can + (b_w,) + (sdr,) + (mis,)

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

    def find(self):    #doing this atm, but will fix functionality later
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

        for i in installed_tools:    #if we cant get this to work , add a "see what tools are installed" button
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
                popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))
            else:
                popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))

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
        #     if isinstance(child,Button):
        #         widget.ids.dynbutton.remove_widget(child)
        # widget.ids.dynbutton.clear_widgets()

        #this if the function that executes when install in pressed


        o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])  # this should be green
        up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
        un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},    background_color=[0, 0, 1, .75])
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

    def bw(widget, value):    #for buttons that do not use a popup

        v = value

        for i in installed_tools:    #if we cant get this to work , add a "see what tools are installed" button
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
                popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))
            else:
                popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))

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
        #     if isinstance(child,Button):
        #         widget.ids.dynbutton.remove_widget(child)

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
        un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},    background_color=[0, 0, 1, .75])
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

        for i in installed_tools:    #if we cant get this to work , add a "see what tools are installed" button
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

        def open_callback(self):    #this functionality will be a little different

            rc_o = open_.open_(v)

            if rc_o != 0:
                o.background_color = [1,0,0,.65]
                o.text = 'Failed to install'

        def update_callback(self):
            layout = FloatLayout()
            rc_up = update.update(v)

            if rc_up != 0:
                popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))
            else:
                popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))

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
        #     if isinstance(child,Button):
        #         widget.ids.dynbutton.remove_widget(child)

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
        un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},    background_color=[0, 0, 1, .75])
        i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
        if v in installed_tools:
            widget.ids[v].background_color = [1,1,1,.65]
            o.bind(on_press=open_callback)
            un.bind(on_press=uninstall_callback)
            up.bind(on_press=update_callback)

            widget.ids.dynbutton.add_widget(o)
            widget.ids.dynbutton.add_widget(up)
            widget.ids.dynbutton.add_widget(un)
        else:
            widget.ids.dynbutton.add_widget(i)
            i.bind(on_press=install_callback)
    pass

class MiscellaneousPage(Screen):
    def mis(widget,value):
        v = value
        for i in installed_tools:
            if i in mis:
                widget.ids[i].background_color = [1,1,1,.65]

        if v == 'katoolin':
            with open("text/katoolin.txt", "r") as stream:
                labeltext1 = stream.read()
            widget.ids["label1"].text = labeltext1
            with open("text/katoolin.txt", "r") as stream:
                labeltext2 = stream.read()
            widget.ids["label2"].text = labeltext2

        def open_callback(self):
            rc_o = open_.open_(v)
            if rc_o != 0:
                o.background_color = [1,0,0,.65]
                o.text = 'Failed to install'

        def update_callback(self):
            layout = FloatLayout()
            rc_up = update.update(v)
            if rc_up != 0:
                popup = Popup(title=v, content=Label(text='Failed to update. Please refer to log.txt for additional information on error!', text_size=(280,None), halign='center', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))
            else:
                popup = Popup(title=v, content=Label(text='Successfully updated!', size_hint=(None,None), size=(300,200)), size_hint=(0.4,0.5))

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

        #this if the function that executes when install in pressed
        def install_callback(self):
            rc_i = install.install(v)
            #this needs to be wrapped around an exception incase for some reason the correct name isn't passed
            if rc_i == 0:
                widget.ids.dynbutton.remove_widget(i)
                o = Button(text='Open', size_hint= (.15, .07), pos_hint= {'x':.3, 'y':.075}, background_color=[0,1,0,.65])
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

        o = Button(id='o', text='Open', size_hint=(.15, .07), pos_hint={'x': .3, 'y': .075}, background_color=[0, 1, 0, .65])
        up = Button(id='up', text='Update', size_hint=(.15, .07), pos_hint={'x': .45, 'y': .075}, background_color=[0, 0, 1, .65])
        un = Button(id='un', text='Uninstall', size_hint=(.15, .07), pos_hint={'x': .60, 'y': .075},    background_color=[0, 0, 1, .75])
        i = Button(id='i', text='Install', size_hint=(.20, .075), pos_hint={'x': .4, 'y': .075})
        if v in installed_tools:
            widget.ids[v].background_color = [1,1,1,.65]
            o.bind(on_press=open_callback)
            un.bind(on_press=uninstall_callback)
            up.bind(on_press=update_callback)

            widget.ids.dynbutton.add_widget(o)
            widget.ids.dynbutton.add_widget(up)
            widget.ids.dynbutton.add_widget(un)
        else:
            widget.ids.dynbutton.add_widget(i)
            i.bind(on_press=install_callback)
    pass

class SeeAllPage(Screen):

    def to_install(widget, name):
        print widget.ids[name].stat

        if widget.ids[name].state == 'down' and name not in tools_to_install:
            widget.ids[name].state = 'normal'
            print widget.ids[name].state
            tools_to_install.append(name)
        else:
            widget.ids[name].state = 'down'
            try:
                tools_to_install.remove(name)
            except:
                pass

    def install_selected(widget):

        print tools_to_install
        for i in tools_to_install:
            print i
            rc_i = install.install(i)
            if rc_i != 0:
                broken.append(i)
            if rc_i == 0:
                installed_tools.append(i)

    def install_all(widget):
        for i in all_tools:
            #just for this tool, need to change the name to be consistent with the backend. In the list it is can-utils-j1939 because it is used for the search functionality
            if i is 'can-utils-j1939':
                i = 'j1939'

            rc_i = install.install(i)
            if rc_i != 0:
                broken.append(i)
            if rc_i == 0:
                installed_tools.append(i)
    pass

class AutoPenApp(App):
    def build(self):
        title = 'AutoPen'
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
        return screen_manager


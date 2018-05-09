import sys
sys.argv[1:] = []
import kivy
kivy.require('1.9.0')
from kivy.uix.dropdown import DropDown
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
from kivy.properties import ObjectProperty, StringProperty
from kivy.base import runTouchApp
#import install_basics
import install
import open_
import uninstall
import update
#from text import *
#SQL interactions
import MySQLdb 

try:
    builder_fh = open('gui_builder_text.txt', 'r')
except IOError as io_error:
    print 'Could not open file', builder_fh.name
    print io_error
    exit(1)
Builder.load_string(builder_fh.read())

installed_tools = []
installed_tools.append('m2')
installed_tools.append('freq')
installed_tools.append('savvy')
installed_tools.append('combine')
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
chosen = ''
cars = []
connection = 1
def set_chosen(input):
	global chosen
	chosen = input

def get_chosen():
	return chosen

try:
    db = MySQLdb.connect(host="autopen.c5eqmploekdx.us-east-2.rds.amazonaws.com", user="SHIFT", passwd="%&12SHilaE7", db="autopen", port=3306)
except MySQLdb.Error as mysql_error:
    print 'Cannot connect to database'
    print mysql_error
    connection = 0
else:
    cursor = db.cursor();
    cursor.execute("SELECT * FROM Cars");
    numrows = cursor.rowcount
    cars = cursor.fetchall()
    cursor.execute("SELECT * FROM Exploits");
    exploits = cursor.fetchall()
    db.close()
    x = .1
    y = .9
    for row in cars:
	#x = x + z
	myString = "<CarsPage>:\n\tButton:\n\t\tid:"+str(row[1])+"\n\t\ttext: '" + str(row[1]) + "'\n\t\tsize_hint: .25, .1\n\t\tpos_hint: {'x':" + str(x) + ", 'y':" + str(y)+"}"
	parttwo = "\n\t\ton_press:\n\t\t\troot.manager.transition.direction='left'\n"
	partthree= "\t\t\troot.manager.transition.duration=.5\n\t\t\troot.manager.current='carinfo'"
	y -= .1
        partfour = "\n\t\ton_press:\n\t\t\troot.manager.get_screen('carinfo').work('"+ str(row[1])+"')"
	#parttwo = "\n\t\ton_press:\n\t\t\troot.cars("+str(row[0])+")"
	Builder.load_string(myString+parttwo+partthree+partfour)
	myString = ''
class CustomDropDown(DropDown):
    pass

class CarInfoPage(Screen):
        label_wid = ObjectProperty()
        exploitbox_wid = ObjectProperty()
        def work(self,stuff):
		if connection == 0:
			print "Cannot connect to Database"
			return
                self.label_wid.text = stuff
                for i in cars:
                        if i[1] == stuff:
                                for t in exploits:
                                        if t[1] == i[0]:
                                                finalmessage = self.exploitbox_wid.text+"\n\n"+"Date Found: "+str(t[2])+"\n"+"Car Year: " + str(t[4])+"\n"+t[3]
                                                self.exploitbox_wid.text = finalmessage		
	pass
	
class ScrollableLabel(ScrollView):
    text = StringProperty('')

class WelcomePage(Screen):
    pass

class DataEntryPage(Screen):
    mandate_wid = ObjectProperty()
    carmodel_wid = ObjectProperty()
    exploit_wid = ObjectProperty()
    exploitdate_wid = ObjectProperty()
    def do_action(self):
        if connection == 0:
		print 'No database connection'
		return
	model = self.carmodel_wid.text
	year = self.mandate_wid.text
	print (self.exploitdate_wid.text)
	print (self.exploit_wid.text)
        db = MySQLdb.connect(host="autopen.c5eqmploekdx.us-east-2.rds.amazonaws.com", user="SHIFT", passwd="%&12SHilaE7", db="autopen", port=3306)
        cursor = db.cursor()
        check = 0
        for car in cars:
                if car[1] == model:
                        check = 1
        if check == 0:
	    valueSend = "INSERT INTO Cars (Model) VALUES ('"+model+"');"
            cursor.execute(valueSend);
        newcursor = db.cursor()
        getId = "SELECT idCars FROM Cars WHERE Model = '" + model +"';"
        newcursor.execute(getId)
	idnum = newcursor.fetchall()
        lastCursor = db.cursor()
        insertEx = "INSERT INTO Exploits (idCars, ExDate, Exploit,CarYear) VALUES ('"+str(idnum[0][0])+"','"+self.exploitdate_wid.text+"','"+self.exploit_wid.text+"','"+year+"');"
        lastCursor.execute(insertEx)
        #print("sent this: " + valueSend)
        db.commit()
        cursor.close()
	newcursor.close()
        lastCursor.close()
        db.close()
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

class CarsPage(Screen):
       # def __init__(self, *args, **kwargs):
        #def starter(self):
        #        bxlayout = BoxLayout(orientation='vertical')
         #       fieldslayout = GridLayout(cols=2, rows=3, row_force_default=True, row_default_height=40)
           #     lbl_uname = Label(text="User name", size_hint=(.5, .25), halign='right')
           #     txt_uname = TextInput(text='', multiline=False)
           #     lbl_pwd = Label(text="Password", size_hint=(.5, .25))
            #    txt_pwd = TextInput(text='', multiline=False, password=True)
            #    lbl_dept = Label(text="Department")
            #    dropdown_dept = DropDown()
            #    for x in ("Bar", "Kitchen", "Housekeeping", "Hotel", "Maintenance"):
            #            dd_btn = Button(text=x)
            #            print x
             #           dropdown_dept.add_widget(dd_btn)
            

             #   bxlayout.add_widget(fieldslayout)
             #   fieldslayout.add_widget(lbl_uname)
             #   fieldslayout.add_widget(txt_uname)
            #    fieldslayout.add_widget(lbl_pwd)
            #    fieldslayout.add_widget(txt_pwd)
            #    fieldslayout.add_widget(lbl_dept)
             #   fieldslayout.add_widget(dropdown_dept)

            #    btnlayout = GridLayout(cols=3, padding=50, spacing = 50)
             #   bxlayout.add_widget(btnlayout)
             #   in_button = Button(text='Clock In')
            #    out_button = Button(text='Clock Out')
           #     btnlayout.add_widget(in_button)
           #     btnlayout.add_widget(out_button)
         
                #return bxlayout
        #dbtn = ObjectProperty(None)
        #top_layout = ObjectProperty(None)
        #def __init__(self, *args, **kwargs):
        #        super(CarsPage, self).__init__(*args, **kwargs)
        #        self.drop_down = CustomDropDown()
        #        dropdown = DropDown()
        #        notes = ['Toyota','Suburu','Prius']
        #        for note in notes:
        #                btn = Button(text='%r' % note,size_hint_y=None, height=30)
        #                btn.bind(on_release=lambda btn: dropdown.select(btn.text))
         #               dropdown.add_widget(btn)
         #       mainbutton = Button(text='Hello', size_hint=(1, 1))
         #       mainbutton.bind(on_release=dropdown.open)
         #       dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
          #      self.top_layout.add_widget(mainbutton)

        #def cars(widget, value):
             #   v = value
		#set_chosen(v)
		#chosen = v
                #chosen = v
		#labeltextcar = '[i][b][color=3388dd]CAN Tools[/color][/b][/i]\n\n\n\ntest code\n\n\n\n\n'
		#widget.ids["labelcar"].text = labeltextcar
		#if v in cars[0]:
		#	db = MySQLdb.connect(host="localhost", user="root", passwd="1234567890", db="autopen")
		#	cursor = db.cursor();
		#	usestring = "Select Exploit from exploits INNER JOIN cars ON exploits.CarsID=cars.CarsID where Model='"+ v +"';"
		#	cursor.execute(usestring);
	
		#	numrows = cursor.rowcount
		#	exploiting = cursor.fetchall()
		#	db.close()
		#	labeltextcar = '[i][b][color=3388dd]CAN Tools[/color][/b][/i]\n\n\n\n\n\n\ntestcode\n\n\n'
		#	widget.ids["labelcar"].text = labeltextcar
		#	screen_manager.current = 'carinfo'
		#	screen_manager.current_screen.cars(v)
			

    	pass	

#newstring = "<CarsInfoPage>:\n\tLabel:\n\t\ttext: '[i][b][color]=3388dd]Carss"
#nextstring = "[/color][/b][/i]'\n\t\tunderline: true\n\t\tmarkup: True\n\t\tfont_size: '40sp'\n\t\tsize_hint: .25, .1\n\t\tpos_hint: {'x': .4, 'y': .8}"
#Builder.load_string(newstring+nextstring)

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
        elif v == 'savvy':
            with open("text/savvy.txt", "r") as stream:
                labeltext1 = stream.read()
            widget.ids["label1"].text = labeltext1
            with open("text/savvy_example.txt", "r") as stream:
                labeltext2 = stream.read()
            widget.ids["label2"].text = labeltext2

        elif v == 'm2':
            with open("m2.txt", "r") as stream:
                labeltext1 = stream.read()
            widget.ids["label1"].text = labeltext1
            with open("m2_example.txt", "r") as stream:
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
        elif v == 'combine':
            with open("text/combine.txt", "r") as stream:
                labeltext1 = stream.read()
            widget.ids["label1"].text = labeltext1
            with open("text/combine_example.txt", "r") as stream:
                labeltext2 = stream.read()
            widget.ids["label2"].text = labeltext2
        elif v == 'freq':
            with open("text/freq.txt", "r") as stream:
                labeltext1 = stream.read()
            widget.ids["label1"].text = labeltext1
            with open("text/freq_example.txt", "r") as stream:
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
        screen_manager.add_widget(CarsPage(name='cars'))
        screen_manager.add_widget(MiscellaneousPage(name='miscellaneous'))
        screen_manager.add_widget(SeeAllPage(name='seeall'))
       	screen_manager.add_widget(CarInfoPage(name='carinfo'))	
	screen_manager.add_widget(DataEntryPage(name='entry'))	
        return screen_manager


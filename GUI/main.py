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


class Container():
    pass

class OtherGoodies():
    pass

class AutoPen(App):
    def build(self):

        btn = Button(text='Back', on_release=self.callback, size_hint=(0.15, 0.1), pos_hint={'x': 0, 'y': .9})
        car = Image(source='AutoPen.png')

        self.layout = FloatLayout()

        #main tools buttons
        can = Button(text='CAN', size_hint=(.2, .1), pos_hint={'x':.1, 'y':.2})
        wifi = Button(text='Wi-fi', size_hint=(.2, .1), pos_hint = {'x':.1, 'y':.6})
        bluetooth = Button(text='Bluetooth', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.2})
        SDR = Button(text='SDR', size_hint=(.2,.1), pos_hint={'x':.7, 'y':.6})

        #adding buttons to main tools
        self.layout.add_widget(can)
        self.layout.add_widget(wifi)
        self.layout.add_widget(bluetooth)
        self.layout.add_widget(SDR)

        #binding buttons to lists
        can.bind(on_press=self.callback)
        wifi.bind(on_press=self.callback)
        bluetooth.bind(on_press=self.callback)
        SDR.bind(on_press=self.callback)

        #ListView parameters
        data = [{'text': 'CAN Tools', 'is_selected': False},{'text': 'Wi-Fi Tools', 'is_selected': False},{'text': 'Bluetooth Tools', 'is_selected': False},{'text': 'Miscellaneous', 'is_selected': False}]
        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 50}
        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=False)
        list_view = ListView(adapter=list_adapter, size_hint=(0.2,0.9))
        list_view.adapter.bind(on_selection_change=self.selection_changed)
        self.layout.add_widget(btn)
        self.layout.add_widget(list_view)
        return self.layout

    def selection_changed(self, *args):
        print('    args when selection changes gets you the adapter', args)
        self.selected_item = args[0].selection[0].text

    def callback(self, value):

        if value == 'can':
            self.sub_list_view.adapter.data = [{'text': 'canutils', 'is_selected': False}, {'text': 'c0f', 'is_selected': False}, {'text': 'Kayak', 'is_selected': False}, {'text': 'UDSim', 'is_selected': False}]
        elif value == 'wifi':
            self.sub_list_view.adapter.data = [{'text': 'aircrack-ng', 'is_selected': False}]
        elif value == 'bluetooth':
            self.sub_list_view.adapter.data = [{'text': 'bluemaho', 'is_selected': False}, {'text': 'btscanner', 'is_selected': False}]
        elif value == 'SDR':
            self.sub_list_view.adapter.data = [{'text': 'gnu-radio', 'is_selected': False}]

        self.layout.do_layout()


if __name__ == "__main__":
    AutoPen().run()






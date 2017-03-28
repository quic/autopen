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

class AutoPen(App):
    def build(self):
        self.load_kv('AutoPen.kv')
        btn = Button(text='Back', on_release=self.callback, size_hint=(0.15, 0.1), pos_hint={'x': 0, 'y': .9})
        car = Image(source='AutoPen.png')

        self.layout = FloatLayout()

        data = [{'text': 'CAN Tools', 'is_selected': False},{'text': 'Wi-Fi Tools', 'is_selected': False},{'text': 'Bluetooth Tools', 'is_selected': False},{'text': 'Miscellaneous', 'is_selected': False}]
        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_y': None,
                                                 'height': 50}
        list_adapter = ListAdapter(data=data,
                                   args_converter=args_converter,
                                   cls=ListItemButton,
                                   selection_mode='single',
                                   allow_empty_selection=True)
        list_view = ListView(adapter=list_adapter, size_hint=(0.2,0.9))

        self.layout.add_widget(btn)
        self.layout.add_widget(list_view)
        return self.layout

    def callback(self, value):
        pass


if __name__ == "__main__":
    AutoPen().run()
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ZikraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        lbl = Label(text="Zikra AI Companion - Version 1.0\nReady to Build!", font_size='20sp')
        layout.add_widget(lbl)
        return layout

if __name__ == '__main__':
    ZikraApp().run()

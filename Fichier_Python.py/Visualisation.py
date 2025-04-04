from kivy.app import App
from kivy.uix.label import Label

class KivyExample(App):
    def build(self):
        return Label(text='Bonjour, Kivy!')

if __name__ == '__main__':
    KivyExample().run()

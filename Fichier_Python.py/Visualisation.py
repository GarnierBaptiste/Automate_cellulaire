from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Visualisation(BoxLayout):
    def __init__(self, mot_entree):
        super(Visualisation, self).__init__()
        self.orientation = 'horizontal'
        self.size_hint = (0.9, 0.1)
        mot = ""
        for elem in mot_entree:
            mot += elem + " "
        lab1 = Label(text=mot[:-1])
        lab2 = Label(text='Etape numéro : 0')
        self.add_widget(lab1)
        self.add_widget(lab2)

class Ecriture(BoxLayout):
    def __init__(self):
        super(Ecriture,self).__init__()
        self.padding = 100,0,100,25
        self.add_widget(TextInput())

class Entree(BoxLayout):
    def __init__(self):
        super(Entree, self).__init__()
        self.orientation = 'vertical'
        self.add_widget(TextInput())
        self.add_widget(Button(text='Lancer la simulation'))

class Mode(BoxLayout):
    def __init__(self):
        super(Mode, self).__init__()
        self.orientation = 'vertical'
        self.add_widget(Button(text='Mode 1',size_hint=(0.5, 0.5)))
        self.add_widget(Button(text='Mode 2',size_hint=(0.5, 0.5)))

class Choix(BoxLayout):
    def __init__(self):
        super(Choix, self).__init__()
        self.orientation = 'horizontal'
        self.add_widget(Entree())
        self.add_widget(Mode())

class Affichage(BoxLayout):
    def __init__(self):
        super(Affichage, self).__init__()
        self.orientation = 'vertical'
        visu = Visualisation("01110")
        self.add_widget(visu)
        ecri = Ecriture()
        self.add_widget(ecri)
        choix = Choix()
        self.add_widget(choix)

class AutomateApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        bn1 = Button(text='Button 1')
        bn2 = Button(text='Button 2')
        layout.add_widget(bn1)
        layout.add_widget(bn2)
        return Affichage()


if __name__ == '__main__':
    AutomateApp().run()
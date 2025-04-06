from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen


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
        bn_retour=Button(text='Retour',size_hint=(0.5, 0.5))
        bn_retour.bind(on_release=self.retour)
        self.add_widget(bn_retour)

    def retour(self,instance):
        App.get_running_app().root.current = 'accueil'

        
        
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

class AutomateApp(Screen):
    def __init__(self,name):
        super(AutomateApp, self).__init__()
        self.name=name
        layout = BoxLayout(orientation='vertical')
        bn1 = Button(text='Button 1')
        bn2 = Button(text='Button 2')
        bn3=Button(text='Button 3')
        layout.add_widget(bn1)
        layout.add_widget(bn2)
        layout.add_widget(bn3)
        self.add_widget(Affichage())
        
        
        

class EcranDaccueil(Screen):
    def __init__(self,name):
        super(EcranDaccueil, self).__init__()
        self.name=name
        layout=BoxLayout(orientation='vertical', spacing=20, padding=40)
        lab1=Label(text='Bienvenue sur votre simulateur de Machine de turing et d Automate Cellulaire',font_size=30)
        btn1=Button(text='Macine de turing',size_hint=(0.2,0.2),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn2=Button(text='Automate Cellulaire',size_hint=(0.2,0.2),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn1.bind(on_release=self.new_page)
        btn2.bind(on_release=self.new_page)
        layout.add_widget(lab1)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        self.add_widget(layout)
        
    def new_page(self,instance):
        self.manager.current='simulation'
    
class GestionEcrans(App):
    def build(self):
        sm = ScreenManager()
        accueil = EcranDaccueil('accueil')
        simulation = AutomateApp('simulation')
        
        sm.add_widget(EcranDaccueil('accueil'))
        sm.add_widget(AutomateApp('simulation'))
        return sm
        
if __name__ == '__main__':
    GestionEcrans().run()
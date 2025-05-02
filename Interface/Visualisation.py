from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class Visualisation(BoxLayout):
    def __init__(self, mot_entree):
        super(Visualisation, self).__init__()
        mot = ""
        for elem in mot_entree:
            mot += elem + " "
        lab1 = Label(text=mot[:-1])
        lab2 = Label(text="Numéro d'étape : 0")
        self.add_widget(lab1)
        self.add_widget(lab2)

class Ecriture(BoxLayout):
    def __init__(self):
        super(Ecriture,self).__init__()
        self.add_widget(TextInput())

class Entree(BoxLayout):
    def __init__(self):
        super(Entree, self).__init__()
        self.add_widget(TextInput())
        self.add_widget(TextInput())

class Mode(BoxLayout):
    def __init__(self):
        super(Mode, self).__init__()
        lance_simu = Button(text='Lancer la simulation', size_hint = (0.5, 0.5))
        lance_simu.bind(on_release = self.lancer_simulation)
        bn_retour=Button(text = 'Retour',size_hint = (0.5, 0.5))
        bn_retour.bind(on_release = self.retour)
        self.add_widget(lance_simu)
        self.add_widget(bn_retour)

    def retour(self,instance):
        App.get_running_app().root.current = 'Accueil'

    def lancer_simulation(self,instance):
        print(mode)

class Choix(BoxLayout):
    def __init__(self):
        super(Choix, self).__init__()
        self.add_widget(Entree())
        self.add_widget(Mode())

class Affichage(BoxLayout):
    def __init__(self):
        super(Affichage, self).__init__()
        visu = Visualisation("01110")
        self.add_widget(visu)
        ecri = Ecriture()
        self.add_widget(ecri)
        choix = Choix()
        self.add_widget(choix)

class AutomateApp(Screen):
    def __init__(self):
        super(AutomateApp, self).__init__()
        layout = BoxLayout(orientation='vertical')
        self.add_widget(Affichage())
 
class EcranDaccueil(Screen):
    def __init__(self):
        super(EcranDaccueil, self).__init__()
        layout=BoxLayout(orientation='vertical', spacing=20, padding=40)
        lab1 = Label(text="Simulateur d'Automate Cellulaire et de Machine de Turing",font_size=30)
        machine_turing = Button(text='Machine de Turing')
        autom_cell_iteration = Button(text = 'Automate Cellulaire : n itérations')
        autom_cell_transition = Button(text = 'Automate Cellulaire : transition particulière')
        autom_cell_succession = Button(text = "Automate Cellulaire : stable")
        machine_turing.bind(on_release = self.new_page_mt)
        autom_cell_iteration.bind(on_release = self.new_page_iteration)
        autom_cell_transition.bind(on_release = self.new_page_transition)
        autom_cell_succession.bind(on_release = self.new_page_succession)
        layout1 = BoxLayout(orientation = 'horizontal')
        layout2 = BoxLayout(orientation = 'vertical')
        layout3 = BoxLayout(orientation = 'vertical')
        layout2.add_widget(machine_turing)
        layout2.add_widget(autom_cell_iteration)
        layout3.add_widget(autom_cell_transition)
        layout3.add_widget(autom_cell_succession)
        layout1.add_widget(layout2)
        layout1.add_widget(layout3)
        layout.add_widget(lab1)
        layout.add_widget(layout1)
        self.add_widget(layout)

    def new_page_mt(self,instance):
        global mode
        mode = "mt"
        self.manager.current = 'Simulation'
    
    def new_page_iteration(self,instance):
        global mode
        mode = "iteration"
        self.manager.current = 'Simulation'

    def new_page_transition(self,instance):
        global mode
        mode = "transition"
        self.manager.current = 'Simulation'

    def new_page_succession(self,instance):
        global mode
        mode = "succession"
        self.manager.current = 'Simulation'
    
class GestionEcrans(App):
    def build(self):
        sm = ScreenManager()
        accueil = EcranDaccueil()
        simulation = AutomateApp()
        sm.add_widget(accueil)
        sm.add_widget(simulation)
        return sm
        
if __name__ == '__main__':
    global mode
    mode = ""
    GestionEcrans().run()
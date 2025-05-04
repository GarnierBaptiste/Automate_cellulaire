
class Machine_Turing():
    """
    QUESTION 8 :
    Classe qui represente la machine de turing avec:
        - alphabet: l'aphabet de la machine
        - les états
        - l'etat finale qui accept le mot
        - l'etat actuel lors du parcours du ruban
        - le curseur qui represente la position dans le ruban
    """
    def __init__(self,conf : dict,etats,qd,qf):
        """
        Constructeur pour la classe Machine_Turing
        """
        self.alphabet = {'0','1','_'}
        self.regle = conf
        self.etat = set(etats)
        self.etat_initiale = qd
        self.etat_finale = qf

    def get_regle(self):
        """
        Permet de récupérer les règles de la machine de turing
        """
        return self.regle
    
    def get_etat_initial(self):
        """
        Permet de récupérer l'état initial de la machine de turing
        """
        return self.etat_initiale
    
    def __str__(self):
        mot = ''
        for key,value in self.regle.items():
            mot += f"{key[0]} {key[1]} => {value[0]} {value[1]} {value[2]}\n" + "                "
        return f"La machine de turing est :\n  L'alphabet => {self.alphabet}\n  Les états => {self.etat}\n  L'état initial => {self.etat_initiale}\n  L'état final => {self.etat_finale}\n  Les règles => {mot}"

class Configuration_Machine():
    '''
    QUESTION 9 :
    Classe qui represente les configurations de la machine de turing
    '''
    def __init__(self,mot,curseur,etat):
        """
        Constructeur pour la classe Configuration
        """
        self.ruban = [elem for elem in mot]
        self.curseur = curseur
        self.etat_actuel = etat
    
    def get_ruban(self):
        """
        Permet de récupérer la configuration
        """
        return self.ruban
    
    def set_ruban(self, nouv, pos = None):
        """
        Permet de modifier la configuration à la position pos
        """
        if pos == None:
            self.ruban = nouv
        else:
            self.ruban[pos] = nouv
    
    def get_curseur(self):
        """
        Permet de récupérer la position du curseur de la configuration
        """
        return self.curseur
    
    def get_etat_actuel(self):
        """
        Permet de récupérer l'état actuel de la configuration
        """
        return self.etat_actuel
    
    def set_etat_actuel(self, nouv_etat):
        """
        Permet de modifier l'état actuel de la configuration
        """
        self.etat_actuel = nouv_etat
    
    def __str__(self):
        return f"La configuration est :\n  Le mot => {''.join(self.ruban)}\n  La position du curseur => {self.curseur}\n  L'état actuel => {self.etat_actuel}"
        
def lecture(fichier : str):
    '''
    QUESTION 10 :
    Fonction qui lis un fichier et renvoie le mot, les configuration et les etats que nous allons utiliser pour
    definir notre machine de turing.
    '''
    with open(fichier,'r') as f:
        etats = []
        configuration = {}
        lignes = f.readlines()
        mot = lignes[0].replace('\n','')
        etats.append(lignes[1].replace('\n',''))
        etats.append(lignes[2].replace('\n',''))
        for ligne in lignes[3:]:
            ligne = ligne.split(',')
            etats.append(ligne[0])
            etats.append(ligne[2])
            configuration[(ligne[0],ligne[1])] = (ligne[2],ligne[3],ligne[4].replace('\n',''))
        mt = Machine_Turing(configuration,etats,etats[0],etats[1])
        configuration_mt = Configuration_Machine(mot,0,etats[0])        
        return mt,configuration_mt

def un_pas_machine(mt : Machine_Turing, config : Configuration_Machine):
    '''
    QUESTION 11 :
    Fonction qui donne la configuration obtenue après un pas de calcul de la machine.
    '''
    etat = (config.get_etat_actuel(),config.get_ruban()[config.get_curseur()])
    config.set_ruban(mt.get_regle()[etat][1],config.get_curseur())
    match mt.get_regle()[etat][2]:
        case '<':
            config.curseur += -1
            if not config.get_curseur() > 0:
                config.set_ruban(['_'] + config.get_ruban())
                
        case '>':
            config.curseur += 1
            if not config.get_curseur() < len(config.get_ruban()):
                config.set_ruban(config.get_ruban() + ['_'])
        case '_':
            pass
    config.set_etat_actuel(mt.get_regle()[etat][0])

def calcul_machine(mt : Machine_Turing, config : Configuration_Machine):
    '''
    QUESTION 12 :
    fonction qui simule le calcul de la machine sur le mot
    '''
    while (config.get_etat_actuel(),config.get_ruban()[config.get_curseur()]) in mt.get_regle().keys():
        un_pas_machine(mt,config)
    if config.get_etat_actuel() == mt.etat_finale:
        return config.ruban
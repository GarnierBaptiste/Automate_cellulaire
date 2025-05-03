
from Automate_cellulaire import Automate,calcul_automate_q5,un_pas_automate
from Automate_cellulaire import Configuration_Automate as conf_auto


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
    def __init__(self,conf : dict,etats,q0):
        """
        Constructeur pour la classe Machine_Turing
        """
        self.alphabet = {'0','1','_'}
        self.regle = conf
        self.etat = set(etats)
        self.etat_initiale = q0

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
    
    def set_ruban(self, nouv_ruban):
        """
        Permet de modifier la configuration
        """
        self.ruban = nouv_ruban

    def set_ruban_pos(self,elem,pos):
        """
        Permet de modifier la configuration à la position pos
        """
        self.ruban[pos] = elem
    
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
        return mot,configuration,etats

def un_pas_machine(mt : Machine_Turing, config : Configuration_Machine):
    '''
    QUESTION 11 :
    Fonction qui donne la configuration obtenue après un pas de calcul de la machine.
    '''
    etat = (config.get_etat_actuel(),config.get_ruban()[config.get_curseur()])
    config.set_ruban_pos(mt.get_regle()[etat][1],config.get_curseur())
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
    if config.get_etat_actuel() == 'accept':
        return config.ruban


def simulation(mt:Machine_Turing,mot):
    etats=set()
    for lettre in mt.alphabet:
        etats.add(('*',lettre))
        for etat in mt.etat:
            etats.add((etat,lettre))
    regles={}
    with open('mt_simulation.txt','w') as f:
        for depart,futur in mt.regle.items():
            q,l=depart
            q2,futur_l,d=futur
            for i in range(3):
                for l1 in mt.alphabet:
                    for l2 in mt.alphabet:
                        triplet=[0,0,0]
                        triplet[i]=(q,l)
                        triplet[(i+1)%3]=('*',l1)
                        triplet[(i+2)%3]=('*',l2)
                        if i==0:
                            if d=='>':
                                regles[tuple(triplet)]=(q2,triplet[1][1]) 
                                f.write(str(tuple(triplet))+':'+str((q2,triplet[1][1])))
                            else:
                                regles[tuple(triplet)]=(triplet[1])   
                                f.write(str()) 
                        if i==1:
                            regles[tuple(triplet)]=('*',futur_l)
                            f.write(str(tuple(triplet))+':'+str(('*',futur_l)) )
                        
                        if i==2:
                            if d=='<':
                                regles[tuple(triplet)]=(q2,triplet[1][1])  
                            else:
                                regles[tuple(triplet)]=(triplet[1]) 
    automate=Automate(etats,regles)
    ruban = []
    for i in range(len(mot)):
        if i==0:
            ruban.append(('q0',str(mot[i])))
        else:
            ruban.append(('*',str(mot[i])))
    conf=conf_auto(ruban)
    conf_mt=Configuration_Machine(mot,0,mt.etat_initiale)
    mt_calcule=calcul_machine(mt,conf_mt)
    auto_calcule=calcul_automate_q5(conf,automate,True,False,False,True)
    return mt_calcule==auto_calcule
                    
if __name__ == "__main__":
    lec = lecture('Fichier_Texte\Machine_Turing.txt')
    mt = Machine_Turing(lec[1],lec[2],lec[2][0])
    config = Configuration_Machine(lec[0],0,mt.get_etat_initial())
    print(simulation(mt,'001'))


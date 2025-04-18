
class Machine_Turing():
    """
    QUESTION 8 :
    Classe qui represente la machine de turing avec:
        - un ruban: qui contient le mot
        - alphabet: l'aphabet de la machine
        - les états
        - l'etat finale qui accept le mot
        - l'etat actuel lors du parcours du ruban
        - le curseur qui represente la position dans le ruban
    """
    def __init__(self,etats,mot):
        """
        Constructeur pour la classe Machine_Turing
        """
        self.ruban = [elem for elem in mot]
        self.alphabet= set()
        self.etat = set(etats)
        self.etat_actuel = etats[0]
        self.etat_final = etats[1]
        self.curseur = 0

    def get_ruban(self):
        """
        Renvoie le ruban de la machine de turing
        """
        return self.ruban
    
    def set_ruban(self,ruban):
        """
        Permet de modifier le ruban
        """
        self.ruban = ruban
    
    def set_elem(self,curseur,elem):
        """
        Permet de modifier un element du ruban
        """
        self.ruban[curseur] = elem

    def get_etat_actuel(self):
        """
        Renvoie l'etat actuel de la machine de turing
        """
        return self.etat_actuel
    
    def set_etat_actuel(self,etat):
        """
        Permet de modifier l'etat actuel de la machine de turing
        """
        self.etat_actuel = etat
    
    def get_etat_final(self):
        """
        Renvoie l'etat final de la machine de turing
        """
        return self.etat_final
    
    def get_curseur(self):
        """
        Renvoie la position du curseur
        """
        return self.curseur
    
    def add_curseur(self, nb):
        """
        Permet de deplacer le curseur
        """
        self.curseur += nb

class Configuration():
    '''
    QUESTION 9 :
    Classe qui represente les configurations de la machine de turing
    '''
    def __init__(self,conf : dict):
        """
        Constructeur pour la classe Configuration
        """
        self.configuration = conf

    def get_configuration(self):
        """
        Renvoie les configurations de la machine de turing
        """
        return self.configuration
        
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
        

def un_pas(mt : Machine_Turing, config : Configuration):
    '''
    QUESTION 11 :
    Fonction qui donne la configuration obtenue apr`es un pas de calcul de la machine.
    '''
    etat = (mt.get_etat_actuel(),mt.get_ruban()[mt.get_curseur()])
    mt.set_elem(mt.get_curseur(),config.get_configuration()[etat][1])
    # mt.ruban[mt.get_curseur()] = config.get_configuration()[etat][1]
    match config.get_configuration()[etat][2]:
        case '<':
            if mt.get_curseur() > 0:
                mt.add_curseur(-1)
            else:
                mt.set_ruban(['_'] + mt.get_ruban())
        case '>':
            mt.add_curseur(1)
            if mt.get_curseur() >= len(mt.ruban):
                mt.set_ruban(mt.get_ruban() + ['_'])
        case '_':
            pass
    mt.set_etat_actuel(config.get_configuration()[etat][0])

def calcul(mt : Machine_Turing, config : Configuration):
    '''
    QUESTION 12 :
    fonction qui simule le calcul de la machine sur le mot
    '''
    while (mt.get_etat_actuel(),mt.get_ruban()[mt.get_curseur()]) in config.get_configuration().keys():
        un_pas(mt,config)
    return mt.get_etat_actuel() == mt.get_etat_final()

if __name__ == "__main__":
    lec = lecture('Fichier_Texte\Machine_Turing.txt')
    mt = Machine_Turing(lec[2],lec[0])
    config = Configuration(lec[1])
    print(calcul(mt,config))

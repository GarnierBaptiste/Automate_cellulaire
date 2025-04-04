
class Machine_Turing():
    '''
    QUESTION 8:
    Classe qui represente la machine de turing avec:
        -un ruban: qui contient le mot
        - alphabet: l'aphabet de la machine
        - les états
        - l'etat finale qui accept le mot
        - l'etat actuel lors du parcours du ruban
        - le curseur qui represente la position dans le ruban'''
    def __init__(self,etats,mot):
        self.ruban = [elem for elem in mot]
        self.alphabet= set()
        self.etat = set(etats)
        self.etat_actuel = etats[0]
        self.etat_finale = etats[1]
        self.curseur=0

class Configuration():
    '''
    QUESTION 9:
    Classe qui represente les configurations de la machine de turing
    '''
    def __init__(self,conf):
        self.configuration=conf
        
def lecture(fichier):
    '''
    QUESTION 10
    fonction qui lis un fichier et renvoie le mot,les configuration et les etats que nous allons utiliser pour
    definir notre machine de turing
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
    QUESTION 11:
    Fonction qui donne la configuration obtenue apr`es un pas de calcul de la machine.
    '''
    etat = (mt.etat_actuel,mt.ruban[mt.curseur])
    mt.ruban[mt.curseur] = config.configuration[etat][1]
    match config.configuration[etat][2]:
        case '<':
            if mt.curseur > 0:
                mt.curseur -= 1
            else:
                mt.ruban = ['_'] + mt.ruban
        case '>':
            mt.curseur += 1
            if mt.curseur >= len(mt.ruban)-1:
                mt.ruban.append('_')
        case '_':
            pass
    mt.etat_actuel = config.configuration[etat][0]

def calcul(mt:Machine_Turing,config:Configuration):
    '''
    QUESTION 12:
    fonction qui simule le calcul de la machine sur le mot
    '''
    while (mt.etat_actuel,mt.ruban[mt.curseur]) in config.configuration.keys():
        un_pas(mt,config)
    if mt.etat_actuel==mt.etat_finale:
        return True
    else:
        return False

if __name__ == "__main__":
    lec = lecture('example.txt')
    mt = Machine_Turing(lec[2],lec[0])
    config = Configuration(lec[1])
    print(calcul(mt,config))

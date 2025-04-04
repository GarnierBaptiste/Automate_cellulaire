
class Machine_Turing():
    def __init__(self,etats,mot):
        self.ruban = [elem for elem in mot]
        self.alphabet= set()
        self.etat = set(etats)
        self.etat_actuel = etats[0]
        self.curseur=0

class Configuration():
    def __init__(self,conf):
        self.configuration=conf
        
def lecture(fichier):
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
                mt.ruban.appen('_')
        case '_':
            pass
    mt.etat_actuel = config.configuration[etat][0]

if __name__ == "__main__":
    lec = lecture('example.txt')
    mt = Machine_Turing(lec[2],lec[0])
    config = Configuration(lec[1])
    print(un_pas(mt,config))
    print(mt.ruban)
    print(mt.etat_actuel)

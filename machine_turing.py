
class Machine_Turing():
    def __init__(self,etats):
        self.ruban=[]
        self.alphabet=set(0,1,'_')
        self.etat=etats
        self.curseur=0

class Configuration():
    def __init__(self,conf):
        self.configuration=conf
        
def lecture(fichier):
    with open(fichier,'r') as f:
        etats=set()
        configuration=[]
        lignes=f.readlines()
        mot=lignes[0][0].replace('\n','')
        etats.add(lignes[1][0].replace('\n',''))
        etats.add(lignes[2][0].replace('\n',''))
        for ligne in lignes[2:]:
            ligne=ligne.split(',')
            etats.add(ligne[0])
            etats.add(ligne[2])
            configuration.append((ligne[0],ligne[1],ligne[2],ligne[3],ligne[4].replace('\n','')))
        return mot,configuration,etats
        
        
lecture('example.txt')
        
        




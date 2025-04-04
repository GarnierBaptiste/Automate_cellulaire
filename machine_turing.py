
class Machine_Turing():
    def __init__(self,etats):
        self.ruban=[]
        self.alphabet=set(0,1,'_')
        self.etat=etats

class Configuration():
    def __init__(self,conf):
        self.configuration=conf
        
def lecture(fichier):
    with open(fichier,'r') as f:
        lignes=[]
        for ligne in f:
            ligne=ligne.split()
            if ligne !=[]:
                lignes.append(ligne)
            
        print(lignes) 
        # lignes=f.readlines().split('\n')
        # etats=set([lignes[0].split('\n'),lignes[1]])
        # temp=[]
        # for elem in lignes[2:]:
        #     print(temp)
        #     # if elem != '':
        #     #     temp.append((elem.split(',')))
        # print(etats)
            
        
lecture('example.txt')
        
        




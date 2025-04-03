class Grille:
    def __init__(self, mot, automate_cellulaire):
        self.automate=automate_cellulaire  #les transitions
        self.taille = len(mot)
        self.ruban = [str(elem) for elem in mot]
        liste = []
        for elem in self.ruban:
            if elem not in liste:
                liste.append(elem)
        self.etat_cellules = liste
        
    def get_taille(self):
        return self.taille
    
    def get_ruban(self):
        return self.ruban
    '''
    Permet de passer de self.ruban a un mot c'est a dire que si j'ai ['1','0','1','1,'] la fonction renvoie '1011'
    '''
    def get_mot(self):
        nv_mot=''
        for lettre in self.ruban:
            nv_mot+=lettre
        return nv_mot

    def get_etat_cellules(self):
        return self.etat_cellules
    
    def set_ruban(self, grille):
        self.ruban =[str(elem) for elem in grille] 

    def get_elem(self,i):
        return self.get_ruban()[i]
        

    def __str__(self):
        mot = ""
        for elem in self.get_ruban():
            mot += elem + " "
        return "Taille : " + str(self.taille) + " \n  Mot  : " + mot[:-1]
        
    
    
    def regle_110(self):
        nouvelle_grille = self.get_ruban()
        for i in range(self.taille):
            i0,i1,i2 = (i-1)%self.taille, (i)%self.taille, (i+1)%self.taille
            etat = (self.get_elem(i0),self.get_elem(i1),self.get_elem(i2))
            match etat:
                case ('1','1','1'):
                    nouvelle_grille[i] = 0
                case ('1','1','0'):
                    nouvelle_grille[i] = 1
                case ('1','0','1'):
                    nouvelle_grille[i] = 1
                case ('1','0','0'):
                    nouvelle_grille[i] = 0
                case ('0','1','1'):
                    nouvelle_grille[i] = 1
                case ('0','1','0'):
                    nouvelle_grille[i] = 1
                case ('0','0','1'):
                    nouvelle_grille[i] = 1
                case ('0','0','0'):
                    nouvelle_grille[i] = 0
        self.set_ruban(nouvelle_grille)
    
    def recup(self,automate):
        with open(automate,'r') as f:
            lignes=f.readlines()
            code=lignes[:-1]
            mot=lignes[len(lignes)-1]
                
    def un_pas(self):
        nv_ruban=[]
        for i in range(len(self.ruban)):
            if i>0 and i < len(self.ruban)-1:
                transition=(self.ruban[i-1],self.ruban[i],self.ruban[i+1])
                nv_ruban.append(self.automate[transition])
            elif i==0:
                transition=('0',self.ruban[0],self.ruban[1])
                nv_ruban.append(self.automate[transition])
            else:
                transition=(self.ruban[len(self.ruban)-2],self.ruban[len(self.ruban)-1],'0')
                nv_ruban.append(self.automate[transition]) 
        return (nv_ruban,transition)
        
    def calcul_automate(self,iteration=None,transition_particuliere=None,succession=None):
        '''
        QUESTION 5: : Ecrire une fonction qui prend comme argument un mot et un automate cellulaire et qui 
                simule le calcul de l'automate. Vous proposerez plusieurs modes pour arrêter le calcul :
                — apr`es un nombre de pas de calcul donnée
                — apr`es l'application d'une transition particuli`ere
                — quand il n y a pas de changements entre deux configurations successives
        '''
        
        if iteration:
            # print(self.get_mot())
            print('je suis l iteration')
            for i in range(iteration):
                self.ruban=self.un_pas()[0]
                print(self.get_mot())
            return self.ruban
        elif transition_particuliere:
            print('je suis la transition particulier')
            print(self.get_mot())
            self.ruban,transition=self.un_pas()
            print(self.get_mot())
            while transition!=transition_particuliere:
                self.ruban,transition=self.un_pas()
                print(self.get_mot())
            return self.ruban
        elif succession:
            print('je suis la succession')
            conf1=self.ruban
            print(self.get_mot())
            self.ruban=self.un_pas()[0]
            conf2=self.ruban
            print(self.get_mot())
            print(conf1,conf2)
            while conf1!=conf2:
                conf1=conf2
                self.ruban=self.un_pas()[0]
                print(self.get_mot())
                conf2=self.ruban
                # print(conf1,conf2)
            return self.ruban


if __name__ == '__main__':
    dico={('1','1','1'):'0',('1','1','0'):'1',('1','0','1'):'1',('1','0','0'):'0',('0','1','1'):'1',('0','1','0'):'1',('0','0','1'):'1',('0','0','0'):'0'}
    # dico={('1','1','1'):'0',('1','1','0'):'0',('1','0','1'):'0',('1','0','0'):'0',('0','1','1'):'0',('0','1','0'):'0',('0','0','1'):'0',('0','0','0'):'0'}
    tableau = Grille('0001000',dico)
    print(tableau.calcul_automate(None,(None),None))
    
    # tableau.set_elem(9,2)
    # print(tableau.ruban)
    # print(tableau)
    # recup('auto.txt')
    

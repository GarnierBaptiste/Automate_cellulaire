class Automate:
    """
    QUESTION 1 :
    Proposer une structure de données qui permet de représenter un automate cellulaire. 
    """
    def __init__(self,transition,etats):
        """
        Constructeur pour la classe Automate
        """
        self.etat_cellules = etats
        self.transition = transition
        

    def get_regles(self):
        """
        Permet de reécupérer les règles qui définissent l'automate cellulaire
        """
        return self.regle
    
    def get_etat_cellules(self):
        """
        Permet de récupérer les état possibles des celullues de l'automate 
        """
        return self.etat_cellules
    
    def updates_regles(self):
        """
        Permet de définir les règles de l'automate cellulaire
        """
        self.regle = recup('Automate_cellulaire.txt')
        self.etat_cellules = recup(self.regle)

class Configuration:
    """
    QUESTION 2 :
    Proposer une structure de données pour représenter la configuration d'un automate cellulaire
    """
    def __init__(self, mot : str):
        """
        Constructeur pour la classe Configuration
        """
        self.mot = [str(elem) for elem in mot]

    def get_taille(self):
        """
        Renvoie la taille du mot
        """
        return len(self.mot)
    
    def get_mot(self):
        """
        Renvoie la liste qui correspond au mot de l'élément
        """
        return self.mot
    
    def get_joli_mot(self):
        """
        Permet de passer d'une liste a un str c'est a dire que si j'ai 
        ['1','0','1','1,'] la fonction renvoie '1011'
        """
        nv_mot=''
        for lettre in self.mot:
            nv_mot+=lettre
        return nv_mot
    
    def set_mot(self, nouv_mot):
        """
        Modifie l'attribut mot de l'element
        """
        self.mot = nouv_mot
    
    def __str__(self):
        """
        Modifie l'affichage des objets de la classe Configuration 
        """
        mot = ''
        for elem in self.get_joli_mot():
            mot += elem + " "
        return "Taille : " + str(self.get_taille()) + " \n  Mot  : " + mot[:-1]

def recup(fonc):
    """
    Permet de récupérer les données
    """
    def recup_regle(nom_fichier : str):
        """
        Récupère les règles de l'automate cellulaire à parir d'un fichier texte
        """
        dico = {}
        with open(nom_fichier,'r') as f:
            lignes=f.readlines()
            for i in range(len(lignes)):
                elem = lignes[i].replace('\n','').split(' -> ')
                tuple_key = (elem[0][0],elem[0][2],elem[0][4])
                dico[tuple_key] = elem[1]
        return dico

    def recup_etat_cellule(regle : dict):
        """
        Récupère les états possibles des cellules de l'automate cellulaire
        """
        etat_cellule = set()
        for key, value in regle.items():
            for i in range(3):
                etat_cellule.add(key[i])
            etat_cellule.add(value)
        return etat_cellule
    
    if type(fonc) == str:
        return recup_regle(fonc)
    elif type(fonc) == dict:
        return recup_etat_cellule(fonc)
    
def initialisation(nom_fichier, mot_entre : str):
    """
    QUESTION 3 :
    Ecrire une fonction qui lit un fichier texte contenant le code d'un automate cellulaire 
    et un d'mot d'entrée et qui initialise la structure de données pour représenter cet automate.
    """
    auto = Automate(nom_fichier)
    mot = Configuration(mot_entre)
    return auto,mot

def un_pas(mot : Configuration,automate : Automate):
    """
    QUESTION 4 : 
    Donner une fonction qui prend en argument un automate cellulaire et une configuration 
    et qui donne la configuration obtenue après un pas de calcul de l'automate.
    """
    nv_ruban=[]
    taille = mot.get_taille()-1
    for i in range(taille+1):
        if i>0 and i < taille:
            transition=(mot.get_mot()[i-1],mot.get_mot()[i],mot.get_mot()[i+1])
            nv_ruban.append(automate.regle[transition])
        elif i==0:
            transition=('0',mot.get_mot()[0],mot.get_mot()[1])
            nv_ruban.append(automate.regle[transition])
        else:
            transition=(mot.get_mot()[len(mot.get_mot())-2],mot.get_mot()[len(mot.get_mot())-1],'0')
            nv_ruban.append(automate.regle[transition]) 
    return (nv_ruban,transition)

def calcul_automate(mot:Configuration,automate:Automate,iteration : int = None,transition_particuliere : bool = None,succession : bool = None):
    """
    QUESTION 5 :
    Ecrire une fonction qui prend comme argument un mot et un automate cellulaire et qui 
    simule le calcul de l'automate. Vous proposerez plusieurs modes pour arrêter le calcul :
    — apr`es un nombre de pas de calcul donnée
    — apr`es l'application d'une transition particuli`ere
    — quand il n y a pas de changements entre deux configurations successives

    Question 6 : 
    Modifier la fonction précédente pour que, à chaque pas de simulation, la configuration 
    de l'automate s'affiche de manière compréhensible
    """
    print(mot.get_joli_mot())
    if iteration:
        print('je suis l iteration')
        for i in range(iteration):
            mot.set_mot(un_pas(mot,auto)[0])
            print(mot.get_joli_mot())
        return mot.get_mot()
    elif transition_particuliere:
        print('je suis la transition particulier')
        print(mot.get_joli_mot())
        mot.get_mot(),transition = un_pas(mot,automate)
        print(mot.get_joli_mot())
        while transition!=transition_particuliere:
            pas = un_pas(mot,automate)
            mot.set_mot(pas[0])
            transition = pas[1]
            print(mot.get_joli_mot())
        return mot.get_mot()
    elif succession:
        print('je suis la succession')
        conf1 = mot.get_mot()
        print(mot.get_joli_mot())
        mot.set_mot(un_pas(mot,auto)[0])
        conf2 = mot.get_mot()
        print(mot.get_joli_mot())
        print(conf1,conf2)
        while conf1!=conf2:
            conf1 = conf2
            mot.set_mot(un_pas(mot,auto)[0])
            print(mot.get_joli_mot())
            conf2 = mot.get_mot()
        return mot.get_mot()


if __name__ == "__main__":
    auto, config = initialisation('Fichier_Texte\Automate_cyclique.txt','0001000')
    calcul_automate(config,auto,iteration = 10)
    
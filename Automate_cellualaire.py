class Automate:
    """
    Classe qui représente l'automate cellualire par ces règles ainsi que l'état des cellules
    """
    def __init__(self,nom_fichier):
        """
        Constructeur pour la classe Automate
        """
        self.regle = recup(nom_fichier)
        self.etat_cellules = recup(self.regle)

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
    Classe qui représente les mots qu'on mettra dans l'automate cellulaire
    """
    def __init__(self, mot):
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
        Permet de passer d'une liste a un str c'est a dire que si j'ai 
        ['1','0','1','1,'] la fonction renvoie '1011'
        """
        nv_mot=''
        for lettre in self.mot:
            nv_mot+=lettre
        return nv_mot
    
    def __str__(self):
        """
        Modifie l'affichage des objets de la classe Configuration 
        """
        mot = ''
        for elem in mot.get_mot():
            mot += elem + " "
        return "Taille : " + str(self.get_taille()) + " \n  Mot  : " + mot[:-1]

def recup(fonc):
    """
    Permet de récupérer les données
    """
    def recup_regle(automate):
        """
        Récupère les règles de l'automate cellulaire à parir d'un fichier texte
        """
        dico = {}
        with open(automate,'r') as f:
            lignes=f.readlines()
            for i in range(len(lignes)):
                elem = lignes[i].replace('\n','').split(' -> ')
                tuple_key = (elem[0][0],elem[0][2],elem[0][4])
                dico[tuple_key] = elem[1]
        return dico

    def recup_etat_cellule(regle):
        """
        Récupère les états possibles des cellules de l'automate cellulaire
        """
        etat_cellule = set()
        for key, value in regle.items():
            etat_cellule.add(key[0])
            etat_cellule.add(key[1])
            etat_cellule.add(key[2])
            etat_cellule.add(value)
        return etat_cellule
    
    if type(fonc) == str:
        return recup_regle(fonc)
    elif type(fonc) == dict:
        return recup_etat_cellule(fonc)

def un_pas(mot : Configuration,automate : Automate):
    """
    QUESTION 4 : : Donner une fonction qui prend en argument un automate cellulaire 
    et une configuration et qui donne la configuration obtenue après un pas de calcul de l’automate.
    """
    nv_ruban=[]
    taille = mot.get_taille()-1
    for i in range(taille+1):
        if i>0 and i < taille:
            transition=(mot.mot[i-1],mot.mot[i],mot.mot[i+1])
            nv_ruban.append(automate.regle[transition])
        elif i==0:
            transition=('0',mot.mot[0],mot.mot[1])
            nv_ruban.append(automate.regle[transition])
        else:
            transition=(mot.mot[len(mot.mot)-2],mot.mot[len(mot.mot)-1],'0')
            nv_ruban.append(automate.regle[transition]) 
    return (nv_ruban,transition)

def calcul_automate(mot:Configuration,automate:Automate,iteration=None,transition_particuliere=None,succession=None):
    """
    QUESTION 5: : Ecrire une fonction qui prend comme argument un mot et un automate cellulaire et qui 
    simule le calcul de l'automate. Vous proposerez plusieurs modes pour arrêter le calcul :
    — apr`es un nombre de pas de calcul donnée
    — apr`es l'application d'une transition particuli`ere
    — quand il n y a pas de changements entre deux configurations successives
    """
    print(mot.get_mot())
    if iteration:
        print('je suis l iteration')
        for i in range(iteration):
            mot.mot=un_pas(mot,auto)[0]
            print(mot.get_mot())
        return mot.mot
    elif transition_particuliere:
        print('je suis la transition particulier')
        print(mot.get_mot())
        mot.mot,transition=un_pas(mot,automate)
        print(mot.get_mot())
        while transition!=transition_particuliere:
            mot.mot,transition=un_pas(mot,automate)
            print(mot.get_mot())
        return mot.mot
    elif succession:
        print('je suis la succession')
        conf1=mot.mot
        print(mot.get_mot())
        mot.mot=un_pas(mot,auto)[0]
        conf2=mot.mot
        print(mot.get_mot())
        print(conf1,conf2)
        while conf1!=conf2:
            conf1=conf2
            mot.mot=un_pas(mot,auto)[0]
            print(mot.get_mot())
            conf2=mot.mot
        return mot.mot

def initialisation(nom_fichier, mot_entre):
    """
    QUESTION 3 : : Ecrire une fonction qui lit un fichier texte contenant le code d'un automate
    cellulaire et un d'mot d'entrée et qui initialise la structure de données pour représenter cet automate.
    """
    auto = Automate(nom_fichier)
    mot = Configuration(mot_entre)
    return auto,mot

if __name__ == "__main__":
    auto, config = initialisation('Fichier_Automate\Automate_infini.txt','0001000')
    calcul_automate(config,auto,iteration=3)
    
class Automate:
    """
    QUESTION 1 :
    Proposer une structure de données qui permet de représenter un automate cellulaire. 
    """
    def __init__(self,etats,transitions):
        """
        Constructeur pour la classe Automate
        """
        self.etat_cellules = etats
        self.regle = transitions

    def get_regles(self):
        """
        Permet de reécupérer les règles qui définissent l'automate cellulaire
        """
        return self.regle
    
    def __str__(self):
        """
        Modifie la fonction de "print" pour la classe "Automate"
        """
        mot = ''
        for key, value in self.regle.items():
            mot += f"{key[0]} {key[1]} {key[2]} -> {value}\n" + "                     "
        return f"L'automate cellulaire est :\n  Les tats possibles => {self.etat_cellules}\n  Les regles disponibles => {mot}"

class Configuration_Automate:
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
    
    def get_mot(self,mode=0):
        """
        Renvoie la liste qui correspond au mot de l'élément
        """
        if mode == 0:
            return self.mot
        else:
            return ''.join(self.mot)

    def set_mot(self, nouv_mot):
        """
        Modifie l'attribut mot de l'element
        """
        self.mot = nouv_mot
    
def initialisation(nom_fichier, mot_entre : str):
    """
    QUESTION 3 :
    Ecrire une fonction qui lit un fichier texte contenant le code d'un automate cellulaire 
    et un d'mot d'entrée et qui initialise la structure de données pour représenter cet automate.
    """
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
        
        return (recup_etat_cellule(recup_regle(fonc)),recup_regle(fonc))

    etats,regles=recup(nom_fichier)
    auto = Automate(etats,regles)
    mot = Configuration_Automate(mot_entre)
    return auto,mot

def un_pas_automate(conf : Configuration_Automate,automate : Automate):
    """
    QUESTION 4 : 
    Donner une fonction qui prend en argument un automate cellulaire et une configuration 
    et qui donne la configuration obtenue après un pas de calcul de l'automate.
    """
    nv_ruban=[]
    taille = conf.get_taille()-1
    for i in range(taille+1):
        if i>0 and i < taille:
            transition=(conf.get_mot()[i-1],conf.get_mot()[i],conf.get_mot()[i+1])
            nv_ruban.append(automate.get_regles()[transition])
        elif i==0:
            transition=('0',conf.get_mot()[0],conf.get_mot()[1])
            nv_ruban.append(automate.get_regles()[transition])
        else:
            transition=(conf.get_mot()[len(conf.get_mot())-2],conf.get_mot()[len(conf.get_mot())-1],'0')
            nv_ruban.append(automate.get_regles()[transition]) 
    return (nv_ruban,transition)

def calcul_automate_q5(conf:Configuration_Automate,automate:Automate,iteration : int = None,transition_particuliere : bool = None,succession : bool = None):
    """
    QUESTION 5 :
    Ecrire une fonction qui prend comme argument un mot et un automate cellulaire et qui 
    simule le calcul de l'automate. Vous proposerez plusieurs modes pour arrêter le calcul :
    — apr`es un nombre de pas de calcul donnée
    — apr`es l'application d'une transition particulière
    — quand il n y a pas de changements entre deux configurations successives
    """
    if iteration:
        for _ in range(iteration):
            conf.set_mot(un_pas_automate(conf,automate)[0])
        return conf.get_mot()
    elif transition_particuliere:
        nv_conf,transition = un_pas_automate(conf,automate)
        conf=Configuration_Automate(nv_conf)
        while transition!=transition_particuliere:
            pas = un_pas_automate(conf,automate)
            conf.set_mot(pas[0])
            transition = pas[1]
        return conf.get_mot()
    elif succession:
        conf1 = conf.get_mot()
        conf.set_mot(un_pas_automate(conf,automate)[0])
        conf2 = conf.get_mot()
        while conf1!=conf2:
            conf1 = conf2
            conf.set_mot(un_pas_automate(conf,automate)[0])
            conf2 = conf.get_mot()
        return conf.get_mot()
    
def calcul_automate_q6(conf:Configuration_Automate,automate:Automate,iteration : int = None,transition_particuliere : bool = None,succession : bool = None):
    """
    QUESTION 6 : 
    Modifier la fonction précédente pour que, à chaque pas de simulation, la configuration 
    de l'automate s'affiche de manière compréhensible
    """
    print(conf.get_mot(1))
    if iteration:
        print('je suis l iteration')
        for _ in range(iteration):
            conf.set_mot(un_pas_automate(conf,automate)[0])
            print(conf.get_mot(1))
        return conf.get_mot()
    elif transition_particuliere:
        print('je suis la transition particulier')
        print(conf.get_mot(1))
        nv_conf,transition = un_pas_automate(conf,automate)
        conf=Configuration_Automate(nv_conf)
        while transition!=transition_particuliere:
            pas = un_pas_automate(conf,automate)
            conf.set_mot(pas[0])
            transition = pas[1]
            print(conf.get_mot(1))
        return conf.get_mot()
    elif succession:
        print('je suis la succession')
        conf1 = conf.get_mot()
        print(conf.get_mot(1))
        conf.set_mot(un_pas_automate(conf,automate)[0])
        conf2 = conf.get_mot()
        print(conf.get_mot(1))
        print(conf1,conf2)
        while conf1!=conf2:
            conf1 = conf2
            conf.set_mot(un_pas_automate(conf,automate)[0])
            print(conf.get_mot(1))
            conf2 = conf.get_mot()
        return conf.get_mot()
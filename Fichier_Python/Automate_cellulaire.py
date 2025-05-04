import ast

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
        return f"L'automate cellulaire est :\n  Les états possibles => {self.etat_cellules}\n  Les regles disponibles => {mot}"

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

    def __str__(self):
        return f"La configuration est :\n  Le mot => {self.get_mot(1)}"
    
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

    etats,regles = recup(nom_fichier)
    auto = Automate(etats,regles)
    mot = Configuration_Automate(mot_entre)
    return auto,mot

def un_pas_automate(conf : Configuration_Automate,automate : Automate,simulation:bool ):
    """
    QUESTION 4 : 
    Donner une fonction qui prend en argument un automate cellulaire et une configuration 
    et qui donne la configuration obtenue après un pas de calcul de l'automate.
    """
    nv_ruban = []
    taille = conf.get_taille()
    mot = conf.get_mot()
    if not simulation:
        for i in range(taille):
            if i>0 and i < taille-1:
                transition = (mot[i-1],mot[i],mot[i+1])
            elif i == 0:
                transition = ('0',mot[0],mot[1])
            else:
                transition = (mot[len(mot)-2],mot[len(mot)-1],'0')
            if transition not in automate.get_regles().keys():
                nv_ruban.append(mot[i])
            else:
                nv_ruban.append(automate.get_regles()[transition])
    #partie pour traiter la simulation d'une Machine de turing en Automate Cellulaire
    if simulation:
        #permet d'avoir une liste de tuple tel que (('q0','1),('*',1'),..) et non ("('q0',1),('*','1'),...)")
        nouvelle_conf = [ast.literal_eval(item) for item in tuple(mot)]
        for i in range(taille):
            if i>0 and i < taille-1:
                transition = (nouvelle_conf[i-1],nouvelle_conf[i],nouvelle_conf[i+1])
            elif i == 0:
                transition = (('*','_'),nouvelle_conf[i],nouvelle_conf[i+1])
            else:
                transition = (nouvelle_conf[i-1],nouvelle_conf[i],('*','_'))
            if transition in automate.get_regles().keys():
                nv_ruban.append(automate.get_regles()[transition])
            else:
                nv_ruban.append(nouvelle_conf[i])
        temp = (tuple(repr(item) for item in nv_ruban)) 
        nv_ruban = temp               
    return nv_ruban

def calcul_automate_q5(conf:Configuration_Automate,automate:Automate,simulation:bool,iteration : int = None,trans_part : tuple = None,succession : bool = None):
    """
    QUESTION 5 :
    Ecrire une fonction qui prend comme argument un mot et un automate cellulaire et qui 
    simule le calcul de l'automate. Vous proposerez plusieurs modes pour arrêter le calcul :
    — apr`es un nombre de pas de calcul donnée
    — apr`es l'application d'une transition particulière
    — quand il n y a pas de changements entre deux configurations successives
    """
    i = 0
    if iteration:
        for _ in range(iteration):
            conf.set_mot(un_pas_automate(conf,automate,simulation))
            i+=1
    elif trans_part:
        trans_part = trans_part[0]+trans_part[1]+trans_part[2]
        while True:
            if trans_part in '0'+conf.get_mot(1)+'0':
                conf.set_mot(un_pas_automate(conf,automate,simulation))
                break
            else:
                conf.set_mot(un_pas_automate(conf,automate,simulation))
            if i > len(automate.get_regles()):
                return f"La transition {(trans_part[0],trans_part[1],trans_part[2])} n'a jamais été appliquée"
            i += 1
    elif succession:
        conf1 = conf.get_mot()
        conf.set_mot(un_pas_automate(conf,automate,simulation))
        conf2 = conf.get_mot()
        while conf1!=conf2:
            conf1 = conf2
            conf.set_mot(un_pas_automate(conf,automate,simulation))
            conf2 = conf.get_mot()
            if i > len(automate.get_regles()):
                return "La configuration ne devient pas un stable"
            i += 1
    if simulation:
        res= [ast.literal_eval(item)[1] for item in conf.get_mot()]
        return res
    else:
        return (conf.get_mot(),i)

        
    
def calcul_automate_q6(conf:Configuration_Automate,automate:Automate,simulation:bool,iteration : int = None,trans_part : tuple = None,succession : bool = None):
    """
    QUESTION 6 : 
    Modifier la fonction précédente pour que, à chaque pas de simulation, la configuration 
    de l'automate s'affiche de manière compréhensible
    """
    print("Voici la configuration au début\n",conf)
    i = 0
    if iteration:
        print(f'Nous allons itérer {iteration} fois la configuration avec les règles de l\'automate ci dessus\n')
        for j in range(iteration):
            conf.set_mot(un_pas_automate(conf,automate,simulation))
            print(f"Voici la configuration à l'itération numéro {j+1}\n",conf,"\n")
    elif trans_part:
        print(f'Nous recherchons si la transition {trans_part} est appliquée\n')
        trans_part = trans_part[0]+trans_part[1]+trans_part[2]
        while True:
            if trans_part in '0'+conf.get_mot(1)+'0':
                conf.set_mot(un_pas_automate(conf,automate,simulation))
                print(f"Voici la configuration après {i+1} itérations", conf,"\n")
                break
            conf.set_mot(un_pas_automate(conf,automate,simulation))
            print(f"Voici la configuration après {i+1} itérations",conf,"\n")
            if i == len(automate.get_regles()):
                return f"La transition {(trans_part[0],trans_part[1],trans_part[2])} n'a jamais été appliquée"
            i += 1
    elif succession:
        print("Nous recherchons s'il y a une succession \n")
        conf1 = conf.get_mot()
        conf.set_mot(un_pas_automate(conf,automate))
        conf2 = conf.get_mot()
        while conf1!=conf2:
            conf1 = conf2
            conf.set_mot(un_pas_automate(conf,automate))
            print(f"Voici la configuration après {i} itérations\n",conf,"\n")
            conf2 = conf.get_mot()
            if i == len(automate.get_regles()):
                return "La configuration ne contient pas de succession"
            i += 1
    if simulation:
        res= [ast.literal_eval(item)[1] for item in conf.get_mot()]
        return res
    else:
        return (conf.get_mot(),i)


# exemple
# etats = ['0', '1']
# regle = {
#     ('1','1','1'): '0',
#     ('1','1','0'): '1',
#     ('1','0','1'): '1',
#     ('1','0','0'): '0',
#     ('0','1','1'): '1',
#     ('0','1','0'): '1',
#     ('0','0','1'): '1',
#     ('0','0','0'): '0'
# }
# config_init = Configuration_Automate("0001000")
# automate=Automate(etats,regle)
# print(calcul_automate_q5(config_init,automate,False,3))
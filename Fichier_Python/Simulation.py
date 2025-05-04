from Automate_cellulaire import Automate,Configuration_Automate,calcul_automate_q5
from Machine_Turing import Machine_Turing,Configuration_Machine,calcul_machine

def simulation(mt:Machine_Turing,mot):
    """
    QUESTION 13 : Programmer une fonction qui prend en entrée le code d'une machine de Turing et construit
    l'automate cellulaire qui la simule. Tester sur plusieurs exemples que la machine de Turing et sa simulation
    par un automate cellulaire font le même calcul.
    """
    def ruban_sans_tiret(ruban):
        '''
        Cette fonction permet de renvoyer un ruban qui ne contient pas de '_'. Pour pouvoir par la suite
        dans la simulation comparer sans probleme la reponse obtenue par notre fonction de calcule de la machine de turing
        et celle de l'automate cellulaire.
        '''
        while ruban and ruban[0] == '_':
            ruban.pop(0)
        while ruban and ruban[-1] == '_':
            ruban.pop()
        return ruban
    
    etats = set()
    for lettre in mt.alphabet:
        etats.add(('*',lettre))
        for etat in mt.etat:
            etats.add((etat,lettre))
    regles = {}
    for depart,futur in mt.regle.items():
        q,l = depart
        q2,futur_l,d = futur
        for i in range(3):
            for l1 in mt.alphabet:
                for l2 in mt.alphabet:
                    triplet = [0,0,0]
                    triplet[i] = (q,l)
                    triplet[(i+1)%3] = ('*',l1)
                    triplet[(i+2)%3] = ('*',l2)
                    if i == 0:
                        if d == '>':
                            regles[tuple(triplet)] = (q2,triplet[1][1]) 
                        else:
                            regles[tuple(triplet)] = (triplet[1])   
                    if i == 1:
                        regles[tuple(triplet)] = ('*',futur_l)
                    if i == 2:
                        if d == '<':
                            regles[tuple(triplet)] = (q2,triplet[1][1])  
                        else:
                            regles[tuple(triplet)] = (triplet[1]) 
    automate = Automate(etats,regles)
    ruban = []
    for i in range(len(mot)):
        if i == 0:
            ruban.append(('q0',str(mot[i])))
        else:
            ruban.append(('*',str(mot[i])))
    conf = Configuration_Automate(ruban)
    conf_mt = Configuration_Machine(mot,0,mt.etat_initiale)
    mt_calcule = ruban_sans_tiret(calcul_machine(mt,conf_mt))
    auto_calcule = calcul_automate_q5(conf,automate,True,False,False,True)
    if mt_calcule == auto_calcule:
        return automate, conf,True
    else:
        return automate, conf,False
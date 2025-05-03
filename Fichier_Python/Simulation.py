from Automate_cellulaire import Automate,calcul_automate_q5,un_pas_automate
from Automate_cellulaire import Configuration_Automate as conf_auto
from Machine_Turing import Machine_Turing,Configuration_Machine,calcul_machine,lecture


def simulation(mt:Machine_Turing,mot):
    etats=set()
    for lettre in mt.alphabet:
        etats.add(('*',lettre))
        for etat in mt.etat:
            etats.add((etat,lettre))
    regles={}
    with open('mt_simulation.txt','w') as f:
        for depart,futur in mt.regle.items():
            q,l=depart
            q2,futur_l,d=futur
            for i in range(3):
                for l1 in mt.alphabet:
                    for l2 in mt.alphabet:
                        triplet=[0,0,0]
                        triplet[i]=(q,l)
                        triplet[(i+1)%3]=('*',l1)
                        triplet[(i+2)%3]=('*',l2)
                        if i==0:
                            if d=='>':
                                regles[tuple(triplet)]=(q2,triplet[1][1]) 
                                f.write(str(tuple(triplet))+':'+str((q2,triplet[1][1])))
                            else:
                                regles[tuple(triplet)]=(triplet[1])   
                                f.write(str()) 
                        if i==1:
                            regles[tuple(triplet)]=('*',futur_l)
                            f.write(str(tuple(triplet))+':'+str(('*',futur_l)) )
                        
                        if i==2:
                            if d=='<':
                                regles[tuple(triplet)]=(q2,triplet[1][1])  
                            else:
                                regles[tuple(triplet)]=(triplet[1]) 
    automate=Automate(etats,regles)
    ruban = []
    for i in range(len(mot)):
        if i==0:
            ruban.append(('q0',str(mot[i])))
        else:
            ruban.append(('*',str(mot[i])))
    conf=conf_auto(ruban)
    conf_mt=Configuration_Machine(mot,0,mt.etat_initiale)
    mt_calcule=calcul_machine(mt,conf_mt)
    auto_calcule=calcul_automate_q5(conf,automate,True,False,False,True)
    return mt_calcule==auto_calcule

if __name__ == "__main__":
    lec = lecture('Fichier_Texte\Machine_Turing.txt')
    mt = Machine_Turing(lec[1],lec[2],lec[2][0])
    config = Configuration_Machine(lec[0],0,mt.get_etat_initial())
    print(simulation(mt,'001'))
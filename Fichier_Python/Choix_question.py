import sys
import inspect
from Automate_cellulaire import Automate,Configuration_Automate,initialisation,un_pas_automate,calcul_automate_q5,calcul_automate_q6
from Machine_Turing import Machine_Turing,Configuration_Machine,lecture,un_pas_machine,calcul_machine

fonc = sys.argv
mode = fonc[2] if len(fonc) > 2 else None
mot = fonc[3] if len(fonc) > 3 else "10101"
bonus = fonc[4] if len(fonc) > 4 else None

match fonc[1]:
    case "exo0":
        print("Tout")
    case "exo1":
        print(inspect.getsource(Automate))
    case "exo2":
        print(inspect.getsource(Configuration_Automate))
    case "exo3":
        print(inspect.getsource(initialisation))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot {mot}.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            print(config)
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question3 Mode=Exemple" et si vous voulez ' \
            'la tester avec un mot particulier il faut ajouter "Mot=votre_mot" après')
    case "exo4":
        print(inspect.getsource(un_pas_automate))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot 10021.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            print("La configuration avant le pas de calcul")
            print(config,'\n')
            config.set_mot(un_pas_automate(config,auto))
            print("La configuration après le pas de calcul")
            print(config)
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question4 Mode=Exemple" et si vous voulez ' \
            'la tester avec un mot particulier il faut ajouter "Mot=votre_mot" après')
    case "exo5":
        print(inspect.getsource(calcul_automate_q5))
        if mode == "Iteration" or mode == "Transition" or mode == "Succession":
            print(f'\nTest de la fonction pour le mode {mode} :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot {mot}.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            print("La configuration lors de l'initialisation")
            print(config)
            if mode == "Iteration":
                if not bonus or ('1' not in bonus and '2' not in bonus and '3' not in bonus and 
                                 '4' not in bonus and '5' not in bonus and '6' not in bonus and 
                                 '7' not in bonus and '8' not in bonus and '9' not in bonus):
                    bonus = 10
                else:
                    bonus = int(bonus)
                calcul_automate_q5(config,auto,iteration=bonus)
                print(f"\nLa configuration après {bonus} itérations est :")
                print(config)
            elif mode == "Transition":
                bonus = tuple(bonus.split(','))
                if not bonus or (len(bonus)!=3):
                    bonus = list(auto.get_regles().keys())[0]
                resultat = calcul_automate_q5(config,auto,transition_particuliere=bonus)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"La transition {bonus}  apparait au bout de {resultat[1]} itérations")
            else:
                resultat = calcul_automate_q5(config,auto,succession=True)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"La configuration devient stable au bout de {resultat[1]} itérations")

        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question5" et ensuite soit "Mode=Iteration" ' \
            'soit "Mode=Transition" et soit "Mode=Succession".\nEn fonction du mode que vous voulez tester et ensuite il ' \
            'faut rajouter "Mot=votre_mot" et enfin si vous etes en mode Iteration ou Transition il faut ' \
            'rajouter "Iteration=votre_nombre_ou_transition"')
    case "exo6":
        print(inspect.getsource(calcul_automate_q6))
    case "exo7":
        pass
    case "exo8":
        print(inspect.getsource(Machine_Turing))
    case "exo9":
        print(inspect.getsource(Configuration_Machine))
    case "exo10":
        pass
    case "exo11":
        pass
    case "exo12":
        pass
    case "exo13":
        pass
    case "exo14":
        pass
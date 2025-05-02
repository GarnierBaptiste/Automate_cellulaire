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
            print('Pour tester la fonction il faut utiliser la commande "make Question3 Mode=Exemple" et si vous voulez la tester avec un mot particulier il faut ajouter "Mot=votre_mot" après')
    case "exo4":
        print(inspect.getsource(un_pas_automate))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot 10021.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            print("Etape 0")
            print(config)
            config.set_mot(un_pas_automate(config,auto)[0])
            print("Etape 1")
            print(config)
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question4 Mode=Exemple" et si vous voulez la tester avec un mot particulier il faut ajouter "Mot=votre_mot" après')
    case "exo5":
        print(inspect.getsource(calcul_automate_q5))
        if mode == "Iteration" or mode == "Transition" or mode == "Succession":
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            print("Etape 0")
            print(config)
            if mode == "Iteration":
                if not bonus or ('1' not in bonus and '2' not in bonus and '3' not in bonus and '4' not in bonus and '5' not in bonus and '6' not in bonus and '7' not in bonus and '8' not in bonus and '9' not in bonus):
                    bonus = 10
                else:
                    bonus = int(bonus)
                calcul_automate_q5(config,auto,iteration=bonus)
                print("\nLa configuration après le nombre d'itérations demandé est :")
                print(config)
            elif mode == "Transition":
                bonus = tuple(bonus.split(','))
                if not bonus or (len(bonus)!=3):
                    bonus = list(auto.get_regles().keys())[0]
                print(type(bonus))
                resultat = calcul_automate_q5(config,auto,transition_particuliere=bonus)
                if type(resultat) == str:
                    print(resultat)
            else:
                resultat = calcul_automate_q5(config,auto,succession=True)
                print(resultat)

        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question5" et ensuite soit "Mode=Iteration" soit "Mode=Transition" et soit "Mode=Succession" en fonction dumode que vous voulez tester et ensuite il faut rajouter "Mot=votre_mot" et enfin si vous etes en mode iteration ou Transition_Particulière il faut rajouter "Iteration=votre_nombre_ou_transition"')
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
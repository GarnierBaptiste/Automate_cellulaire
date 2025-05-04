import sys,inspect,random
from Automate_cellulaire import Automate,Configuration_Automate,initialisation,un_pas_automate,calcul_automate_q5,calcul_automate_q6
from Machine_Turing import Machine_Turing,Configuration_Machine,lecture,un_pas_machine,calcul_machine
from Simulation import simulation

fonc = sys.argv
mode = fonc[2] if len(fonc) > 2 else None
mot = fonc[3] if len(fonc) > 3 else "10101"
bonus = fonc[4] if len(fonc) > 4 else None

match fonc[1]:
    case "exo0":
        print("Question 1 :")
        print(inspect.getsource(Automate))
        print("Question 2 :")
        print(inspect.getsource(Configuration_Automate))
        print("Question 3 :")
        print(inspect.getsource(initialisation))
        print("Question 4 :")
        print(inspect.getsource(un_pas_automate))
        print("Question 5 :")
        print(inspect.getsource(calcul_automate_q5))
        print("Question 6 :")
        print(inspect.getsource(calcul_automate_q6))
        print("Question 7 :")
        print("Question 8 :")
        print(inspect.getsource(Machine_Turing))
        print("Question 9 :")
        print(inspect.getsource(Configuration_Machine))
        print("Question 10 :")
        print(inspect.getsource(lecture))
        print("Question 11 :")
        print(inspect.getsource(un_pas_machine))
        print("Question 12 :")
        print(inspect.getsource(calcul_machine))
        print("Question 13 :")
        print(inspect.getsource(simulation))
        print("Question 14 :")
        with open('Fichier_Texte/Question14.txt','r') as f:
            mot = '\n'
            for elem in f.readlines():
                mot += elem
            print(mot)
        print("Pour plus d'exemple de test, il faut utiliser les commandes individuelles avec un Mode")
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
                if not bonus or (len(bonus) != 5):
                    bonus = list(auto.get_regles().keys())[0]
                else:
                    bonus = tuple(bonus.split(','))
                resultat = calcul_automate_q5(config,auto,trans_part = bonus)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"La transition {bonus} apparait au bout de {resultat[1]+1} itérations")
            else:
                resultat = calcul_automate_q5(config,auto,succession = True)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"Il y a une succession au bout de {resultat[1]+1} itérations")
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question5" et ensuite soit "Mode=Iteration" ' \
            'soit "Mode=Transition" et soit "Mode=Succession".\nEn fonction du mode que vous voulez tester et ensuite il ' \
            'faut rajouter "Mot=votre_mot" et enfin si vous etes en mode Iteration ou Transition il faut ' \
            'rajouter "Iteration=votre_nombre_ou_transition"')
    case "exo6":
        print(inspect.getsource(calcul_automate_q6))
        if mode == "Iteration" or mode == "Transition" or mode == "Succession":
            print(f'\nTest de la fonction pour le mode {mode} :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot {mot}.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt",mot)
            print(auto)
            if mode == "Iteration":
                if not bonus or ('1' not in bonus and '2' not in bonus and '3' not in bonus and
                                 '4' not in bonus and '5' not in bonus and '6' not in bonus and 
                                 '7' not in bonus and '8' not in bonus and '9' not in bonus):
                        bonus = 10
                else:
                    bonus = int(bonus)
                calcul_automate_q6(config,auto,iteration = bonus)
            elif mode == "Transition":
                if not bonus or (len(bonus) != 5):
                    bonus = list(auto.get_regles().keys())[0]
                else:
                    bonus = tuple(bonus.split(','))
                resultat = calcul_automate_q6(config,auto,trans_part = bonus)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"La transition {bonus}  est utilisé pour passer à l'itération numéro {resultat[1]+1}")
            else:
                resultat = calcul_automate_q6(config,auto,succession = True)
                if type(resultat) == str:
                    print(resultat)
                else:
                    print(f"La configuration a une succession au bout de {resultat[1]+1} itérations")
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question6" et ensuite soit "Mode=Iteration" ' \
            'soit "Mode=Transition" et soit "Mode=Succession".\nEn fonction du mode que vous voulez tester et ensuite il ' \
            'faut rajouter "Mot=votre_mot" et enfin si vous etes en mode Iteration ou Transition il faut ' \
            'rajouter "Iteration=votre_nombre_ou_transition"')
    case "exo7":
        if mode != "Infini" and mode != "Cycle" and mode != "Choix1" and mode != "Choix2":
            print('Pour tester la fonction il faut utiliser la commande "make Question7" et ensuite soit "Mode=Infini" soit ' \
            '"Mode=Cycle" et soit "Mode=Choix1" ou "Mode=Choix2".\n il faut rajouter "Mot=votre_mot" sinon le sera 10101 par défaut')
        else:
            if mode == "Infini":
                mot = '0000000000'
                i = random.randint(0,10)
                mot = mot[:i] + '1' + mot[i+1:]
                auto,config = initialisation("Fichier_Texte/Automate_infini.txt",mot)
                print(auto)
                calcul_automate_q6(config,auto,iteration = 10)
            if mode == "Cycle":
                mot = ''
                for _ in range(23):
                    mot += str(random.randint(0,2))
                    print(mot)
                auto,config = initialisation("Fichier_Texte/Automate_cyclique.txt",mot)
                print(auto,'\n',config)
                print()
                calcul_automate_q6(config,auto,iteration = 10)
            if mode == "Choix1":
                mot = '00000000000000000000000'
                i = random.randint(0,22)
                mot = mot[:i] + '1' + mot[i+1:]
                auto,config = initialisation("Fichier_Texte/Automate_interessant_1.txt",mot)
                print(auto)
                print(config)
                calcul_automate_q6(config,auto,iteration = 10)
            if mode == "Choix2":
                auto,config = initialisation("Fichier_Texte/Automate_interessant_2.txt",'000001100010000')
                print(auto)
                calcul_automate_q6(config,auto,iteration = 10)

    case "exo8":
        print(inspect.getsource(Machine_Turing))
    case "exo9":
        print(inspect.getsource(Configuration_Machine))
    case "exo10":
        print(inspect.getsource(lecture))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles et le mot écrites dans le fichier "Machine_Turing.txt" qui se situe dans le dossier Fichier_Texte.\n')
            mt,config = lecture('Fichier_Texte/Machine_Turing.txt')
            print(mt,"\n\n",config)
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question10 Mode=Exemple"')
    case "exo11":
        print(inspect.getsource(un_pas_machine))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles et le mot écrites dans le fichier "Machine_Turing.txt" qui se situe dans le dossier Fichier_Texte.\n')
            mt,config = lecture('Fichier_Texte/Machine_Turing.txt')
            print(mt,"\n",config)
            un_pas_machine(mt,config)
            print("\nLa configuration après le pas de calcul")
            print(config)
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question11 Mode=Exemple"')
    case "exo12":
        print(inspect.getsource(calcul_machine))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles et le mot écrites dans le fichier "Machine_Turing.txt" qui se situe dans le dossier Fichier_Texte.\n')
            mt, config = lecture('Fichier_Texte/Machine_Turing.txt')
            print(mt,"\n",config)
            resultat = calcul_machine(mt,config)
            if resultat:
                print("La Machine de Turing accepte le mot")
            else:
                print("La Machine de Turing n'accepte pas le mot")
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question12 Mode=Exemple"')

    case "exo13":
        print(inspect.getsource(simulation))
        if mode == "Exemple":
            print(f'\nTest de la fonction :\n   On utilise les règles et le mot écrites dans le fichier "Machine_Turing.txt" qui se situe dans le dossier Fichier_Texte.\n')
            mt, config = lecture('Fichier_Texte/Machine_Turing.txt')
            mot = ''
            for elem in config.get_ruban():
                mot += elem
            print(mt,"\n",config)
            resultat = simulation(mt,config.get_ruban())
            if resultat[2]:
                print(f"Le mot {mot} est accépté par l'Automate Celluaire qui représente la Machine de Turing et on a \n{resultat[0]}\n{resultat[1]}")
            else:
                print(f"Le mot {mot} n'est pas accépté par l'Automate Celluaire qui représente la Machine de Turing")
        else:
            print('Pour tester la fonction il faut utiliser la commande "make Question13 Mode=Exemple"')
    case "exo14":
        with open('Fichier_Texte/Question14.txt','r') as f:
            mot = '\n'
            for elem in f.readlines():
                mot += elem
            print(mot)
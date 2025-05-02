import sys
import inspect
from Automate_cellulaire import Automate,Configuration_Automate,initialisation,un_pas_automate,calcul_automate_q5,calcul_automate_q6
from Machine_Turing import Machine_Turing#,Configuration_Machine,initialisation_machine_turing,un_pas_machine_turing,calcul_machine_turing_q5,calcul_machine_turing_q6

fonc = sys.argv
print(fonc)
match fonc[1]:
    case "exo0":
        print("coucou")
    case "exo1":
        print(inspect.getsource(Automate))
    case "exo2":
        print(inspect.getsource(Configuration_Automate))
    case "exo3":
        print(inspect.getsource(initialisation))
        if len(sys.argv[1:]) > 1:
            mode = fonc[2]
            try :
                mot = fonc[3]
            except:
                mot = "10021"
            print(f'\nTest de la fonction :\n   On utilise les règles écrites dans le fichier "Automate_cellulaire.txt" qui se situe dans le dossier Fichier_Texte et le mot {mot} choisi arbitrairement.\n')
            auto,config = initialisation("Fichier_Texte/Automate_cellulaire.txt","10021")
            print(auto)
    case "exo4":
        print(inspect.getsource(un_pas_automate))
    case "exo5":
        print(inspect.getsource(calcul_automate_q5))
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
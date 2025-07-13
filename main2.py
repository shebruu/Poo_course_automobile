# This is a sample Python script.
from voiture import Voiture
from circuit import Circuit
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Bienvenue')

    v1 = Voiture("Peugeot", "208", 5, 40, 20, 80)
    print(f"Voiture 1 : {v1.marque} {v1.modele} | Vitesse max : {v1.vitesse_max} | Vitesse min : {v1.vitesse_min}")

    v2 = Voiture("Renault", "Clio", 5, 50, 20, 80)
    print(f"Voiture 2 : {v2.marque} {v2.modele} | Vitesse max : {v2.vitesse_max} | Vitesse min : {v2.vitesse_min}")

    c1v1 = Circuit(5, 140)
    print(f"Circuit de la voiture 1 : {c1v1.nb_tour} tours de {c1v1.distance_tour} km")

    # Boucle principale
    while True:
        print("\n--- Nouvelle simulation de course ---")
        vitesse_random = v1.vitesse_aleatoire()
        print("Vitesse tirée au hasard pour la voiture 1 : {:.2f} km/h".format(vitesse_random))

        temps_tour_circuit = c1v1.temps_parcours_circuit(v1)
        print("Temps pour un tour de circuit : {:.2f} minutes".format(temps_tour_circuit))

        temps_total_v1 = c1v1.temps_total(v1)
        print("Somme des temps totaux des tours pour cette voiture : {:.2f} minutes".format(temps_total_v1))

        temps_min = c1v1.temps_total_plus_bas(v1)
        print("Temps total le plus bas pour cette voiture : {:.2f} minutes".format(temps_min))

        # Demande à l'utilisateur s'il veut recommencer
        choix = input("\nAppuyez sur Entrée pour relancer, ou tapez 'q' pour quitter : ").strip().lower()
        if choix == 'q':
            print("Fin de la simulation.")
            break
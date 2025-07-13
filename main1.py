from voiture import Voiture
from circuit import Circuit
import time
import os

def print_hi(name):
    print(f'Hi, {name}')

def afficher_piste(longueur, position):
    """Affiche une piste avec la voiture positionnée dessus."""
    piste = ['_'] * longueur
    idx = min(longueur-1, max(0, int(position)))
    piste[idx] = '🚗'
    print('|' + ''.join(piste) + '|')

if __name__ == '__main__':
    print_hi('Bienvenue sur le Circuit !')

    v1 = Voiture("Peugeot", "208", 5, 40, 20, 80)
    v2 = Voiture("Renault", "Clio", 5, 50, 20, 80)

    c1 = Circuit(5, 140)
    print(f"\n--- COURSE SUR {c1.nb_tour} TOURS DE {c1.distance_tour} km ---")
    print(f"Voiture 1 : {v1.marque} {v1.modele}")
    print(f"Voiture 2 : {v2.marque} {v2.modele}")

    while True:
        print("\n==== NOUVELLE COURSE ====\n")
        for tour in range(1, c1.nb_tour + 1):
            # Génère une vitesse aléatoire pour chaque voiture ce tour
            vitesse1 = v1.vitesse_aleatoire()
            vitesse2 = v2.vitesse_aleatoire()

            # Calcule la position sur une piste de 40 caractères
            piste_longueur = 40
            pos1 = (vitesse1 - v1.vitesse_min) / (v1.vitesse_max - v1.vitesse_min) * (piste_longueur - 1)
            pos2 = (vitesse2 - v2.vitesse_min) / (v2.vitesse_max - v2.vitesse_min) * (piste_longueur - 1)

            print(f"\nTour {tour} / {c1.nb_tour}")
            print(f"Peugeot 208  | Vitesse : {vitesse1:.1f} km/h")
            afficher_piste(piste_longueur, pos1)
            print(f"Renault Clio | Vitesse : {vitesse2:.1f} km/h")
            afficher_piste(piste_longueur, pos2)
            time.sleep(1)  # Effet dynamique (peux retirer si tu veux)

        # Calculs finaux
        temps_total_v1 = c1.temps_total(v1)
        temps_total_v2 = c1.temps_total(v2)
        temps_min1 = c1.temps_total_plus_bas(v1)
        temps_min2 = c1.temps_total_plus_bas(v2)

        print("\n===== RÉSULTATS =====")
        print(f"Total Peugeot 208  : {temps_total_v1:.1f} minutes (meilleur possible : {temps_min1:.1f})")
        print(f"Total Renault Clio : {temps_total_v2:.1f} minutes (meilleur possible : {temps_min2:.1f})")

        choix = input("\nAppuyez sur Entrée pour refaire la course, ou tapez 'q' pour quitter : ").strip().lower()
        if choix == 'q':
            print("Merci d'avoir joué !")
            break
        os.system('cls' if os.name == 'nt' else 'clear')  # Efface l'écran entre chaque course


import random
from voiture import Voiture
# class Circuit(Voiture):
class Circuit:


    def __init__(self,nb_tour, distance_tour_km):
        # super().__init__(marque,modele,nbtour=None,distance_tour_km=None,vitesse_min=None,vitesse_max=None)
        self._nb_tour=nbtour
        self._distance_tour_km=distance_tour_km

    def trouver_distance(self, voiture)
    temps_tour_circuit_h=_distance_tour_km/vitesse_voiture_tour
    _somme_total_temps=(temps_tour_circuit_h*60)*_nb_tour

    def trouver_vitesse_random(self,voiture):
        return random.uniform(voiture._vitesse_min,voiture._vitesse_max)

    def trouver_temps_tour_circuit_h(self,voiture):
        return voiture._distance_tour_km/trouver_vitesse_random(voiture)

    
v1=Voiture("Peugot","208",5,40,20,80)
print(f"Marque : {v1.marque}")

v2= Voiture("renault","clio",5,50,20,80)



c1v1=Circuit(5)

vitesse_voiture_tour=trouver_vitesse_random(v1)
print("vitesse voiture tour : ",vitesse_voiture_tour)

temps_tour_circuit_h=trouver_temps_tour_circuit_h(v1)
print("temps  en heure pour un tour de circuit")
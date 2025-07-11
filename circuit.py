
import random
from voiture import Voiture
# class Circuit(Voiture):
def vitesse_rand(voiture):
    """ Génere une vitesse aléatoire de voiture a partir de  sa vitesse minimal et maximal  """
    return random.uniform(voiture.vitesse_min, voiture.vitesse_max)


class Circuit:


    def __init__(self,nb_tour, distance_tour=5):
        # super().__init__(marque,modele,nbtour=None,distance_tour_km=None,vitesse_min=None,vitesse_max=None)
        self._nb_tour=nb_tour
        self._distance_tour =distance_tour

    @property
    def nb_tour(self):
        return self._nb_tour

    @property
    def distance_tour_km(self):
         return self._distance_tour

    @property
    def distance_tour(self):
        return self._distance_tour
    @distance_tour.setter
    def distance_tour(self,value):
         self._distance_tour=value

    def temps_parcours_circuit(self, voiture):

        vitesse= vitesse_rand(voiture)
        temps_heure=self.distance_tour/vitesse
        return temps_heure * 60


    def temps_total(self, voiture):

        somme_temps_total= self.temps_parcours_circuit(voiture)
        return somme_temps_total  * self.nb_tour


v1=Voiture("Peugot","208",5,40,20,80)
print(f"Marque : {v1.marque}")

v2= Voiture("renault","clio",5,50,20,80)



c1v1=Circuit(5,140)

vitesse_random=vitesse_rand(v1)
print("vitesse voiture tour : ",vitesse_random)



#
# temps_tour_circuit=temps_parcours_circuit(v1)
# print("temps  en heure pour un tour de circuit",temps_tour_circuit)




temps_total= temps_total(v1)
print("Somme des Temps totaux des tours de cette voiture : ",temps_total)
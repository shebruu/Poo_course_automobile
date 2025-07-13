import random
from voiture import Voiture
""" 
def vitesse_rand(voiture):
    return random.uniform(voiture.vitesse_min, voiture.vitesse_max)
# appel : vitesse_random=vitesse_rand(v1)

"""
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
    """ 
    @staticmethod
    def vitesse_rand(voiture):
    
        Génère une vitesse aléatoire comprise entre la vitesse minimale et maximale de la voiture.

        Args:
            voiture (Voiture): Instance de la classe Voiture, contenant les attributs 'vitesse_min' et 'vitesse_max'.

        Returns:
            float: Vitesse aléatoire (en km/h) tirée entre la vitesse minimale et maximale de la voiture.

        return random.uniform(voiture.vitesse_min, voiture.vitesse_max)
        Apel : vitesse_random=Circuit.vitesse_rand(v1)
        ds un polymorphisme :     vitesse= vitesse_rand(voiture)
"""
    def temps_parcours_circuit(self, voiture):
        """
        Calcule le temps nécessaire (en minutes) pour effectuer un tour de circuit avec une vitesse aléatoire.

        À chaque appel, la vitesse de la voiture est tirée au hasard entre ses bornes, simulant la variabilité réelle.

        Args:
            voiture (Voiture): Instance de la classe Voiture.

        Returns:
            float: Temps mis pour parcourir un tour (en minutes) avec la vitesse aléatoire obtenue.
        """
        vitesse= voiture.vitesse_rand
        temps_heure=self.distance_tour/vitesse
        return temps_heure * 60


    def temps_total(self, voiture):
        """
        Calcule le temps total (en minutes) pour effectuer tous les tours du circuit,
        en tirant une nouvelle vitesse aléatoire à chaque tour.

        Args:
            voiture (Voiture): Instance de la classe Voiture.

        Returns:
            float: Temps total (en minutes) pour l'ensemble des tours, chaque tour ayant sa propre vitesse.
        """
        temps_total = 0
        for _ in range(self.nb_tour):
            temps_total += self.temps_parcours_circuit(voiture)
        return temps_total

    def temps_total_plus_bas(self,voiture):
        """
        Calcule le temps total minimal possible (en minutes) pour tous les tours du circuit,
        c'est-à-dire si la voiture roule à sa vitesse maximale durant toute la course.

        Args:
            voiture (Voiture): Instance de la classe Voiture.

        Returns:
            float: Temps total minimal théorique (en minutes) pour l'ensemble des tours, à vitesse maximale.
        """
        temps_tour = self.distance_tour / voiture.vitesse_max  # temps en heures
        temps_tour_minutes = temps_tour * 60
        temps_total_min = temps_tour_minutes * self.nb_tour
        return temps_total_min


v1=Voiture("Peugot","208",5,40,20,80)
print(f"Voiture 1 :  : {v1.marque} {v1.modele} | Vitesse max :  {v1.vitesse_max} Vitesse min :{v1.vitesse_min}")

v2= Voiture("renault","clio",5,50,20,80)
print(f"Voiture 2 :  : {v2.marque} {v2.modele} | Vitesse max :  {v2.vitesse_max} Vitesse min :{v2.vitesse_min} ")


c1v1=Circuit(5,140)
print(f"Circuit de la voiture 1 :  {c1v1.nb_tour} ")

# Exemple : vitesse aléatoire d’un tour
vitesse_random=v1.vitesse_rand()
print("vitesse voiture 1 pour un  tour : {:.2f} km/h".format(vitesse_random))



# Temps pour un tour
temps_tour_circuit = c1v1.temps_parcours_circuit(v1)
print("Temps pour un tour de circuit : {:.2f} minutes ".format(temps_tour_circuit))


# Temps total pour tous les tours (appel CORRECT de la méthode sur l’instance)
temps_total_v1 = c1v1.temps_total(v1)
print("Somme des temps totaux  des tours pour cette voiture : {:.2f} minutes".format(temps_total_v1))


# Calcul du temps minimal possible pour v1 sur c1v1
temps_min = c1v1.temps_total_plus_bas(v1)
print("Temps total le plus bas  pour cette voiture : {:.2f} minutes".format(temps_min))

import random
class Voiture:
    def __init__(self,marque,modele,nbtour=None,distance_tour_km=None,vitesse_min=None,vitesse_max=None):
        self._marque=marque
        self._modele=modele
        self._nbtour=nbtour
        self._distance_tour_km=distance_tour_km
        self._vitesse_min=vitesse_min
        self._vitesse_max=vitesse_max

    def __str__(self):
        return f"{self.__class__.__name__} : {self.marque}, {self.modele}  "

    @property
    def marque(self):
        return self._marque

    @property
    def modele(self):
        return self._modele
    @property
    def vitesse_min(self):
        return self._vitesse_min

    @property
    def vitesse_max(self):
        return self._vitesse_max


    @vitesse_max.setter
    def vitesse_max(self,value):
         self._vitesse_max=value

    @vitesse_min.setter
    def vitesse_min(self, value):
        self._vitesse_min = value

    def vitesse_aleatoire(self):
        """
        Génère une vitesse aléatoire comprise entre la vitesse minimale et maximale de CETTE voiture.

        Returns:
            float: Vitesse aléatoire (en km/h) tirée entre la vitesse minimale et maximale de cette voiture.
        """
        return random.uniform(self.vitesse_min, self.vitesse_max)
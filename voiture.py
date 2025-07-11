class Voiture:
    def __init__(self,marque,modele):
        self._marque=marque
        self._modele=modele
        self._nbtour=0
        self._distance_tour_km=0
        self._vitesse_min=0
        self._vitesse_max=0

    def __str__(self):
        return f"{self.__class__.__name__} : {self.marque}, {self.modele}  "

    @property
    def marque(self):
        return self._marque

    @property
    def modele(self):
        return self._modele


v1=Voiture("Peugot",208)
print(f"Marque : {v1.marque}")

bmax=v1._vitesse_max=50
print(bmax)

# vm_v1=v1._vitesse_max=80
# print(f"{vm_v1}")

"""
    def __init__(self,marque, marque,vitesse_minimal,vitesse_maximale):
        self._marque=marque
        self._modele=modele
        self._vitesse_min=vitesse_min
        self._vitesse_max=vitesse_maximale
"""




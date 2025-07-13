1. . Calcul de la vitesse d’un tour (vitesse aléatoire)
    But : Simuler la vitesse réelle, différente à chaque tour.

    Formule :
    vitesse_tour = random.uniform(vitesse_min, vitesse_max)
Appel :vitesse_random = Circuit.vitesse_rand(v1)
vitesse_rand est une méthode @staticmethod.
➔ Elle n'utilise pas de données spécifiques à un objet Circuit (self).
➔ On peut donc l’appeler directement sur la classe (Circuit.vitesse_rand()), sans créer un objet Circuit.

si methode definie ds l autre classe : appeler sur  objet de cette autre classe 
vitesse = v1.vitesse_aleatoire()

2. Calcul du temps pour un tour

    But : Savoir combien de temps met la voiture pour un seul tour, à une certaine vitesse.
    analyser la preformance tou a tour 
    Formule :
    temps_heure = distance_tour / vitesse_tour
    temps_minutes = temps_heure * 60
temps_tour_circuit = c1v1.temps_parcours_circuit(v1)
temps_parcours_circuit utilise les données du circuit (nombre de tours, distance du tour…) stockées dans l’objet c1v1.
➔ On doit  appeler cette méthode sur l’objet Circuit créé (c1v1).

   3. Calcul du temps total pour tous les tours (simulation réaliste)
       But : Obtenir le temps total réel sur le circuit, avec vitesse différente à chaque tour.
        Estimer la durée  réelle d' une course 
   Algorithme : 
   temps_total = 0
    pour chaque tour:
       tirer une vitesse aléatoire
       calculer temps pour ce tour
       ajouter au temps_total

    Formule : 
    temps_total = somme(temps_minutes_pour_chaque_tour)


4. Calcul du temps total le plus bas (record théorique)
    But : Trouver le meilleur temps possible (si la voiture va à sa vitesse max tout le temps).

    Vitesse minimale : donnerait le temps le plus long possible.
    Vitesse aléatoire : simule la vraie vie, avec des variations,  ne donne ni le record ni le pire.
    Vitesse maximale : représente la performance idéale et le “record du circuit”    

    Formule :
    temps_tour_h = distance_tour / vitesse_max
    temps_tour_minutes = temps_tour * 60
    temps_total_min = temps_tour_min * nb_tour


   5. Calcul du temps total le plus haut (le perdant)
But : Trouver le pire temps possible (si la voiture va à sa vitesse min tout le temps).

Formule :
temps_tour_max = distance_tour / vitesse_min
temps_total_max = temps_tour_max * 60 * nb_tour

exemple 
pour chaque tour:
    vitesse = random entre vitesse_min et vitesse_max
    temps_tour = (distance_tour / vitesse) * 60
    additionner au temps_total

temps_min_possible = ((distance_tour / vitesse_max) * 60) * nb_tour
temps_max_possible = ((distance_tour / vitesse_min) * 60) * nb_tour


| Cas                                      | Doit utiliser | Exemple d’appel                   |
| ---------------------------------------- | :-----------: | :-------------------------------- |
| **Méthode statique** (@staticmethod)     |   La Classe   | Circuit.vitesse\_rand(v1)         |
| **Méthode d’instance** (self, sur objet) |    L’objet    | c1v1.temps\_parcours\_circuit(v1) |
| **Méthode de Voiture** (self)            |    L’objet    | v1.vitesse\_aleatoire()           |


| Type de méthode        | Mot-clé/décorateur | 1er paramètre | Comment on l’appelle                                                    | Rôle / Quand l’utiliser ?                                                                                | Accès aux données ?                |
| ---------------------- | ------------------ | :-----------: | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| **Méthode d’instance** | *(aucun)*          |     `self`    | Sur un **objet** (`objet.methode()`)                                    | Pour travailler ou modifier **les attributs propres à chaque objet** (ex : position d’une voiture)       | Attributs et méthodes de l’objet   |
| **Méthode de classe**  | `@classmethod`     |     `cls`     | Sur la **classe** (`Classe.methode()`)                                  | Pour travailler sur **la classe dans son ensemble** (ex : créer des objets d’une manière spéciale)       | Attributs et méthodes de la classe |
| **Méthode statique**   | `@staticmethod`    |   *(aucun)*   | Sur la **classe ou un objet** (`Classe.methode()` ou `objet.methode()`) | Pour des **fonctions utilitaires** : liées logiquement à la classe, mais qui n’utilisent pas ses données | Rien : n’accède ni à self ni à cls |


Méthode d’instance :
Fonction qui agit sur un objet spécifique (par exemple, une voiture particulière). Elle peut lire ou modifier les attributs de cet objet. Elle est définie normalement sans décorateur.
Exemple d’appel : voiture1.demarrer()

Méthode de classe :
Fonction qui agit sur la classe elle-même (par exemple, compter le nombre total de voitures créées, ou fournir une “fabrique” d’objets). On la reconnaît à son décorateur @classmethod et au premier paramètre nommé cls.
Exemple d’appel : Voiture.creer_sportive()

Méthode statique :
Fonction utilitaire logiquement liée à la classe, mais qui n’utilise pas les données de la classe ou d’un objet (ni self ni cls). On la définit avec le décorateur @staticmethod.
Exemple d’appel : Voiture.calculer_taxe(chevaux)

quand ? 
Utilise une méthode d’instance pour manipuler des données d’un objet particulier.

Utilise une méthode de classe si ton code doit agir sur la classe entière ou fournir des “constructeurs alternatifs”.

Utilise une méthode statique pour des outils mathématiques, de validation ou de transformation qui ne dépendent ni d’un objet, ni de la classe.


Convention de visibilité
| Visibilité  | Syntaxe      | Accès                                                            | Utilisation / Convention                                             |
| ----------- | ------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Public**  | `variable`   | Partout (aucune restriction)                                     | Attribut accessible librement : usage normal                         |
| **Protégé** | `_variable`  | Par convention : interne à la classe et ses sous-classes         | Indique qu’on ne doit pas y accéder “directement” depuis l’extérieur |
| **Privé**   | `__variable` | Name mangling : accessible uniquement à l’intérieur de la classe | Pour cacher l’attribut, éviter les conflits avec les sous-classes    |


Pourquoi définir les attributs dans le constructeur (__init__) ?
tous les attributs qui définissent l’état de l’objet devraient être initialisés dans __init__
    Assure l’initialisation des données propres à chaque objet dès sa création.

    Permet d’appliquer la protection (public/protégé/privé) directement à l’attribut.

    Organise le code et rend les objets “prêts à l’emploi” avec leurs valeurs par défaut ou reçues en paramètre.

    Garantit la cohérence : chaque objet a bien ses attributs définis, ce qui réduit le risque de bug lors de l’utilisation.


exemple 
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque        # public
        self._vitesse = 0           # protégé (par convention)
        self.__num_serie = 123456   # privé (vraiment interne à la classe)

class Voiture:
    def __init__(self, marque, modele="Clio"):
        self.marque = marque
        self.modele = modele
class Voiture:
    def __init__(self, marque, modele=None):
        self.marque = marque
        self.modele = modele if modele is not None else "Clio"
        self._vitesse = 0  publique 
        self.__num_serie = 123456   protégée 

(@property) implémentable pour tous les attributs initialisés dans le constructeur, qu’ils soient publics, protégés (_attribut), ou privés (__attribut).
permet de : contrôler/modifier l’accès à un attribut,

ajouter de la validation,

rendre certains attributs “lecture seule”,

ou garder la possibilité de changer l’implémentation interne plus tard.


acces 
| Type d’attribut  | Exemple de déclaration | Appel possible en dehors de la classe ? | Syntaxe d’accès hors classe  | Meilleure pratique recommandée                |
| ---------------- | ---------------------- | :-------------------------------------: | ---------------------------- | --------------------------------------------- |
| **Public**       | `self.attribut`        |                   Oui                   | `objet.attribut`             | Accès direct autorisé                         |
| **Protégé (\_)** | `self._attribut`       |    Oui (mais à éviter, sauf héritage)   | `objet._attribut`            | Accès direct déconseillé : préférer propriété |
| **Privé (\_\_)** | `self.__attribut`      |           Non (name mangling)           | `objet._NomClasse__attribut` | À éviter : exposer par propriété              |
| **Propriété**    | via `@property`        |                   Oui                   | `objet.nom_propriété`        | Recommandé pour lecture/écriture contrôlée    |

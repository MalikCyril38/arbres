    #classe
class Animal:
    def __init__(self, name, weight, size):
        self.name = name
        self.set_weight(weight)
        self.size = size
    
    #Operator overloading --> pour retourner de façon explicite l'objet Animal
    def __str__(self):
        return f'Ce {self.name} a un poids de {self.get_weight()} kg et une taille de {self.size} cm'
 

    #Ajouter une Méthode qui ne fait rien pour le moment
    def se_deplacer(self):
        pass   
    #Encapsulation
    def get_weight(self):
        return self.__weight   

    def get_name(self):
        return self.name
        
    def set_weight(self, new_weight):
        if not(isinstance(new_weight, int) or isinstance(new_weight, float)):
            raise TypeError("weight must be an interger or a float")
        if not (new_weight > 0):
            raise ValueError('weight doit être un nombre positif')
        
        self.__weight = new_weight
        
    #polymorphisme --> redéfinir une méthode propre à chacune des classes enfants
class Serpent(Animal):
    def se_deplacer(self):
        print('je rampe')

class Oiseau(Animal):
    def se_deplacer(self):
        print('je vole')

    #Mot clé super --> étendre une règle aux classes enfants qui hérite d'une autre classe

    def __init__(self, name, weight, size, altitude_max):
        super().__init__(name, weight, size)
        self.altitude_max = altitude_max


    

if __name__=="__main__":

    #attributs et #héritage 
    serpent = Serpent (name = 'serpent', weight = 1, size = 1)
    oiseau = Oiseau (name = 'oiseau', weight = 0.5, size = 0.5, altitude_max=600)

    #polymorphisme
    oiseau.se_deplacer()

    #Mot clé super --> étendre une règle aux classes enfants qui hérite d'une autre classe
    oiseau = Oiseau (name = 'oiseau', weight = 0.5, size = 0.5, altitude_max=600)

    print(oiseau)
    print(f"l'animal est {oiseau.name} et vole a une hauteur de {oiseau.altitude_max}")

    print(f"l'animal est {oiseau.get_name()} et vole a une hauteur de {oiseau.altitude_max}")
   
    print(oiseau.set_weight(-8))
    print(oiseau.set_weight('rtttgrgt'))
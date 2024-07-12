from Animal import Animal, Oiseau, Serpent

class Zoo:
    def __init__(self, animaux):
        self.liste_animaux = []
        for animal in animaux:
            self.ajout_animal(animal)
        

    def ajout_animal(self, animal):
        if isinstance(animal, Animal):
            self.liste_animaux.append(animal)
        else:
            raise TypeError('animal must be an Animal')

    def __add__(self, other_zoo):
        return Zoo(self.liste_animaux + other_zoo.liste_animaux)


# def __init__(self, animaux):
#         self.liste_animaux = animaux
#        



if __name__ == "__main__":
    
    pie = Oiseau(name = 'pie', weight = 0.8, size=0.35, altitude_max=500)
    ours = Animal(name ='ours', weight = 1000, size = 1.90)
    vipère = Serpent(name = 'nina', weight = 0.5, size = 1)
    chien = Animal(name = 'Beauceron', weight = 80, size = 0.5)
    
    zoo1 = Zoo([pie, ours])
    zoo2 = Zoo([chien, vipère])

    zoo3 = zoo1 + zoo2

for animal in zoo3.liste_animaux:
    print(animal)

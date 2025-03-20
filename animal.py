class Animal:
    def __init__(self, name, group, number_of_legs, skills):
  
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills


    def __str__(self):
        return f"Name: {self.name}, Group: {self.group}, Legs: {self.number_of_legs}, Skills: {', '.join(self.skills)}"


axolotl = Animal("Axolotl", "Amphibians", 4, ["regenerating limbs", "swimming", "breathing through skin"])
quokka = Animal("Quokka", "Mammals", 4, ["smiling", "jumping", "foraging"])
kakapo = Animal("Kakapo", "Birds", 2, ["climbing", "parrot-like mimicry", "nocturnal behavior"])
dung_beetle = Animal("Dung Beetle", "Insects", 6, ["rolling dung", "navigating using stars", "burrowing"])
saola = Animal("Saola", "Mammals", 4, ["camouflage", "speed", "elusive behavior"])

animals = [axolotl, quokka, kakapo, dung_beetle, saola]
for animal in animals:
    print(animal)

class Animal():
    def __init__(self, animal_type, name, age, weight, meat_type, vaccination):
        self.animal_type = animal_type.title()
        self.name = name.title()
        self.age = age                  #years
        self.weight = weight            #kilograms
        self.meat_type = meat_type.lower()
        self.have_wool = 0              #имеет ли ценность шерсть животного (0 или 1)
        self.have_milk = 0              #дает ли животное молоко
        self.vaccination = vaccination  #делали ли животному прививку

    def make_vaccination():
        """сделать прививку"""

    def derive_to_pasture():
        """вывести на пастбище"""

    def feed():
        """покормить"""

    def slaughter():
        """забить"""

    def derive_to_stall():
        """отвести в стойло"""

    def get_description(self):
        print(f"{self.animal_type} по имени {self.name}\nВес: {self.weight} кг\nВозраст {self.age} лет\nТип мяса: {self.meat_type}")
        if self.vaccination: print('Прививка сделана.')
        else: print('Прививка не сделана.')
        if self.have_wool: print('Дает шерсть.\n')
        else: print('Не дает шерсть.\n')

class Bird():
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        self.bird_type = bird_type.title()
        self.name = name.title()
        self.age = age
        self.weight = weight
        self.meat_type = meat_type.lower()
        self.egg_type = egg_type         #съедобны ли яйца (бинарная переменная)
        self.vaccination = vaccination

    def get_description(self):
        print(f"{self.bird_type} по имени {self.name}\nВес: {self.weight} кг\nВозраст {self.age} лет\nТип мяса: {self.meat_type}")
        if self.vaccination: print('Прививка сделана.')
        else: print('Прививка не сделана.')
        if self.egg_type: print('Яйца съедобны.\n')
        else: print('Яйца несъедобны.\n')



class Cow(Animal):
    def __init__(self, animal_type, name, age, weight, meat_type, vaccination):
        self.have_milk = 1
        super().__init__(animal_type, name, age, weight, meat_type, vaccination)
    
    def get_milk():
        """Подоить корову"""

class Goat(Animal):
    def __init__(self, animal_type, name, age, weight, meat_type, vaccination):
        self.have_milk = 1
        super().__init__(animal_type, name, age, weight, meat_type, vaccination)

    def get_milk():
        """Подоить козу"""

class Sheep(Animal):
    def __init__(self, animal_type, name, age, weight, meat_type, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, vaccination)
        self.have_wool = 1
    
    def shear():
        """Постричь овцу"""

class Pig(Animal):
    def __init__(self, animal_type, name, age, weight, meat_type, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, vaccination)

class Duck(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)

class Chicken(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)

class Goose(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)

"""Экземпляры классов"""

cow_manka = Cow('корова', 'манька', 5, 600, 'говядина', 1)
cow_manka.get_description()

pig_eldar = Pig('свинья', 'Эльдар', 2, 300, 'свинина', 1)
pig_eldar.get_description()

sheep_dolly = Sheep('овца', 'Долли', 4, 100, 'баранина', 0)
sheep_dolly.get_description()

goat_danila = Goat('козел', 'Данила', 5, 150, 'козлятина', 0)
goat_danila.get_description()

duck_richard = Duck('утка', 'ричард', 2, 5, 'мясо утки', 0, 0)
duck_richard.get_description()

chicken_rosa = Chicken('курица', 'роза', 1, 2, 'курятина', 1, 1)
chicken_rosa.get_description()

goose_don = Goose('гусь', 'дон', 2, 4, 'гусятина', 0, 1)
goose_don.get_description()

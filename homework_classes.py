class Animal():
    def __init__(self, name, age, weight, meat_type, vaccination):
        self.name = name.title()
        self.age = age                  #years
        self.weight = weight            #kilograms
        self.meat_type = meat_type.lower()
        self.vaccination = vaccination  #делали ли животному прививку
        

class Mammal(Animal):
    def __init__(self, animal_type, name, age, weight, meat_type, have_wool, vaccination):
        super().__init__(name, age, weight, meat_type, vaccination)
        self.animal_type = animal_type
        self.have_wool = have_wool
    
    def get_description(self):
        print(f"{self.animal_type.title()} по имени {self.name.title()}\nВес: {self.weight}\
        кг\nВозраст {self.age} лет\nТип мяса: {self.meat_type}")
        if self.vaccination: print('Прививка сделана.')
        else: print('Прививка не сделана.')
        if self.have_wool: print('Дает шерсть.\n')
        else: print('Не дает шерсть.\n')
        
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


class Bird(Animal):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        self.bird_type = bird_type.title()
        self.egg_type = egg_type #съедобны ли яйца (бинарная переменная)
        super().__init__(name, age, weight, meat_type, vaccination)

       
    def get_description(self):
        print(f"{self.bird_type.title()} по имени {self.name.title()}\nВес: {self.weight} кг\nВозраст\
        {self.age} лет\nТип мяса: {self.meat_type}")
        if self.vaccination: print('Прививка сделана.')
        else: print('Прививка не сделана.')
        if self.egg_type: print('Яйца съедобны.\n')
        else: print('Яйца несъедобны.\n')


class Cow(Mammal):
    def __init__(self, animal_type, name, age, weight, meat_type, have_wool, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, have_wool, vaccination)
        self.voice = 'мууу'
    
    def get_milk():
        """Подоить корову"""


class Goat(Mammal):
    def __init__(self, animal_type, name, age, weight, meat_type, have_wool, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, have_wool, vaccination)
        self.voice = 'бэээ'

    def get_milk():
        """Подоить козу"""


class Sheep(Mammal):
    def __init__(self, animal_type, name, age, weight, meat_type, have_wool, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, have_wool, vaccination)
        self.have_wool = 1
        self.voice = 'бэээ'

    def shear():
        """Постричь овцу"""


class Pig(Mammal):
    def __init__(self, animal_type, name, age, weight, meat_type, have_wool, vaccination):
        super().__init__(animal_type, name, age, weight, meat_type, have_wool, vaccination)
        self.voice = 'хрююю'
        


class Duck(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)
        self.voice = 'кря-кря'


class Chicken(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)
        self.voice = 'кококо'


class Goose(Bird):
    def __init__(self, bird_type, name, age, weight, meat_type, egg_type, vaccination):
        super().__init__(bird_type, name, age, weight, meat_type, egg_type, vaccination)
        self.voice = 'гагага'

"""Экземпляры классов"""

cow_manka = Cow('корова', 'манька', 5, 600, 'говядина', 0, 1)
print(cow_manka.voice)
cow_manka.get_description()


pig_eldar = Pig('свинья', 'Эльдар', 2, 300, 'свинина', 0, 1)
print(pig_eldar.voice)
pig_eldar.get_description()

sheep_dolly = Sheep('овца', 'Долли', 4, 100, 'баранина', 0, 0,)
print(sheep_dolly.voice)
sheep_dolly.get_description()

goat_danila = Goat('козел', 'Данила', 5, 150, 'козлятина', 0, 0)
print(goat_danila.voice)
goat_danila.get_description()

duck_richard = Duck('утка', 'ричард', 2, 5, 'мясо утки', 0, 0)
print(duck_richard.voice)
duck_richard.get_description()

chicken_rosa = Chicken('курица', 'роза', 1, 2, 'курятина', 1, 1)
print(chicken_rosa.voice)
chicken_rosa.get_description()

goose_don = Goose('гусь', 'дон', 2, 4, 'гусятина', 0, 1)
print(goose_don.voice)
goose_don.get_description()


class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность по умолчанию
        self.name = name


class Mammal(Animal):
    pass  # Наследует eat от Animal


class Predator(Animal):
    pass  # Наследует eat от Animal


class Flower(Plant):
    pass  # Наследует от Plant, съедобность по умолчанию False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем на съедобное


# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов и выполнение действий
print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False

a1.eat(p1)  # Вывод: Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)  # Вывод: Хатико съел Заводной апельсин

print(a1.alive)  # Вывод: False (погиб)
print(a2.fed)    # Вывод: True (насытился)
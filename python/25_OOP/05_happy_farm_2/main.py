class Garden_man:
    count_ripe = 0

    def __init__(self, name, my_garden):
        self.name = name
        self.my_garden = my_garden

    def my_garden_grow(self):
        print('Садовник Ухаживает за грядкой')
        self.my_garden.grow_all()
        self.my_garden.are_all_ripe()

    def ripe(self):
        if all([i_potate.is_ripe() for i_potate in self.my_garden.potatoes]):
            self.count_ripe += 1
            self.my_garden.new_garden()
            print(f'Картошка созрела, уражай собран\n'
                  f'Кол-во собранных урожаев: {self.count_ripe}')
        else:
            print('Собирать пока рано')


class Potato:
    states = {0: 'отсутствует', 1: 'росток', 2: 'зеленая', 3: 'зрелая'}

    def __init__(self, index):
        self.index = index
        self.states = 0

    def grow(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def regrow(self):
        self.states = 0

    def is_ripe(self):
        if self.states == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.states]}')


class Garden_potates:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает')
        for i_potate in self.potatoes:
            i_potate.grow()

    def new_garden(self):
        for i_potate in self.potatoes:
            i_potate.regrow()

    def are_all_ripe(self):
        if not all([i_potate.is_ripe() for i_potate in self.potatoes]):
            print('Картошка еще не созрела\n')
        else:
            print('Картошка созрела\n')


my_garden = Garden_potates(5)
gardenman = Garden_man('Den', my_garden)
gardenman.my_garden_grow()
gardenman.ripe()
gardenman.my_garden_grow()
gardenman.my_garden_grow()
gardenman.ripe()
my_garden = Garden_potates(5)
gardenman.my_garden_grow()
gardenman.my_garden_grow()
gardenman.my_garden_grow()
gardenman.ripe()

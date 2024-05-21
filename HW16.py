class House:

    def __init__(self):
        self.size = '120 м^2'
        self.price = '5 500 000'
        self.numberOfFloors = 10

    def clear(self):
        print('Дом полностью убран!')

    def floor(self, item):
        print('Текущий этаж', item)


my_home = House()
my_home.clear()
print(my_home.size)
a = 0
while a < my_home.numberOfFloors:
    a = a + 1
    my_home.floor(a)

from random import choice
class Building:
    total=0
    names = ['cottege', 'skyscraper', 'villa', 'hut', 'townhouse', 'chalet',]

    def __init__(self):
        Building.total+=1
        self.name = choice(Building.names)

    def __str__(self):
        return 'Building ' + self.name

objects = []
numberofobjects = 40
while len(objects)<numberofobjects:
    new_object = Building()
    objects.append(new_object)
    print(new_object)

print('Количество объектов -', Building.total)


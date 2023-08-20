class parent:
    color = "blue"
    name = "Hussein"

    def __init__(self):
        self.len = 100
        self.address = 'Palestine , Gaza strip'

    @classmethod
    def get_color(cls):
        print(f'Parent  color is : {cls.color}')

    def get_len(self):
        print(f'Parent  len is : {self.len}')


parent1 = parent()
print(parent1.len)
parent1.get_len()


class child(parent):
    def __init__(self):
        super().__init__()
        self.city = 'Gaza'
        self.len = 180

    def Get_city(self):
        print(f'child  len is : {self.city}')

    # def get_len(self):
    #     print(f' child  len is : {self.len}')


child1 = child()
print(child1.city)
print(child1.len)
print(child1.get_len())

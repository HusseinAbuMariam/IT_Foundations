
class Member:
    num_me = 0

    def __init__(self, name, age, city):
        print("hello")
        self.name = name
        self.age = age
        self.city = city
        Member.num_me += 1
        
    def eat(self):
        print("member is eating")

    @classmethod
    def calc_avg_age(cls):
        print(" Avg of all members is : 65")
        print(cls.num_me)


m1 = Member('moh', 20, 'Gaza')
m1.eat()
print(m1.name)
print(m1.age)
print(m1.city)
m2 = Member('hussein', 19, 'Gaza')
print(m2.name)
print(m2.age)
print(m2.city)
print(Member.num_me)
print(Member.calc_avg_age())

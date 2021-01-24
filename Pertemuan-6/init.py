class Person:

    def __init__(self,name,age,nama_lawan):
        self.name = name
        self.age = age
        self.nama_lawan = nama_lawan

    def sapa(self):
        print("Hallo namaku " + self.name)
        print("Nama kamu siapa?")

    def salamKenal(self):
        print("salam kenal " + self.nama_lawan)
        print("Senang bertemu denganmu")

p1 = Person("Nafi",22,"Dodit")
p1.sapa()
p1.salamKenal()


# p1 = Person("Nafi", 22)
# p2 = Person("Dodit", 24)

# print(p1.name)
# print(p1.age)

# print(p2.name)
# print(p2.age)

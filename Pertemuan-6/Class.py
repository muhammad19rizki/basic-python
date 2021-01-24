class Myclass:
    x = 5
    y = 10
    luas_persegi =x*y
    luas_lingkaran = 22/7*x*x

def myclassses():
    x = 5
    return x

p1 = Myclass()
p2 = Myclass()
print(p1.luas_persegi)
print(p2.luas_lingkaran)
p2 = myclassses()
print(myclassses())
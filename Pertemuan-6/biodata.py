class biodata:

    def __init__(self,name,age,noTlp):
        self.name = name
        self.age = age
        self.noTlp = noTlp

    def result(self):
        print("Biodata : ")
        print("Nama : " + self.name)
        print("Age : " + self.age)
        print("No Telepon : " + self.noTlp)

bio = biodata(name = input("Nama: "), age = input("Umur: " ), noTlp= input("No Telp: "))
bio.result()
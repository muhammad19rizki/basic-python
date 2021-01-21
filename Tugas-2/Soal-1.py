contact = {}

def menu():
    print("Selamat Datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

def getContact():
    print("Daftar Kontak : ")
    for key, value in contact.items():
        print("Nama: {} \nNo. Telepon: {}".format(key, value))

def createContact():
    print("Tambah Kontak : ")
    name = input("Nama: ")
    telephoneNumber = input("No. Telepon: ")
    contact[name] = telephoneNumber
    print("Kontak berhasil ditambahkan")

def main():
    menu()
    choose = int(input("Pilih Menu : "))
    while True:
        if choose == 1:
            getContact()
            menu()
            choose = int(input("Pilih Menu : "))
        elif choose == 2:
            createContact()
            menu()
            choose = int(input("Pilih Menu : "))
        elif choose == 3:
            print("Program selesai, sampai jumpa!")
            break
        else:
            print("Menu tidak tersedia")
            menu()
            choose = int(input("Pilih Menu : "))
   

main()
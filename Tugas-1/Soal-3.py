teori = int(input("input nilai teori : "))
praktek = int(input("input nilai praktek : "))

if teori<70 and praktek<70:
    print("Anda harus mengulang ujian teori dan praktek")
elif  teori<70 and praktek<=70:
    print("Anda harus mengulang ujian teori")
elif teori<=70 and praktek<70:
    print("Anda harus mengulang ujian praktek")
else:
    print("Selamat, anda lulus!")
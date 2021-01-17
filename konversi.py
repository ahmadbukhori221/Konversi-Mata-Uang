def addmoney (*args):
    hasil = args[0] *args[1]
    return hasil

ulang = ("y")
while ulang == ("y"):
    print ("---------------KONVERSI MATA UANG---------------")
    print ("1. konversi mata uang")
    print ("-----------------------------------------------\n")
    pilihan = int (input("Masukkan pilihan anda : "))
    if pilihan == 1 :
        print ("-------------------KONVERSI MATA UANG-------------------")
        x = int (input("Masukkan jumlah uang dalam dolar: "))
        y = int (input("Masukkan kurs dollar terhadap rupiah: "))
        print(x,"Dollar = Rp ",addmoney(x,y),"Rupiah")
        print ("--------------------------------------------------------\n")
      
    else:
        print("input salah, masukkan 1 ")
        continue
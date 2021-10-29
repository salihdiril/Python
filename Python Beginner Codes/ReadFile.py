musteri_listesi = open("Musteriler", "r")

if musteri_listesi.readable():
    for musteri in musteri_listesi.readlines():
        print(musteri)

musteri_listesi.close()
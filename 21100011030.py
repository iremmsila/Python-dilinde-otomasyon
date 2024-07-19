#İREM SILA SARIKAYA
#21100011030
import json

def kargo():
    while True:
        print("\n")
        print("Sayin musterimiz, KARGOCUM'a hoş geldiniz. Bizi tercih ettiginiz icin tesekkür ederiz!")
        print("1-ekleme")
        print("2-arama")
        print("3-guncelleme")
        print("4-listeleme")
        print("5-silme")
        print("6-ucret hesaplama")
        print("7-teslimat süresi hesaplama")
        print("8-cıkıs")
        islem = input("lütfen yapmak istediginiz islemi seciniz")

        if islem == "1":
            ekleme()

        elif islem == "2":
            arama()

        elif islem == "3":
            guncelleme()

        elif islem == "4":
            listeleme()

        elif islem == "5":
            silme()

        elif islem == "6":
            ucret_hesaplama()

        elif islem == "7":
            mesafe_hesapla()

        elif islem == "8":
            exit()

        else:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            kargo()

def ekleme():
    global kullanici_bilgileri
    kullanici_bilgileri= {}
    global ucret
    global kargo_desisi

    def no_sorgula():
        aranan = str(kargo_no)
        with open("21100011030.txt", "r") as dosya:
            data = dosya.readlines()
        id = '"kargo numarasi": ' + aranan
        bulundu = 0
        for line in data:
            if id in line:
                print(line)
                bulundu += 1
                if bulundu >= 1:
                    print("bu id kullanılıyor\n")
                    return 1


    kargo_no = input("kargo numarasi giriniz")

    donus= no_sorgula()
    kargo_no = int(kargo_no)
    if donus == 1:
        print("bu numara alinmis lütfen farkli bir kargo numarasi giriniz")
        print("(kargo numaralari essiz olmalidir)")
        kargo()

    print("lütfen türkçe karakter kullanmayınız")
    adi = input("adi").upper()
    soyadi = input("soyadi").upper()

    ucret_hesaplama()

    kullanici_bilgileri = {'kargo numarasi': kargo_no,
               'adi': adi,
               'soyadi': soyadi,
               'ucreti': ucret
               }

    with open('21100011030.txt', 'a') as dosya:
        dosya.write(json.dumps(kullanici_bilgileri))
        dosya.write("\n")


def ucret_hesaplama():
    global kargo_desisi
    global ucret

    kargo_desisi = int(input("kargo desisi:"))

    if kargo_desisi < 20:
        ucret = kargo_desisi * 3
        print("gel al noktasından faydalanarak %20 indirim kazanmak ister misiniz?")
        gel_al = input("(e/h)").lower()
        if gel_al == "e":
            ucret -= ucret * 0.2

        print("teslimatta olusabilecek her türlü hasardan kargonu korumak ister misin?\n\n"
                        "sadece %15 fiyat artisi ile kargonu sigortala!")
        sigorta = input("(e/h").lower()
        if sigorta == "e":
            ucret += ucret * 0.15

        ucret = str(ucret)

    elif kargo_desisi < 40:
        ucret = kargo_desisi * 5
        print("gel al noktasından faydalanarak %20 indirim kazanmak ister misiniz?(e/h)")
        gel_al = input("(e/h)")
        if gel_al == "e":
            ucret -= ucret * 0.2

        print("teslimatta olusabilecek her türlü hasardan kargonu korumak ister misin?")
        sigorta = input("sadece %15 fiyat artisi ile kargonu sigortala!(e/h)")
        if sigorta == "e":
            ucret += ucret * 0.15

        ucret = str(ucret)

    elif kargo_desisi < 60:
        ucret = kargo_desisi * 7
        gel_al = input("gel al noktasından faydalanarak %20 indirim kazanmak ister misiniz?(e/h)")
        if gel_al == "e":
            ucret -= ucret * 0.2

        sigorta = input("teslimatta olusabilecek her türlü hasardan kargonu korumak ister misin?"
                        "sadece %15 fiyat artisi ile kargonu sigortala!(e/h)")
        if sigorta == "e":
            ucret += ucret * 0.15

        ucret = str(ucret)

    elif kargo_desisi < 80:
        ucret = kargo_desisi * 9
        gel_al = input("gel al noktasından faydalanarak %20 indirim kazanmak ister misiniz?(e/h)")
        if gel_al == "e":
            ucret -= ucret * 0.2

        sigorta = input("teslimatta olusabilecek her türlü hasardan kargonu korumak ister misin?"
                        "sadece %15 fiyat artisi ile kargonu sigortala!(e/h)")
        if sigorta == "e":
            ucret += ucret * 0.15

        ucret = str(ucret)

    else:
        ucret = kargo_desisi * 15
        gel_al = input("gel al noktasından faydalanarak %20 indirim kazanmak ister misiniz?(e/h)")
        if gel_al == "e":
            ucret -= ucret * 0.2

        sigorta = input("teslimatta olusabilecek her türlü hasardan kargonu korumak ister misin?"
                        "sadece %15 fiyat artisi ile kargonu sigortala!(e/h)")
        if sigorta == "e":
            ucret += ucret * 0.15
        ucret = str(ucret)

    print("\n------> odenecek tutar: ", ucret)
    print("\n")

def arama():
    aranan = input("lütfen aratmak istediğiniz kargo numarasini giriniz")
    with open("21100011030.txt", "r") as dosya:
        data = dosya.readlines()
    id = '"kargo numarasi": ' + aranan
    bulundu = 0
    for line in data:
        if id in line:
            print(line)
            bulundu += 1

    if bulundu == 0:
        print("boyle bir kargo numarası yok")


def listeleme():
    with open("21100011030.txt", "r") as dosya:
        print("-------------------")
        print(dosya.read())
        print("-------------------")
        dosya.seek(0)


def guncelleme():
    print("1-isim degisikligi")
    print("2-soyisim degisikligi")
    islem = input("secim=")                  # id essiz olduğu için degistirilemez

    if islem == "1":
        eski_veri = input("lütfen degisiklik yapma istediğiniz kelimeyi giriniz").upper()
        guncel_veri = input("yeni veri:").upper()
        with open(r'21100011030.txt', 'r') as dosya:
            veri = dosya.read()
            veri = veri.replace(eski_veri, guncel_veri)

        with open(r'21100011030.txt', 'w') as pdosya:
            pdosya.write(veri)

        print("güncelleme başarılı!")

    elif islem == "2":
        eski_veri = input("lütfen degisiklik yapma istediğiniz kelimeyi giriniz").upper()
        guncel_veri = input("yeni veri:").upper()
        with open(r'21100011030.txt', 'r') as dosya:
            veri = dosya.read()
            veri = veri.replace(eski_veri, guncel_veri)

        with open(r'21100011030.txt', 'w' ) as pdosya:
            pdosya.write(veri)

        print("güncelleme başarılı!")

    else:
        print("Hatalı giriş. Lütfen tekrar deneyiniz")
        guncelleme()


def silme():
    aranan = input("lütfen degisiklik yapma istediğiniz kargo numarasini giriniz")

    with open("21100011030.txt", "r") as dosya:
        data = dosya.readlines()

    sil_id = '"kargo numarasi": ' + aranan
    print(sil_id)

    with open("21100011030.txt","w") as dosya:
        for line in data:
            if sil_id in line:
                continue
            else:
                dosya.write(line)


def mesafe_hesapla():
    global km
    print("1-Antalya")
    print("2-Ankara")
    print("3-Mardin")
    print("4-Sivas")
    print("5-Erzurum")
    nereden = input("kargo cikis yeri:")

    no = "0123456789"
    if nereden not in no:
        print("Gecersiz islem. Lutfen tekrar deneyiniz")
        nereden = input("kargo cikis yeri:")


    def km_sorgula():
        if 600 > km:
            print("\n")
            print("*************************")
            print("teslimat süresi 1 iş günü")
            print("\n")
        elif 1200 > km:
            print("\n")
            print("*************************")
            print("teslimat süresi 2 iş günü")
            print("\n")
        else:
            print("\n")
            print("*************************")
            print("teslimat süresi 3 iş günü")
            print("\n")

    if nereden == "1":
        print("1-Ankara")
        print("2-Mardin")
        print("3-Sivas")
        print("4-Erzurum")
        nereye = input("kargo varis yeri:")

        no = "0123456789"
        if nereye not in no:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            nereye = input("kargo varis yeri")

        if nereye == "1":
            km = 573
            km_sorgula()

        elif nereye == "2":
            km = 1152
            km_sorgula()

        elif nereye == "3":
            km = 804
            km_sorgula()

        elif nereye == "4":
            km = 1238
            km_sorgula()

    elif nereden == "2":
        print("1-Antalya")
        print("2-Mardin")
        print("3-Sivas")
        print("4-Erzurum")
        nereye = input("kargo varis yeri:")

        no = "0123456789"
        if nereye not in no:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            nereye = input("kargo varis yeri")

        if nereye == "1":
            km = 573
            km_sorgula()

        elif nereye == "2":
            km = 1040
            km_sorgula()

        elif nereye == "3":
            km = 540
            km_sorgula()

        elif nereye == "4":
            km = 876
            km_sorgula()

    elif nereden == "3":
        print("1-Antalya")
        print("2-Ankara")
        print("3-Sivas")
        print("4-Erzurum")
        nereye = input("kargo varis yeri:")

        no = "0123456789"
        if nereye not in no:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            nereye = input("kargo varis yeri")

        if nereye == "1":
            km = 1155
            km_sorgula()

        elif nereye == "2":
            km = 1043
            km_sorgula()

        elif nereye == "3":
            km = 635
            km_sorgula()

        elif nereye == "4":
            km = 411
            km_sorgula()

    elif nereden == "4":
        print("1-Antalya")
        print("2-Ankara")
        print("3-Mardin")
        print("4-Erzurum")
        nereye = input("kargo varis yeri:")

        no = "0123456789"
        if nereye not in no:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            nereye = input("kargo varis yeri")

        if nereye == "1":
            km = 803
            km_sorgula()

        elif nereye == "2":
            km = 538
            km_sorgula()

        elif nereye == "3":
            km = 605
            km_sorgula()

        elif nereye == "4":
            km = 434
            km_sorgula()

    elif nereden == "5":
        print("1-Antalya")
        print("2-Ankara")
        print("3-Mardin")
        print("4-Sivas")
        nereye = input("kargo varis yeri:")

        no = "0123456789"
        if nereye not in no:
            print("Gecersiz islem. Lutfen tekrar deneyiniz")
            nereye = input("kargo varis yeri")

        if nereye == "1":
            km = 1240
            km_sorgula()

        elif nereye == "2":
            km = 877
            km_sorgula()

        elif nereye == "3":
            km = 492
            km_sorgula()

        elif nereye == "4":
            km = 434
            km_sorgula()
    else:
        print("gecersiz islem lütfen tekrar deneyiniz")
        mesafe_hesapla()

kargo()
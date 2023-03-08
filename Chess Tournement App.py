# Sığmayan yorum satırları yorum gerekn kısımların üstlerine yazılmıştır.
import math


def main():  # Main fonksiyonu bütün fonksiyonların sıralı çalışmasını sağlar..
    lisans_dict, oyuncu_say = sozlukle()
    sirali_list = sirala(lisans_dict, "a")
    ilk_tablo(sirali_list)
    tur_say = tur_al(oyuncu_say)
    ren_tur_list = tur_basi(tur_say, oyuncu_say, sirali_list)
    nihai_tablo(ren_tur_list)
    capraz_tablo(ren_tur_list, tur_say)


def lisans_al(lisans_list):  # Kişiye özel olmak üzere lisans numarasını alır ve yazdırır.
    try:
        lno = int(input("\nOyuncunun lisans numarasini giriniz (bitirmek için 0 ya da negatif giriniz): "))
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        lno = lisans_al(lisans_list)
    else:
        if lno > 0 and lno not in lisans_list:
            lisans_list.append(lno)
        elif lno > 0 and lno in lisans_list:
            print("Lütfen başka kullanıcıya ait değer girmeyiniz!")
            lno = lisans_al(lisans_list)
    return lno


def ad_soyad_al():  # Kişinin adını doğru şekilde alır.
    try:
        ad_soyad = str(input("Oyuncunun adini-soyadini giriniz: "))
        ad_soyad = str(ad_soyad.replace('ı', 'I').replace('i', 'İ').upper())
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        ad_soyad = ad_soyad_al()
    return ad_soyad


def ilk_renk_al():  # En üstteki oyuncunun rengini alır.
    try:
        renk = input("Başlangıç sıralamasına göre ilk oyuncunun ilk turdaki rengini giriniz (b/s): ")
        while renk not in ["s", "b", "S", "B"]:
            print("Lütfen geçerli bir değer giriniz!")
            renk = ilk_renk_al()
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        renk = ilk_renk_al()
    return renk.lower()


def tur_al(oyuncu_sayisi):  # Tur sayısını doğru aralıklarda alır.
    try:
        max_tur = oyuncu_sayisi - 1
        min_tur = math.log2(oyuncu_sayisi)
        min_tur = math.ceil(min_tur)
        tur_say = int(input(f"\nTurnuvadaki tur sayısını giriniz ({min_tur}-{max_tur}): "))
        while tur_say > max_tur or tur_say < min_tur:
            tur_say = tur_al(oyuncu_sayisi)
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        tur_say = tur_al(oyuncu_sayisi)
    return tur_say


def puan_al(durum):  # Farklı puanlama sistemlerinia it puanları alır.
    puan = 0
    try:
        if durum == "a":
            puan = int(input("Uluslararası (FIDE) kuvvet puanınınızı giriniz (ELO): 0,"
                             " 1000 veya daha büyük tam sayı: "))
        elif durum == "b":
            puan = int(input("Ulusal kuvvet puanı (UKD): 0, 1000 veya daha büyük tam sayı "))
        while 0 < puan < 1000 or puan < 0:
            puan = int(input("Lütfen geçerli bir değer giriniz:"))
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        puan = puan_al(durum)
    return puan


def mac_sonuc_al(tur_num, masa_no):  # O turda Belirli masada oynan turun sonucunu doğru şekilde alır.
    try:
        sonuc = input("\n" + str(tur_num + 1) + ". turda " + str(masa_no) +
                      ". masada oynanan maçın sonucunu giriniz (0-5): ")
        while sonuc not in ["0", "1", "2", "3", "4", "5"]:
            sonuc = int(input("Lütfen geçerli bir değer giriniz:"))
    except ValueError:
        print("Lütfen geçerli bir değer giriniz!")
        sonuc = mac_sonuc_al(tur_num, masa_no)
    return sonuc


def sozlukle():  # Alınan değerleri bir sözlüğün içine atar.
    lisans_list = []
    lisans_dict = {}
    oyuncu_sayisi = 0
    lno = lisans_al(lisans_list)
    while lno > 0:
        ad_soyad = ad_soyad_al()
        elo = puan_al("a")
        ukd = puan_al("b")
        puan = 0
        lisans_dict.update({lno: [str(ad_soyad), elo, ukd, puan]})
        oyuncu_sayisi += 1
        lno = lisans_al(lisans_list)
    return lisans_dict, oyuncu_sayisi


def sirala(list_dict, cins):  # Kişileri farklı sıralama kriterlerine göre sıralar.
    harfler = "ABCÇDEFGĞHIİJKLMNPRSŞTUÜVYZ"
    sirali_list = []
    if cins == "a":
        sirali_list = sorted(list_dict.items(), key=lambda veri: (-(veri[1][3]), -(veri[1][1]), -(veri[1][2]),
                                                                  [harfler.index(c) for c in veri[1][0] if
                                                                   c in harfler],
                                                                  veri[0]))
    elif cins == "b":
        sirali_list = sorted(list_dict, key=lambda veri: (-(veri[0][1][3]), -(veri[0][1][1]), -(veri[0][1][2]),
                                                          [harfler.index(c) for c in veri[0][1][0] if
                                                           c in harfler],
                                                          veri[0][0]))
    elif cins == "c":
        sirali_list = sorted(list_dict, key=lambda veri: (-(veri[0][1][3]), -(veri[4][0]), -(veri[4][1]),
                                                          -(veri[4][2]), -(veri[4][3])))
    return sirali_list


def ilk_tablo(sirali_dict):  # İlk sıralanmış tabloyu yazdırır.
    sirali_list = list(sirali_dict)
    print("\nBaşlangıç Sıralama Listesi: ")
    print("BSNo   LNo     Ad-Soyad       ELO    UKD")
    print("----   -----   ------------   ----   ----")
    for veri in range(len(sirali_list)):
        print(format(veri + 1, "4"), end='     ')
        print(str(sirali_list[veri][0]).rjust(3), end="   ")
        print(format(sirali_list[veri][1][0], "4"), end=" " * (15 - len(sirali_list[veri][1][0])))
        print(str(sirali_list[veri][1][1]).rjust(4), end="   ")
        print(str(sirali_list[veri][1][2]).rjust(4))


def renk_degistir(renk):  # Gönderilen rengin tersini döndürür.
    if renk == "s":
        renk2 = "b"
        return renk2
    elif renk == "b":
        renk2 = "s"
        return renk2


# Her bir kullanıcın olası her bir değerini alan dev bir liste döndürür ve
# bu listeye kullancıların ilk renklerini atarak ilk eşleştirmeyi yapar..
def liste_baslat(tur_say, oyuncu_say, sirali_list):
    ren_tur_list = [[sirali_list[kisi], 0, [[0 for tur_ici in range(5)] for tur in range(tur_say)], False,
                     [0 for tur_ici in range(4)], 0, [], []]
                    for kisi in range(oyuncu_say)]
    # İlk tablo yapılır
    renk = ilk_renk_al()
    renk2 = renk_degistir(renk)
    for x in range(len(ren_tur_list)):
        ren_tur_list[x][1] += x + 1
        if x % 2 == 0:
            ren_tur_list[x][2][0][1] = renk
        else:
            ren_tur_list[x][2][0][1] = renk2
    a = 0
    masa_no = 1
    for i in range(oyuncu_say // 2):
        genel_eslestir(a, a + 1, ren_tur_list, 0, masa_no)
        masa_no += 1
        a += 2
    if len(ren_tur_list) % 2 == 1:
        ren_tur_list[-1][2][0][0] = "-"
        ren_tur_list[-1][2][0][4] = ren_tur_list[-1][2][0][1]
        ren_tur_list[-1][2][0][1] = "-"
        ren_tur_list[-1][2][0][2] += 1
        ren_tur_list[-1][3] = True
        ren_tur_list[-1][2][0][3] = (len(ren_tur_list) // 2) + 1
        hayali_rakip_bul(-1, 0, ren_tur_list, tur_say, 6)
        hayali_rakip_bul(-1, 0, ren_tur_list, tur_say, 7)
    return ren_tur_list


def renk_depola(ren_tur_list, kisi, kisi_2, renk, renk_2, tur_num):  # Listeye doğru rengin girilmesini sağlar.
    ren_tur_list[kisi][2][tur_num][1] = renk_2
    ren_tur_list[kisi_2][2][tur_num][1] = renk


# Bütün kodda kullanılacak basit eşleştirme algoritmasıdır.
def genel_eslestir(kisi_1, kisi_2, ren_tur_list, tur_num, masa_no):
    ren_tur_list[kisi_1][2][tur_num][0] = ren_tur_list[kisi_2][1]
    ren_tur_list[kisi_1][2][tur_num][3] = masa_no
    ren_tur_list[kisi_2][2][tur_num][0] = ren_tur_list[kisi_1][1]
    ren_tur_list[kisi_2][2][tur_num][3] = masa_no


# Eşitlik bozma methodlarına eklenecek ek puanı hesaplar.
def hayali_rakip_bul(kisi, tur_num, ren_tur_list, tur_say, a):
    ren_tur_list[kisi][a].append(((tur_say - (tur_num + 1)) * 0.5) + ren_tur_list[kisi][0][1][3])


# Toplam oyuncuların tek sayı olduğu durum için bye oyuncu kontrol algoritması.
def bye_kontrol(ren_tur_list, tur_num, tur_say):
    for a in reversed(ren_tur_list):
        if not a[3]:
            a[3] = True
            a[2][tur_num][0] = "-"
            a[2][tur_num][4] = a[2][tur_num - 1][1]
            a[2][tur_num][1] = "-"
            a[2][tur_num][2] += 1
            a[6].append(((tur_say - (tur_num + 1)) * 0.5) + a[0][1][3])
            a[7].append(((tur_say - (tur_num + 1)) * 0.5) + a[0][1][3])
            a[2][tur_num][3] = (len(ren_tur_list) // 2) + 1
            bye_oyuncu = a[0][0]
            return bye_oyuncu


def bye_puan_ata(ren_tur_list, tur_num):  # Tabloda görünmesin diye bye oyunculara sonradan puan atar.
    for kisi in range(len(ren_tur_list)):
        if ren_tur_list[kisi][2][tur_num][0] == "-" or ren_tur_list[kisi][2][tur_num][2] == "+":
            ren_tur_list[kisi][0][1][3] += 1


def bye_ise(kisi, tur_num):  # bye ise index değiştirir.
    if kisi[2][tur_num][1] != "-":
        a = 1
    else:
        a = 4
    return a


# Girilen sonuçlara göre yapılacak işlemleri yapar. Ayrıca GS eşitlik bozma değerini de yerine atar
def puan_hesap(kisi_1, kisi_2, ren_tur_list, tur_num, masa_no, tur_say):
    sonuc = mac_sonuc_al(tur_num, masa_no)
    if sonuc == "0":
        ren_tur_list[kisi_1][2][tur_num][2] = "½"
        ren_tur_list[kisi_1][0][1][3] += 0.5
        ren_tur_list[kisi_2][2][tur_num][2] = "½"
        ren_tur_list[kisi_2][0][1][3] += 0.5
    elif sonuc == "1":
        ren_tur_list[kisi_1][2][tur_num][2] = 1
        ren_tur_list[kisi_1][0][1][3] += 1
        ren_tur_list[kisi_1][4][3] += 1
    elif sonuc == "2":
        ren_tur_list[kisi_2][2][tur_num][2] = 1
        ren_tur_list[kisi_2][0][1][3] += 1
        ren_tur_list[kisi_2][4][3] += 1
    elif sonuc == "3":
        ren_tur_list[kisi_1][2][tur_num][2] = "+"
        ren_tur_list[kisi_2][2][tur_num][2] = "-"
        hayali_rakip_bul(kisi_1, tur_num, ren_tur_list, tur_say, 6)
        hayali_rakip_bul(kisi_1, tur_num, ren_tur_list, tur_say, 7)
        hayali_rakip_bul(kisi_2, tur_num, ren_tur_list, tur_say, 6)
        ren_tur_list[kisi_1][0][1][3] += 1
        ren_tur_list[kisi_1][4][3] += 1
        ren_tur_list[kisi_1][3] = True
    elif sonuc == "4":
        ren_tur_list[kisi_2][2][tur_num][2] = "+"
        ren_tur_list[kisi_1][2][tur_num][2] = "-"
        hayali_rakip_bul(kisi_1, tur_num, ren_tur_list, tur_say, 6)
        hayali_rakip_bul(kisi_2, tur_num, ren_tur_list, tur_say, 7)
        hayali_rakip_bul(kisi_2, tur_num, ren_tur_list, tur_say, 6)
        ren_tur_list[kisi_2][0][1][3] += 1
        ren_tur_list[kisi_2][4][3] += 1
        ren_tur_list[kisi_2][3] = True
    elif sonuc == "5":
        ren_tur_list[kisi_1][2][tur_num][2] = "-"
        ren_tur_list[kisi_2][2][tur_num][2] = "-"
        hayali_rakip_bul(kisi_1, tur_num, ren_tur_list, tur_say, 6)
        hayali_rakip_bul(kisi_2, tur_num, ren_tur_list, tur_say, 6)


def onceki_iki_renk(ren_tur_list, kisi, tur_num):  # Kişinin o elden önce sahip olduğu iki rengi bulur.
    onceki = [0, 0]
    if (tur_num - 1) >= 0:
        if ren_tur_list[kisi][2][tur_num - 1][1] != "-":
            onceki[1] = (ren_tur_list[kisi][2][tur_num - 1][1])
            if (tur_num - 2) >= 0:
                if ren_tur_list[kisi][2][tur_num - 2][1] != "-":
                    onceki[0] = ren_tur_list[kisi][2][tur_num - 2][1]

    return onceki


# Kişileri geçici olarak bir masada eşleyerek masa başı gerekli puanı atar.
def masalar(ren_tur_list, tur_num, tur_say):
    masa_no = 1
    esliler = []
    son_esliler = []
    for kisi in range(len(ren_tur_list)):
        for kisi_2 in range((len(ren_tur_list))):
            if kisi != kisi_2:
                if ren_tur_list[kisi][2][tur_num][3] == ren_tur_list[kisi_2][2][tur_num][3]:
                    esliler.append([kisi, kisi_2])
    for esli in esliler:
        esli.sort()
    for veri in esliler:
        if veri not in son_esliler:
            son_esliler.append(veri)
    for a in range(len(son_esliler)):
        kisi = son_esliler[a][0]
        kisi_2 = son_esliler[a][1]
        if ren_tur_list[kisi][2][tur_num][1] == "b":
            puan_hesap(kisi, kisi_2, ren_tur_list, tur_num, masa_no, tur_say)
            masa_no += 1
        elif ren_tur_list[kisi_2][2][tur_num][1] == "b":
            puan_hesap(kisi_2, kisi, ren_tur_list, tur_num, masa_no, tur_say)
            masa_no += 1


def rakiple(kisi, ren_tur_list, cins):  # Kişinin bütün rakiplerini bulur.
    rakipler = []
    for tur in range(len(ren_tur_list[kisi][2])):
        if cins == "a":
            if ren_tur_list[kisi][2][tur][0] != 0 or ren_tur_list[kisi][2][tur][0] != "-":
                rakipler.append(ren_tur_list[kisi][2][tur][0])
        elif cins == "b":
            if ren_tur_list[kisi][2][tur][0] != 0 and ren_tur_list[kisi][2][tur][0] != "-" and \
                    ren_tur_list[kisi][2][tur][2] != "-" and ren_tur_list[kisi][2][tur][2] != "+":
                rakipler.append(ren_tur_list[kisi][2][tur][0])
    return rakipler


def sb_rakipler(kisi, ren_tur_list, tur_say):  # Kişinin kazanamadığı rakiplerini bulur.
    yen_rakipler = []
    ber_rakipler = []
    for tur in range(tur_say):
        if ren_tur_list[kisi][2][tur][0] != "-" and ren_tur_list[kisi][2][tur][2] == 1:
            yen_rakipler.append(ren_tur_list[kisi][2][tur][0])
        elif ren_tur_list[kisi][2][tur][0] != "-" and ren_tur_list[kisi][2][tur][2] == "½":
            ber_rakipler.append(ren_tur_list[kisi][2][tur][0])
    return yen_rakipler, ber_rakipler


# Her tur için  1.1 1.2 1.3 sistemlerine göre eşleşmesi gereken oyuncuları
# listede ayrılmış bölüme masa numaralarını atayarak eşler.
def rakip_bul(ren_tur_list, tur_num, tur_say):
    masa_no = 1
    eslenmis = []
    if len(ren_tur_list) / 2 != 1:  # Tek sayıya düşen oyuncu BYE olarak alınır.
        bye_oyuncu = bye_kontrol(ren_tur_list, tur_num, tur_say)
        eslenmis.append(bye_oyuncu)
    for kisi in range(len(ren_tur_list)):
        if ren_tur_list[kisi][0][0] not in eslenmis:
            rakipler = rakiple(kisi, ren_tur_list, "b")
            puan = ren_tur_list[kisi][0][1][3]
            dongu_kir = False
            while not dongu_kir and puan >= 0:
                esles = 1
                while esles <= 3 and not dongu_kir:
                    bas_ind = kisi + 1
                    while bas_ind < len(ren_tur_list) and not dongu_kir:
                        kisi_2 = bas_ind
                        if ren_tur_list[kisi_2][0][1][3] == puan and ren_tur_list[kisi_2][0][0] not in eslenmis:
                            onceki = onceki_iki_renk(ren_tur_list, kisi, tur_num)
                            onceki_2 = onceki_iki_renk(ren_tur_list, kisi_2, tur_num)
                            kontrol = bye_ise(ren_tur_list[kisi], tur_num - 1)
                            renk = ren_tur_list[kisi][2][tur_num - 1][kontrol]
                            istenen_renk = renk_degistir(renk)
                            if ren_tur_list[kisi_2][2][tur_num - 1][1] != "-":
                                renk_2 = ren_tur_list[kisi_2][2][tur_num - 1][1]
                            else:
                                renk_2 = istenen_renk
                            if esles == 1:  # 1.1  eşleştirme esası için
                                if (istenen_renk == renk_2 or onceki_2 == [0, 0]) and \
                                        ren_tur_list[kisi_2][1] not in rakipler:
                                    if onceki != [istenen_renk, istenen_renk] and onceki_2 != [renk, renk]:
                                        renk_depola(ren_tur_list, kisi, kisi_2, renk, istenen_renk, tur_num)
                                        genel_eslestir(kisi, kisi_2, ren_tur_list, tur_num, masa_no)
                                        eslenmis.append(ren_tur_list[kisi][0][0])
                                        eslenmis.append(ren_tur_list[kisi_2][0][0])
                                        masa_no += 1
                                        dongu_kir = True
                            elif esles == 2:  # 1.2  eşleştirme esası için
                                if (renk == renk_2) and ren_tur_list[kisi_2][1] not in rakipler:
                                    if onceki != [istenen_renk, istenen_renk] and onceki_2 != [renk, renk]:
                                        renk_depola(ren_tur_list, kisi, kisi_2, renk, istenen_renk, tur_num)
                                        genel_eslestir(kisi, kisi_2, ren_tur_list, tur_num, masa_no)
                                        eslenmis.append(ren_tur_list[kisi][0][0])
                                        eslenmis.append(ren_tur_list[kisi_2][0][0])
                                        masa_no += 1
                                        dongu_kir = True
                            elif esles == 3:  # 1.3  eşleştirme esası için
                                if (renk == renk_2) and ren_tur_list[kisi_2][1] not in rakipler:
                                    if onceki != [renk, renk] and onceki_2 != [istenen_renk, istenen_renk]:
                                        renk_depola(ren_tur_list, kisi, kisi_2, istenen_renk, renk, tur_num)
                                        genel_eslestir(kisi_2, kisi, ren_tur_list, tur_num, masa_no)
                                        eslenmis.append(ren_tur_list[kisi][0][0])
                                        eslenmis.append(ren_tur_list[kisi_2][0][0])
                                        masa_no += 1
                                        dongu_kir = True
                        bas_ind += 1
                    esles += 1
                puan -= 0.50


def tur_basi(tur_say, oyuncu_say, sirali_list):  # Tur başına döndürülmesi gereken
    ren_tur_list = liste_baslat(tur_say, oyuncu_say, sirali_list)
    for tur in range(tur_say):
        if tur == 0:
            tur_bas_tablo(ren_tur_list, tur)
            bye_puan_ata(ren_tur_list, tur)
            masalar(ren_tur_list, tur, tur_say)
        else:
            ren_tur_list = sirala(ren_tur_list, "b")
            rakip_bul(ren_tur_list, tur, tur_say)
            tur_bas_tablo(ren_tur_list, tur)
            bye_puan_ata(ren_tur_list, tur)
            masalar(ren_tur_list, tur, tur_say)
    bh_hesapla(ren_tur_list)
    sb_hesapla(ren_tur_list, tur_say)
    return ren_tur_list


def bh_hesapla(ren_tur_list):  # BH puanlarını alır.
    for kisi in range(len(ren_tur_list)):
        toplam = []
        rakipler = rakiple(kisi, ren_tur_list, "b")
        for kisi_2 in range((len(ren_tur_list))):
            if kisi != kisi_2:
                if ren_tur_list[kisi_2][1] in rakipler:
                    toplam.append(ren_tur_list[kisi_2][0][1][3])
        toplam.extend(ren_tur_list[kisi][6])
        toplam.sort()

        toplam.pop(0)
        ren_tur_list[kisi][4][0] = sum(toplam)
        toplam.pop(0)  # BH2 için.
        ren_tur_list[kisi][4][1] = sum(toplam)


# SB puanını yenilgileri genelden çıkarark hesaplar.
def sb_hesapla(ren_tur_list, tur_say):
    for kisi in range(len(ren_tur_list)):
        toplam = []
        yen_rakipler, ber_rakipler = sb_rakipler(kisi, ren_tur_list, tur_say)
        for kisi_2 in range((len(ren_tur_list))):
            if kisi != kisi_2:
                if ren_tur_list[kisi_2][1] in yen_rakipler:
                    toplam.append(ren_tur_list[kisi_2][0][1][3])
                elif ren_tur_list[kisi_2][1] in ber_rakipler:
                    toplam.append((ren_tur_list[kisi_2][0][1][3]) / 2)
        toplam.extend(ren_tur_list[kisi][7])
        ren_tur_list[kisi][4][2] = sum(toplam)


# Tur başına yazdırılması gereken değerleri rakiplerin tablodaki yerlerini bularak yazdırır.
def tur_bas_tablo(ren_tur_list, tur_num):
    masa_tur_list = ren_tur_list.copy()
    sirali_masa_tur_list = sorted(masa_tur_list, key=lambda veri: (veri[2][tur_num][3]))
    print("\n" + str(tur_num + 1) + ". Tur Eşleştirme Listesi:")
    print(format("Beyazlar", "^20"), end=" ")
    print(format("Siyahlar", "^16"))
    print("MNo BSNo   LNo Puan - Puan   LNo BSNo")
    print("--- ---- ----- ----   ---- ----- ----")
    for b in sirali_masa_tur_list:
        if b[2][tur_num][1] == "b":
            for s in sirali_masa_tur_list:
                if s[2][tur_num][1] == "s":
                    if b[2][tur_num][3] == s[2][tur_num][3]:
                        print(format(b[2][tur_num][3], "3"), end=" ")
                        print(format(b[1], "4"), end=" ")
                        print(format(b[0][0], "5"), end=" ")
                        print(format(b[0][1][3], "4.2f"), end=" - ")
                        print(format(s[0][1][3], "4.2f"), end=" ")
                        print(format(s[0][0], "5"), end=" ")
                        print(format(s[1], "4"))
        elif b[2][tur_num][1] == "-":
            print(format(b[2][tur_num][3], "3"), end=" ")
            print(format(b[1], "4"), end=" ")
            print(format(b[0][0], "5"), end=" ")
            print(format(b[0][1][3], "4.2f"), end=" - ")
            print("BYE")


def nihai_tablo(ren_tur_list):  # Nihai tabloyu yazdırır ve SNo değerini listeye atar.
    ren_tur_list = sirala(ren_tur_list, "c")
    print("\nNihai Sıralama Listesi:")
    print("SNo BSNo   LNo Ad-Soyad      ELO  UKD Puan  BH-1  BH-2    SB GS")
    print("--- ---- ----- ------------ ---- ---- ---- ----- ----- ----- --")
    for kisi in range(len(ren_tur_list)):
        print(format(kisi + 1, "3"), end=" ")
        print(format(ren_tur_list[kisi][1], "4"), end=" ")
        print(format(ren_tur_list[kisi][0][0], "5"), end=" ")
        print(format(ren_tur_list[kisi][0][1][0], "12"), end=" ")
        print(format(ren_tur_list[kisi][0][1][1], "4"), end=" ")
        print(format(ren_tur_list[kisi][0][1][2], "4"), end=" ")
        print(format(ren_tur_list[kisi][0][1][3], "4.2f"), end=" ")
        print(format(ren_tur_list[kisi][4][0], "5.2f"), end=" ")
        print(format(ren_tur_list[kisi][4][1], "5.2f"), end=" ")
        print(format(ren_tur_list[kisi][4][2], "5.2f"), end=" ")
        print(format(ren_tur_list[kisi][4][3], "2"))
        ren_tur_list[kisi][5] = kisi + 1


def capraz_tablo(ren_tur_list, tur_say):  # Çapraz tabloyu yazdırır.
    print("\nÇapraz Tablo:")
    print("BSNo SNo  LNo Ad-Soyad      ELO  UKD", end=" ")
    for tur_num in range(tur_say):
        print(" " + str(tur_num + 1) + ". Tur", end=" ")
    print("Puan  BH-1  BH-2    SB GS")
    print("---- --- ---- ------------ ---- ----", end=" ")
    for tur_num in range(tur_say):
        print("-------", end=" ")
    print("---- ----- ----- ----- --")
    for kisi in sorted(ren_tur_list, key=lambda veri: veri[1]):
        print(format(kisi[1], "3"), end=" ")
        print(format(kisi[5], "4"), end=" ")
        print(format(kisi[0][0], "4"), end=" ")
        print(format(kisi[0][1][0], "12"), end=" ")
        print(format(kisi[0][1][1], "4"), end=" ")
        print(format(kisi[0][1][2], "4"), end=" ")
        for tur_num in range(tur_say):
            print(f"{kisi[2][tur_num][0]:>3}", end=" ")
            print(format(kisi[2][tur_num][1], "1"), end=" ")
            print(format(kisi[2][tur_num][2], "1"), end=" ")
        print(format(kisi[0][1][3], "4.2f"), end=" ")
        print(format(kisi[4][0], "5.2f"), end=" ")
        print(format(kisi[4][1], "5.2f"), end=" ")
        print(format(kisi[4][2], "5.2f"), end=" ")
        print(format(kisi[4][3], "2"))


main()

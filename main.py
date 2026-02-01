import time
import random
from os import system
from collections import Counter

class Kasyno:
    def __init__(self):
        self.pieniadze = 5000
        self.realna_szansa = 1000
        self.szansa = 1000
        self.dlug = 0
        self.rrso_pozyczka = 20
        self.rrso_kredyt = 200
        self.tax_trans = 0

def lochy():
    def forever():
        time.sleep(8484848)
    try:
        system("cls") # Nie chce mi sie pisac wersji na linuxa
        print(f"Jesteś w lochach.")
        print("Spotkałeś Maćka. Co robisz?")
        odpowiedz = input("(zagaduje/ignoruje): ")
        if (odpowiedz == "zagaduje"):
            print("""
1 - "Siema co tam"
2 - "Iasfsdjf"
3 - "Czemu tu jestes?"
""")
            wybor = int(input("Ktora odpowiedz wybierasz?: "))
            if (wybor == 1):
                print("Ty: Siema, co tam?")
                time.sleep(1)
                print("Maciek: A nic")
                print("""
1 - "Aha ok"
2 - "Uciekamy stad?"
""")
                wybor = int(input("Ktora odpowiedz wybierasz?: "))
                if (wybor == 1):
                    print("Ty: Aha ok")
                    time.sleep(0.5)
                    print("Maciek: Ok")
                    time.sleep(5)
                    print("Przegrales")
                    quit()
                elif (wybor == 2):
                    print("Ty: Uciekamy stad?")
                    time.sleep(1)
                    print("Maciek: Ty sie jeszcze pytasz? Wiadomo")
                    time.sleep(3)
                    print("*Uciekliscie*")
                else:
                    print("Nie")
                    quit()
            elif (wybor == 2):
                print("Ty: Iasfsdjf")
                time.sleep(2)
                print("Maciek: Ej wezcie go do psychiatryka")
                print("Zostales wziety do psychiatryka.")
                forever()
                # Pozniej sie doda psychiatryk
            elif (wybor == 3):
                print("Ty: Czemu tu jestes?")
                time.sleep(0.2)
                print("Maciek: Oszustwa podatkowe")
                print("""
1 - "Niezle"
2 - "Dales zla liczbe w lotto??"
3 - "Uciekamy stad?"
""")
                wybor = int(input("Ktora odpowiedz wybierasz?: "))
                if (wybor == 1):
                    print("Ty: Niezle")
                    time.sleep(0.5)
                    print("Maciek: No")
                    time.sleep(5)
                    print("Przegrales")
                    time.sleep(0.5)
                    quit()
                elif (wybor == 2):
                    print("Ty: Dales zla liczbe w lotto??")
                    time.sleep(0.5)
                    print("Maciek: Skad wiesz?")
                    print("""
1 - "Nie wazne"
2 - "No bo ja tez"
3 - "Uciekamy stad?"
""")
                    wybor = int(input("Ktora odpowiedz wybierasz?: "))
                    if (wybor == 1):
                        print("Ty: Nie wazne")
                        time.sleep(0.5)
                        print("*Maciek ci strzela sierpowego i umierasz*")
                        time.sleep(0.5)
                        quit()
                    elif (wybor == 2):
                        print("Ty: No bo ja tez")
                        time.sleep(1)
                        print("Maciek: XDD")
                        time.sleep(2)
                        print("Ty: Uciekamy stad?")
                        time.sleep(1)
                        print("Maciek: Nie.")
                        time.sleep(3)
                        print("*Maciek wzial didiegodo klatki i zaczal cie winogrować* (przegrales)")
                        time.sleep(0.5)
                        quit()
                    elif (wybor == 3):
                        print("Ty: Uciekamy stad?")
                        time.sleep(1)
                        print("Maciek: Ta")
                        time.sleep(3)
                        print("*Uciekliscie*")
                elif (wybor == 3):
                    print("Ty: Uciekamy stad?")
                    time.sleep(1)
                    print("Maciek: Dobra")
                    time.sleep(3)
                    print("*Uciekliscie*\n")
                else:
                    print("Nie")
                    quit()
            else:
                print("Niepoprawny wybor xd")
                forever()
        elif (odpowiedz == "ignoruje"):
            print("Zignorowales Maćka.")
            forever()
        else:
            print("Nie")
            quit()
    except ValueError:
        print("Wpisz liczbe.")

def ruletka(k: Kasyno):
    try:
        if (k.pieniadze >= 250):
            print("""Jaki tryb? (kolor/pole)""")
            tryb = input("Tryb: ")
            if (tryb in ["kolor", "pole"]):
                if (tryb == "kolor"):
                    print("""
Jaki kolor?
                          
R - Czerwony
G - Zielony
B - Czarny
""")
                    kolor = input("Kolor: ")
                    if (kolor in ["R", "G", "B"]):
                        print("Losuje...")
                        trafione = random.randint(0, 36)
                        time.sleep(10)
                        if (
                            kolor == "R" and trafione in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] or
                            kolor == "B" and trafione in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 28, 31, 33, 35]
                        ):
                            print(f"Wygrales 500zł!")
                            k.pieniadze += 250
                        elif (kolor == "G" and trafione == 0):
                            print(f"Wow!! Wygrales {250 * 36}zł")
                            k.pieniadze += (250 * 36)
                        else:
                            print("Przegrales")
                            k.pieniadze -= 250
                    else:
                        print("Ten kolor nie istnieje")
                elif (tryb == "pole"):
                    print("Jakie pole? (0-36)")
                    pole = int(input("Pole: "))
                    print("Losuje..")
                    trafione = random.randint(0, 36)
                    time.sleep(10)
                    if (pole == trafione):
                        wygrane = 250 * 36
                        print(f"Udalo ci sie!! Wygrywasz {wygrane}zł")
                        k.pieniadze += wygrane
                    else:
                        print("Przegrales")
                        k.pieniadze -= 250
            else:
                print("Musisz podac poprawny tryb")
            k.tax_trans += 1
        else:
            print("Nie stac cie na ruletke")
    except ValueError:
        print("Musisz wpisac poprawne pole!!")

def blackjack(k: Kasyno):
    if (k.pieniadze >= 250):
        k.tax_trans += 1
        karty_krupiera = random.randint(2, 11) + random.randint(2, 11)
        karty_gracza = random.randint(2, 11) + random.randint(2, 11)
        while True:
            if (karty_gracza == 21 and karty_krupiera != 21):
                print(f"O kurde wygrales. (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                k.pieniadze += 500
                break
            elif (karty_gracza != 21 and karty_krupiera == 21):
                print(f"Przegrales. (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                k.pieniadze -= 250
                break
            elif (karty_gracza == 21 and karty_krupiera == 21):
                print(f"Remis (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                break
            if (karty_gracza > 21):
                print(f"Przegrales (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                k.pieniadze -= 250
                break
            if (karty_krupiera > 21):
                print(f"Wygrales (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                k.pieniadze += 500
                break
            print("Karty krupiera: ?")
            print(f"Twoje karty: {karty_gracza}")
            print("Bierzesz czy stoisz?")
            odpowiedz = input("Odpowiedz (stoje/biore): ")
            if (odpowiedz == "biore"):
                karty_gracza += random.randint(2, 11)
                if (karty_krupiera in [18, 19]):
                    if (random.randint(1, 2) == 2):
                        karty_krupiera = 21
                else:
                    if (random.randint(1, 2) == 1):
                        karty_krupiera += random.randint(2, 11)
            elif (odpowiedz == "stoje"):
                if (karty_krupiera in [18, 19]):
                    if (random.randint(1, 2) == 2):
                        karty_krupiera = 21
                else:
                    if (random.randint(1, 2) == 1):
                        karty_krupiera += random.randint(2, 11)
    else:
        print("Nie stac cie na blackjacka")

def lotto(k: Kasyno):
    try:
        def wylosuj():
            return random.randint(1, 49)
        def sprawdz(n):
            if 1 <= n <= 49:
                return True
            else:
                return False
        pula_3 = 0.005
        pula_4 = 0.9
        pula_5 = 5
        pula_6 = 550
        if (k.pieniadze >= 100):
            print(f"!! LOTTO !! WYGRAJ {pula_6} TYSIĘCY !! (tylko dziś)")
            print('Musisz wpisac 6 liczb w zakresie 1-49, wpisanie niepoprawnej liczby zostanie ukarane')
            l_1 = int(input("Pierwsza liczba: ")); l_2 = int(input("Druga liczba: "))
            l_3 = int(input("Trzecia liczba: ")); l_4 = int(input("Czwarta liczba: "))
            l_5 = int(input("Piąta liczba: ")); l_6 = int(input("Szósta liczba: "))
            r_1 = wylosuj(); r_2 = wylosuj()
            r_3 = wylosuj(); r_4 = wylosuj()
            r_5 = wylosuj(); r_6 = wylosuj()
            RP = [r_1, r_2, r_3, r_4, r_5, r_6]
            if (
                sprawdz(l_1) and sprawdz(l_2) and sprawdz(l_3) and sprawdz(l_4) and sprawdz(l_5) and sprawdz(l_6)
            ):
                UP = [l_1, l_2, l_3, l_4, l_5, l_6]
                if (len(UP) == len(set(UP))):
                    if (len(RP) == len(set(RP))):
                        razem = RP + UP
                        counter = Counter(razem)
                        zgadniete = sum(ile - 1 for ile in counter.values() if ile > 1)
                        if (zgadniete in [0, 1, 2]):
                            print(f"Ah.. Nie wygrales nic. Odgadniete liczby: {zgadniete}")
                            k.pieniadze -= 100
                        elif (zgadniete == 3):
                            print(f"Wygrales {pula_3 * 1000}zł!")
                            k.pieniadze += pula_3 * 1000
                        elif (zgadniete == 4):
                            print(f"Wygrales {pula_4 * 1000}zł!!")
                            k.pieniadze += pula_4 * 1000
                        elif (zgadniete == 5):
                            print(f"Wygrales {pula_5} tysiecy zlotych!!")
                            k.pieniadze += pula_5 * 1000
                        elif (zgadniete == 6):
                            print(f"WOWW!! WYGRALES {pula_6} TYSIĘCY ZŁOTYCH!!!")
                            k.pieniadze += pula_6 * 1000
                    else:
                        # Nie chce mi sie pisać rerollu
                        print("Oj! Nasz system losowania ma powtorzenia. To nie twoj blad! Sprobuj ponownie.")
                else:
                    print("Nie mozesz wpisac tych samych liczb w lotto!")
            else:
                print('Musisz wpisac poprawna liczbe! Zostajesz wyrzucony przez rząd do lochów')
                lochy(k)
    except ValueError:
        print("Wpisz liczbe")
    # Wiem ze to wszystko jest koszmarnie napisane ale nwm xd

def splac(k: Kasyno):
    try:
        if (k.dlug > 0):
            print("Ile chcesz splacic?")
            chce = int(input("Chce splacic: "))
            if (chce > k.dlug):
                print("To wiecej niz dlug, lecz po prostu splacimy całość.")
                k.pieniadze -= k.dlug
                k.dlug = 0
                print("Okej. Dziekujemy za splacenie dlugu")
            else:
                k.pieniadze -= chce
                print(f"Dobrze. Splacono {chce}/{round(k.dlug)} zlotych dlugu.")
                k.dlug -= chce
        else:
            print("Nie masz dlugu xd")
    except ValueError:
        print("Wpiszesz liczbe")

def oddaj(k: Kasyno):
    try:
        if (k.pieniadze == 0):
            print("Jak ty pieniedzy nie masz\n")
        else:
            ile = int(input("Ile chcesz oddac?: "))
            if (ile <= 0):
               print("Nie mozesz oddac nic")
            else:
               print("Okej.")
               if (ile > k.pieniadze):
                   print("Nie stac cie by tyle oddac\n")
               else:    
                   k.pieniadze = k.pieniadze - ile
                   k.tax_trans += 1
                   print("Dziekujemy za wplate.\n")
    except ValueError:
        print("Wpisz liczbe")

def kredyt(k: Kasyno):
    try:
        if (k.pieniadze > 10001):
            mozliwosci = [15000, 25000, 50000]
            print("Okej...")
            print("Ile chcesz pozyczyc? (15000, 25000, 50000)")
            ilosc = int(input("Chce pozyczyc: "))
            if (ilosc in mozliwosci):
                print(f"Ok, RRSO to {k.rrso_kredyt}%")
                k.pieniadze = k.pieniadze + ilosc
                k.dlug = k.dlug + (ilosc * (k.rrso_kredyt / 100 + 1))
                k.tax_trans += 1
                print(f"Twoj aktualny dlug to: {round(k.dlug)}\n")
            else:
                print("Nie mozesz wyplacic takiej kwoty\n")
        else:
            print("Nie stac cie na kredyt, potrzebujesz 10001zł.")
    except ValueError:
        print("Wpisz liczbe")

def pozyczka(k: Kasyno):
    try:
        if (k.pieniadze < 100):
            mozliwosci = [500, 1000, 2500, 10000]
            print("Ile chcesz pozyczyc? (500, 1000, 2500, 10000)")
            ilosc = int(input("Chce pozyczyc: "))
            if (ilosc in mozliwosci):
                print(f"Ok, RRSO to {k.rrso_pozyczka}%")
                k.pieniadze = k.pieniadze + ilosc
                k.dlug = k.dlug + (ilosc * (k.rrso_pozyczka / 100 + 1))
                k.tax_trans += 1
                print(f"Twoj aktualny dlug to: {round(k.dlug)}\n")
            else:
                print("Nie mozesz wyplacic takiej kwoty\n")
        else:
            print("Ale po co ci pozyczka, idz wydaj to w kasynie\n")
    except ValueError:
        print("Wpisz liczbe")

def zmien_szanse(k: Kasyno):
    if (500 <= k.realna_szansa <= 1000):
        k.szansa = round(k.szansa - 5)
        k.realna_szansa = round(k.realna_szansa - 5)
    elif (300 <= k.realna_szansa <= 499):
        k.szansa = round(k.szansa - 4)
        k.realna_szansa = round(k.realna_szansa - 4)
    elif (200 <= k.realna_szansa <= 299):
        k.szansa = round(k.szansa - 3)
        k.realna_szansa = round(k.realna_szansa - 3)
    elif (10 <= k.realna_szansa <= 199):
        k.szansa = round(k.szansa - 2)
        k.realna_szansa = round(k.realna_szansa - 2)
    else:
        k.szansa = round(k.szansa)      
        k.realna_szansa = round(k.realna_szansa)  
    k.tax_trans += 1

def praca(k: Kasyno):

    nadgodziny = None
    print("Pracujesz")
    if (random.randint(1, 2) == 1):
        nadgodziny = True
    else:
        nadgodziny = False
    time.sleep(8)
    if (nadgodziny):
        print("Pracujesz na nadgodziny wiec poczekaj jeszcze")
        time.sleep(4)
    pieniadze_wypracowane = random.randint(0, 1000)
    if (pieniadze_wypracowane > 0):
        print(f"Ok masz pieniadze ({pieniadze_wypracowane}zł)")
        k.pieniadze += pieniadze_wypracowane
    else:
        print("HAHAHA PRACODAWCA CIE OKRADL")
        print("CO ROBISZ")
        odpowiedz = input("Odpowiedz (gonie/nic): ")
        if (odpowiedz == "gonie"):
            print("Gonisz pracodawce")
            time.sleep(3)
            udalo_sie = None
            if (random.randint(1, 3) == 3): 
                udalo_sie = True 
            else: 
                udalo_sie = False
            if (udalo_sie):
                print("Udalo sie")
                k.pieniadze += 5000
            else:
                print("Nie udalo sie")
                if (k.pieniadze >= 500):
                    k.pieniadze -= 500
                else:
                    k.pieniadze = 0
        elif (odpowiedz == "nic"):
            print("Ok, pracodawca uciekl.")
    k.tax_trans += 1
                
def main():
    k = Kasyno()
    try:
        while True:
            print(f"Pieniadze na kasyno: {round(k.pieniadze)}")
            if (k.dlug > 0):
                print(f"Masz dlug wynoszacy {round(k.dlug)} zlotych. Dlug bedzie automatycznie splacany w kwocie 2% długu przy kazdej transkacji.")
                if (k.pieniadze < (k.dlug * 0.02)):
                    print("Nie masz pieniedzy na splacenie dlugu, wypozycz wiecej albo sie pozegnaj z mieszkaniem")
                else:
                    splacono = k.pieniadze * 0.02
                    k.pieniadze = k.pieniadze * 0.98
                    k.dlug = k.dlug - splacono
                    print("Pomyslnie splacono 2%~ długu.")
                    # Bo nie chce mi sie pisac systemu spłacania
                    # A i to do naprawienia bo tez zle dziala xd
                    # Okej juz dziala ale nie chce mi sie usuwac tych komentarzy
            if (k.tax_trans >= 30):
                k.tax_trans = 0
                if (k.pieniadze >= 100):
                    k.pieniadze -= k.pieniadze / 10
                    print(f"Zabrano podatek {round(k.pieniadze / 10)}zł. (więcej na inne)")
                else:
                    k.dlug += 1000
                    print("Nałożono dług 1000 złotych ze względu na brak wystarczającej ilości pieniędzy na koncie, by zapłacić podatki.")
            print("$$$ KASYNO $$$")
            print(f"Masz szanse 1/{k.szansa}")
            print("Wybierz sobie liczbe bo to kasyno i jak zgadniesz liczbe 0-9 to wygrasz pieniadze")
            liczba = input("Jaka? (/sklep/gry/inne): ")
            if (liczba == "sklep"):
                while True:
                    print("Witaj w sklepie")
                    print("Wpisz 'szansa' by zwiekszyc swoja szanse w kasynie o 0.5% (za 300zl)")
                    print("Wpisz 'pozyczka' by pozyczyc pieniadze")
                    print("Wpisz 'kredyt' by wziac kredyt")
                    co = input(": ")
                    if (co == "szansa"):
                        if ((k.pieniadze - 300) < 0):
                            print("Nie stac cie")
                        else:    
                            print("Ok")
                            k.pieniadze -= 300
                            zmien_szanse(k)
                    elif (co == "pozyczka"):
                        print("Ok")
                        pozyczka(k)
                    elif (co == "kredyt"):
                        print("Ok")
                        kredyt(k)
                    else:
                        print("ok")
                        break
            elif (liczba == "wyjdz"):
                quit()
            elif (liczba == "gry"):
                while True:
                    print("Wpisz 'blackjack' by zagrac w blackjacka (250zl)")
                    print("Wpisz 'ruletka' by zagrac w ruletke (250zl)")
                    print("Wpisz 'lotto' by zagrac w lotto (100zl)")
                    co = input(": ")
                    if (co == "blackjack"):
                        blackjack(k)
                    elif (co == "ruletka"):
                        ruletka(k)
                    elif (co == "lotto"):
                        lotto(k)
                    else:
                        print("ok")
                        break
            elif (liczba == "inne"):
                while True:
                    print("Wpisz 'oddaj' by oddac pieniadze w rece panstwowe")
                    print("Wpisz 'praca' by pracowac")
                    print("Wpisz 'podatki' by zobaczyc informacje o podatkach.")
                    print("Wpisz 'splac' by splacic dlug")
                    co = input(": ")
                    if (co == "oddaj"):
                        print("Oj tak")
                        oddaj(k)
                    elif (co == "praca"):
                        praca(k)
                    elif (co == "podatki"):
                        print("""
Podatki zabierają ci 10% twojego stanu bankowego co 30 transakcji. 
Sprawdzenie informacji o podatkach NIE liczy się jako transakcja.
W momentu niskiego stanu konta, państwo nałoży dług w ilości 1000 złotych.
""")
                    elif (co == "splac"):
                        splac(k)
                    else:
                        print("ok")
                        break
            else:
                time.sleep(1)
                print("Procesuje liczbe czekaj")
                if (k.pieniadze >= 100):
                    time.sleep(1)
                    print("Dobra\n")
                    time.sleep(1)
                    if(random.randint(1, k.realna_szansa) != (round(k.realna_szansa * 0.84))):
                    # Nie chodzi mi o 84% tylko o 1/1000 i tak 0.84 jest przypadkowe
                        print("Oj niestety nie wygrales przykro mi")
                        k.pieniadze -= 100
                    else:
                        print("O KURDE JACKPOT")
                        k.pieniadze = k.pieniadze + 100000
                        k.realna_szansa += 50
                    k.tax_trans += 1
                else:
                    print("Nie stac cie juz wiecej na kasyno, wez pozyczke w sklepie")
    except KeyboardInterrupt:
        print("Nie nie wychodzisz z kasyna")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

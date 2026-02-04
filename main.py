import time
import random
import os
from collections import Counter

class Kasyno:
    def __init__(self):
        self.pieniadze = 5000
        self.realna_szansa = 1000
        self.szansa = 1000
        self.dlug = 0
        self.rrso_kredyt = 200
        self.tax_trans = 0
        self.pracodawca = 1
        self.kung_fu_1_raz = True
        self.mistrz_kungfu = ""
        self.sila = 0
        self.zrecznosc = 0
        self.social_credit = 0

# FUNCKJE POMOCNICZE

def inputint(m: str):
    try:
        i = int(input(m))
        return i
    except ValueError:
        print("Wpisz liczbe!!")
    except EOFError:
        print("XDD Nie klikaj Ctrl + Z + Enter wiecej bo zostaniesz wrzcuony do lochow")

def rng(first: int, last: int):
    return random.randint(first, last)

def czekaj(ile: float = 1):
    time.sleep(ile)

def in_range(first: int, last: int, num: float):
    return True if first <= num <= last else False

def lochy(powod: str):
    def forever():
        czekaj(848484)
    def handle_else():
        print("Nie mozesz tak zrobic xd")
        czekaj(2.5)
        quit()
    
    # Kiedys ja to na kotlina przepisze
    os.system("cls" if (os.name == 'nt') else "clear")
    print(f"{powod}\n")
    print(f"Jesteś w lochach.")
    print("Spotkałeś Maćka. Co robisz?")
    odpowiedz = input("(zagaduje/ignoruje): ")
    match (odpowiedz):
        case "zagaduje":  
            print("""
1 - "Siema co tam"
2 - "Iasfsdjf"
3 - "Czemu tu jestes?"
""")
            wybor = inputint("Ktora odpowiedz wybierasz?: ")
            match (wybor):
                case 1: 
                    print("Ty: Siema, co tam?")
                    czekaj(1)
                    print("Maciek: A nic")
                    print("""
1 - "Aha ok"
2 - "Uciekamy stad?"
""")
                    wybor = inputint("Ktora odpowiedz wybierasz?: ")
                    match (wybor):
                        case 1: 
                            print("Ty: Aha ok")
                            czekaj(0.5)
                            print("Maciek: Ok")
                            czekaj(5)
                            print("[Przegrales]")
                            czekaj(2.5)
                            quit()
                        case 2:
                            print("Ty: Uciekamy stad?")
                            czekaj(1)
                            print("Maciek: Ty sie jeszcze pytasz? Wiadomo")
                            czekaj(3)
                            print("*Uciekliscie*")
                        case _:
                            handle_else()
                case 2:
                    print("Ty: Iasfsdjf")
                    czekaj(2)
                    print("Maciek: Ej wezcie go do psychiatryka")
                    print("Zostales wziety do psychiatryka.")
                    forever()
                    # Pozniej sie doda psychiatryk
                case 3:
                    print("Ty: Czemu tu jestes?")
                    czekaj(0.2)
                    print("Maciek: Oszustwa podatkowe")
                    print("""
1 - "Niezle"
2 - "Dales zla liczbe w lotto??"
3 - "Uciekamy stad?"
""")
                    wybor = inputint("Ktora odpowiedz wybierasz?: ")
                    match (wybor):
                        case 1: 
                            print("Ty: Niezle")
                            czekaj(0.5)
                            print("Maciek: No")
                            czekaj(5)
                            print("[Przegrales]")
                            czekaj(2.5)
                            quit()
                        case 2:
                            print("Ty: Dales zla liczbe w lotto??")
                            czekaj(0.5)
                            print("Maciek: Skad wiesz?")
                            print("""
1 - "Nie wazne"
2 - "No bo ja tez"
3 - "Uciekamy stad?"
""")
                            wybor = inputint("Ktora odpowiedz wybierasz?: ")
                            match (wybor):
                                case 1: 
                                    print("Ty: Nie wazne")
                                    czekaj(0.5)
                                    print("*Maciek ci strzela sierpowego i umierasz*")
                                    czekaj(2.5)
                                    quit()
                                case 2:
                                    print("Ty: No bo ja tez")
                                    czekaj(1)
                                    print("Maciek: XDD")
                                    czekaj(2)
                                    print("""
1 - "No"
2 - "Uciekamy stad?"
""")
                                    wybor = inputint("Ktora odpowiedz wybierasz?: ")
                                    match wybor:
                                        case 1:
                                            print("Ty: No")
                                            czekaj(1)
                                            print("Maciek: Tak")
                                            czekaj(1)
                                            print("Ty: Ok")
                                            czekaj(1)
                                            print("Maciek: *zaczyna tanczyc hinduskie tango*")
                                            czekaj(1)
                                            print("[Przegrales]")
                                            czekaj(2.5)
                                            quit()
                                        case 2:
                                            print("Ty: Uciekamy stad?")
                                            czekaj(1)
                                            print("Maciek: Nie.")
                                            czekaj(3)
                                            print("*Maciek wzial didiegodo klatki i zaczal cie winogrować* (przegrales)")
                                            czekaj(2.5)
                                            quit()
                                        case _:
                                            handle_else()
                                case 3:
                                    print("Ty: Uciekamy stad?")
                                    czekaj(1)
                                    print("Maciek: Ta")
                                    czekaj(3)
                                    print("*Uciekliscie*")
                                case _:
                                    handle_else()
                        case 3:
                            print("Ty: Uciekamy stad?")
                            czekaj(1)
                            print("Maciek: Dobra")
                            czekaj(3)
                            print("*Uciekliscie*\n")
                        case _:
                            handle_else()
                case _:
                    handle_else()
        case ("ignoruje"):
            print("Zignorowales Maćka.")
            forever()
        case _:
            handle_else()

def ruletka(k: Kasyno):
    POLA_CZERWONE = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    POLA_CZARNE = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 29, 28, 31, 33, 35}
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
                    trafione = rng(0, 36)
                    czekaj(1.5)
                    if (
                        kolor == "R" and trafione in POLA_CZERWONE or
                        kolor == "B" and trafione in POLA_CZARNE
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
                pole = inputint("Pole: ")
                print("Losuje..")
                trafione = rng(0, 36)
                czekaj(1.5)
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

def blackjack(k: Kasyno):
    if (k.pieniadze >= 250):
        k.tax_trans += 1
        karty_krupiera = rng(2, 11) + rng(2, 11)
        karty_gracza = rng(2, 11) + rng(2, 11)
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
                karty_gracza += rng(2, 11)
                if (karty_krupiera in [18, 19]):
                    if (rng(1, 2) == 2):
                        karty_krupiera = 21
                else:
                    if (rng(1, 2) == 1):
                        karty_krupiera += rng(2, 11)
            elif (odpowiedz == "stoje"):
                if (karty_krupiera in [18, 19]):
                    if (rng(1, 2) == 2):
                        karty_krupiera = 21
                else:
                    if (rng(1, 2) == 1):
                        karty_krupiera += rng(2, 11)
    else:
        print("Nie stac cie na blackjacka")

def kungfupanda(k: Kasyno):
        if (k.kung_fu_1_raz):
            print("Witaj w treningu sztuki walk!")
            print("Najpierw musisz wybrac swojego trenera") # to nic nie zmienia xd
            print("""
1 - Xiao pu
2 - Daigo
3 - Nunu
""")
            wybor = inputint("Ktorego mistrza wybierasz?: ")
            if (wybor in [1, 2, 3]):
                czekaj(1)
                if (wybor == 1):
                    k.mistrz_kungfu = "Xiao pu"
                elif (wybor == 2):
                    k.mistrz_kungfu = "Daigo"
                elif (wybor == 3):
                    k.mistrz_kungfu = "Nunu"
                print("Swietnie! Pamietaj, trenowanie moze ci pomoc nawalac pracodawce jak cie okradnie i przezyc w lochach!")
                czekaj(1)
                print("No dobrze, zrecznosc odpowiada za twoja predkosc, a sila no za sile")
                czekaj(1)
                print("Wiec to wszystko z twojego pierwszego treningu. Wejściówka to była 300zł wiec tyle zabierzemy.")
                if (k.pieniadze >= 300):
                    k.pieniadze -= 300
                else:
                    print("Oj! Nie masz tyle na koncie. Zrobimy dlug, z RRSO 150%")
                    k.dlug += 750
                k.kung_fu_1_raz = False
            else:
                czekaj(1)
                print("Musisz wybrac poprawnego mistrza!!")
                if (k.pieniadze >= 50):
                    k.pieniadze -= 50 # za nieposłuszeństwo
                else:
                    k.dlug += 100
        else:
            czy_zajety = True if (rng(1, 5) == 3) else False
            if (czy_zajety):
                print(f"Witaj ponownie. Aktualnie {k.mistrz_kungfu} jest zajęty. Ale zabierzemy 500zł dla zasady.\n")
                if (k.pieniadze >= 500):
                    k.pieniadze -= 500
                else:
                    czekaj(1/3)
                    print("Oj! Nie masz tyle pieniedzy, nalozymy dlug 1200zł!!")
                    k.dlug += 1200
            else:
                if (k.pieniadze >= 250):
                    mozliwe_treningi_sila = [
                        f"*Nawalasz sie z mistrzem {k.mistrz_kungfu}*",
                        f"*Bijesz makenina*"
                    ]
                    mozliwe_treningi_zrecznosc = [
                        f"*Biegniesz za twoim pracodawcom ktury cie okradł*",
                        f"*Uciekasz przed czyms co cie goni*"
                    ]
                    print("Witaj ponownie! Dzisiaj trenujemy.")
                    czekaj(0.5)
                    print(f"Masz {k.sila} siły")
                    czekaj(0.25)
                    print(f"I {k.zrecznosc} zręczności.")
                    czekaj(1)
                    print("Co dzisiaj chcesz trenować? (S = siła, Z = zręczność)")
                    wybor = input("Trenuje: ")
                    if (wybor in ["S", "Z"]):
                        if (wybor == "S"):
                            print("Dobrze, dzisiaj trenujemy siłe.")
                            print(random.choice(mozliwe_treningi_sila))
                            udalo_sie = True if (rng(1, 10) in [1, 2, 3, 4, 5, 6, 7, 8, 9]) else False
                            if (udalo_sie):
                                ile_sily = rng(1, 3)
                                czekaj(1)
                                print(f"Dostales {ile_sily} siły!")
                                k.sila += ile_sily
                            else:
                                print("Oj! Oberwales, tracisz siłe")
                                if (k.sila >= 1):
                                    k.sila -= 1
                        elif (wybor == "Z"):
                            print("Dobrze, dzisiaj trenujemy zrecznosc.")
                            print(random.choice(mozliwe_treningi_zrecznosc))
                            udalo_sie = True if (rng(1, 10) in [1, 2, 3, 4, 5, 6, 7, 8, 9]) else False
                            if (udalo_sie):
                                ile_zrecznosci = rng(1, 3)
                                czekaj(1)
                                print(f"Dostales {ile_zrecznosci} zręczności!")
                                k.zrecznosc += ile_zrecznosci
                            else:
                                print("Oj! Oberwales, tracisz zrecznosc")
                                if (k.zrecznosc >= 1):
                                    k.zrecznosc -= 1
                    else:
                        print("Musisz wybrac poprawny trening!")
                    k.pieniadze -= 250
                else:
                    print("Nie stac cie na trening!")

def lotto(k: Kasyno):
    def wylosuj():
        return rng(1, 49)
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
        l_1 = inputint("Pierwsza liczba: "); l_2 = inputint("Druga liczba: ")
        l_3 = inputint("Trzecia liczba: "); l_4 = inputint("Czwarta liczba: ")
        l_5 = inputint("Piąta liczba: "); l_6 = inputint("Szósta liczba: ")
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
                    # Tu niestety nie lochy..
            else:
                lochy("Wpisales te same liczby w lotto")
        else:
            lochy("Wpisales zla liczbe w lotto.")
    # Wiem ze to wszystko jest koszmarnie napisane ale nwm xd

def splac(k: Kasyno):
    if (k.dlug > 0):
        print("Ile chcesz splacic?")
        chce = inputint("Chce splacic: ")
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

def oddaj(k: Kasyno):
    if (k.pieniadze == 0):
        print("Jak ty pieniedzy nie masz\n")
    else:
        ile = inputint("Ile chcesz oddac?: ")
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
                if (ile >= 10000):
                    k.social_credit += 5
                elif (in_range(5000, 9999, ile)):
                    k.social_credit += 4
                elif (in_range(2500, 4999, ile)):
                    k.social_credit += 3
                elif (in_range(500, 2499, ile)):
                    k.social_credit += 2
                elif (in_range(250, 499, ile)):
                    k.social_credit += 1
                # Tak wiem ze tu mozna np zrobic 2x 500 i masz tyle social creditów 
                # co za 1x 5000 ale nie chce mi sie tego zmienaic 

def kredyt(k: Kasyno):
    if (k.pieniadze > 10001):
        mozliwosci = [15000, 25000, 50000]
        print("Okej...")
        print("Ile chcesz pozyczyc? (15000, 25000, 50000)")
        ilosc = inputint("Chce pozyczyc: ")
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

def pozyczka(k: Kasyno):
    def calculate_rrso():
        if (k.social_credit >= 100):
            return 5
        elif (in_range(50, 99, k.social_credit)):
            return 10
        elif (in_range(10, 49, k.social_credit)):
            return 15
        else:
            return 20
    rrso = calculate_rrso()
    if (k.pieniadze < 100):
        mozliwosci = [500, 1000, 2500, 10000]
        print("Ile chcesz pozyczyc? (500, 1000, 2500, 10000)")
        ilosc = inputint("Chce pozyczyc: ")
        if (ilosc in mozliwosci):
            print(f"Ok, RRSO to {rrso}%")
            k.pieniadze = k.pieniadze + ilosc
            k.dlug = k.dlug + (ilosc * (rrso / 100 + 1))
            k.tax_trans += 1
            print(f"Twoj aktualny dlug to: {round(k.dlug)}\n")
        else:
            print("Nie mozesz wyplacic takiej kwoty\n")
    else:
        print("Ale po co ci pozyczka, idz wydaj to w kasynie\n")

def zmien_szanse(k: Kasyno):
    if (in_range(500, 1000, k.realna_szansa)):
        k.szansa = round(k.szansa - 5)
        k.realna_szansa = round(k.realna_szansa - 5)
    elif (in_range(300, 499, k.realna_szansa)):
        k.szansa = round(k.szansa - 4)
        k.realna_szansa = round(k.realna_szansa - 4)
    elif (in_range(200, 299, k.realna_szansa)):
        k.szansa = round(k.szansa - 3)
        k.realna_szansa = round(k.realna_szansa - 3)
    elif (in_range(11, 199, k.realna_szansa)):
        k.szansa = round(k.szansa - 2)
        k.realna_szansa = round(k.realna_szansa - 2)
    else:
        k.szansa = round(k.szansa)      
        k.realna_szansa = round(k.realna_szansa)  
    k.tax_trans += 1

def praca(k: Kasyno):
    def oblicz_szanse_dogoniecie():
        if (k.zrecznosc >= 100):
            return True if (rng(1, 5) in [1, 2, 3, 4]) else False # 80%
        elif (k.zrecznosc >= 50):
            return True if (rng(1, 4) in [1, 2, 3]) else False # 75%
        elif (k.zrecznosc >= 25):
            return True if (rng(1, 3) in [1, 2]) else False # 67%
        elif (k.zrecznosc >= 10):
            return True if (rng(1, 2) == 1) else False # 50%
        elif (k.zrecznosc >= 0):
            return True if (rng(1, 3) == 1) else False # 33%
        else:
            return False

    def oblicz_szanse_pobicie():
        if (k.sila >= 100):
            return True if (rng(1, 6) in [1, 2, 3, 4, 5]) else False # 83%
        elif (k.sila >= 50):
            return True if (rng(1, 5) in [1, 2, 3, 4]) else False # 80%
        elif (k.sila >= 25):
            return True if (rng(1, 4) in [1, 2, 3]) else False # 75%
        elif (k.sila >= 10):
            return True if (rng(1, 3) in [1, 2]) else False # 67%
        elif (k.sila >= 0):
            return True if (rng(1, 2) == 1) else False # 50%
        else:
            return False
        
    nadgodziny = None
    print(f"Pracujesz u pracodawcy #{k.pracodawca}")
    if (rng(1, 2) == 1):
        nadgodziny = True
    else:
        nadgodziny = False
    czekaj(8)
    if (nadgodziny):
        print("Pracujesz na bezpłatne nadgodziny wiec poczekaj jeszcze")
        czekaj(4)
    pieniadze_wypracowane = rng(1, 1000)
    czy_okradnal = True if (rng(1, 10) == 1) else False
    if (not czy_okradnal):
        if (pieniadze_wypracowane):
            print(f"Ok masz pieniadze ({pieniadze_wypracowane}zł)")
            k.pieniadze += pieniadze_wypracowane
    else:
        print("XDDD PRACODAWCA CIE OKRADL")
        print("CO ROBISZ")
        odpowiedz = input("Odpowiedz (gonie/nic): ")
        match (odpowiedz):
            case "gonie":
                print("GONISZ PRACODAWCE...")
                czekaj(3)
                udalo_sie = None
                if (oblicz_szanse_dogoniecie()): 
                    udalo_sie = True 
                else: 
                    udalo_sie = False
                if (udalo_sie):
                    print("Udalo sie dogonic pracodawce")
                    co = input("Co z nim robisz/? (bije/konfrontuje): ")
                    print("Bijesz sie z pracodawca...")
                    match (co):
                        case "bije":
                            if (oblicz_szanse_pobicie()): 
                                print("Pobiles go!")
                                k.pieniadze += 5000
                            else:
                                print("Nie udalo sie")
                                if (k.pieniadze >= 500):
                                    k.pieniadze -= 500
                                else:
                                    k.dlug += 1000
                        case "konfrontuje":
                            print("Ty: CO TY ZROBILES")
                            czekaj(1)
                            print("*Pracodawca ucieka*")
                        case _:
                            print("Nie mozesz tak zrobic, ale uciekl jak cos")
                else:
                    print("Nie udalo sie")
                    if (k.pieniadze >= 500):
                        k.pieniadze -= 500
                    else:
                        k.pieniadze = 0
            case "nic":
                print("Ok, pracodawca uciekl.")
            case _:
                print("To nie jest odpowiedz ale i tak pracodawca uciekl")
        k.pracodawca += 1
    k.tax_trans += 1

def main_sklep(k: Kasyno):
    while True:
        print("Witaj w sklepie")
        print("Wpisz 'szansa' by zwiekszyc swoja szanse w kasynie o 0.5% (za 300zl)")
        print("Wpisz 'pozyczka' by pozyczyc pieniadze")
        print("Wpisz 'kredyt' by wziac kredyt")
        co = input(": ")
        match (co):
            case "szansa":
                if ((k.pieniadze - 300) < 0):
                    print("Nie stac cie")
                else:    
                    print("Ok")
                    k.pieniadze -= 300
                    zmien_szanse(k)
            case "pozyczka":
                print("Ok")
                pozyczka(k)
            case "kredyt":
                print("Ok")
                kredyt(k)
            case _:
                print("ok")
                break

def main_gry(k: Kasyno):
    while True:
        print("Wpisz 'blackjack' by zagrac w blackjacka (250zl)")
        print("Wpisz 'ruletka' by zagrac w ruletke (250zl)")
        print("Wpisz 'lotto' by zagrac w lotto (100zl)")
        co = input(": ")
        match (co):
            case "blackjack":
                blackjack(k)
            case "ruletka":
                ruletka(k)
            case "lotto":
                lotto(k)
            case _:
                print("ok")
                break
               
def main_inne(k: Kasyno):
    while True:
        print("Wpisz 'oddaj' by oddac pieniadze w rece panstwowe")
        print("Wpisz 'praca' by pracowac")
        print("Wpisz 'podatki' by zobaczyc informacje o podatkach.")
        print("Wpisz 'splac' by splacic dlug")
        print("Wpisz 'walka' by trenowac sztuki walk")
        co = input(": ")
        match (co):
            case "oddaj":
                print("Oj tak")
                oddaj(k)
            case "praca":
                praca(k)
            case "podatki":
                print("""
Podatki zabierają ci 10% twojego stanu bankowego co 30 transakcji. 
Sprawdzenie informacji o podatkach NIE liczy się jako transakcja.
W momentu niskiego stanu konta, państwo nałoży dług w ilości 1000 złotych.
""")
            case "splac":
                splac(k)
            case "walka":
                kungfupanda(k)
            case _:
                print("ok")
                break

def main_los(k: Kasyno):
    czekaj(1)
    print("Procesuje liczbe czekaj")
    if (k.pieniadze >= 100):
        czekaj(1)
        print("Dobra\n")
        czekaj(1)
        if (rng(1, k.realna_szansa) != (round(k.realna_szansa * 0.84))):
            # Nie chodzi mi o 84% tylko o domyslne 1/1000 i tak 0.84 jest przypadkowe
            print("Oj niestety nie wygrales przykro mi")
            k.pieniadze -= 100
        else:
            print("O KURDE JACKPOT")
            k.pieniadze = k.pieniadze + 100000
            k.realna_szansa += 50
        k.tax_trans += 1
    else:
        print("Nie stac cie juz wiecej na kasyno, wez pozyczke w sklepie")

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
                    splacono = k.dlug * 0.02
                    k.pieniadze = k.pieniadze - splacono
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
            if (not k.szansa < 10):
                print(f"Masz szanse 1/{k.szansa}")
            else:
                print(f"Masz szanse 1/{k.realna_szansa}")
            print("Wybierz sobie liczbe bo to kasyno i jak zgadniesz liczbe 0-9 to wygrasz pieniadze")
            liczba = input("Jaka? (/sklep/gry/inne): ")

            opcje = { "sklep": main_sklep, "gry": main_gry, "inne": main_inne }
            opcje.get(liczba, main_los)(k)

    except KeyboardInterrupt:
        print("Troche smutno ze chcesz opuscic kasyno no ale dobra..")
    except EOFError:
        print("Xdd myslales ze przechytrzysz kasyno ale nie, my znamy takie sztuczki")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

import time
import random

pieniadze = 5000
realna_szansa = 1000
szansa = 1000
dlug = 0
rrso_pozyczka = 20
rrso_kredyt = 200
tax_trans = 0

def ruletka():
    global pieniadze
    global tax_trans
    try:
        if (pieniadze >= 250):
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
                            pieniadze += 250
                        elif (kolor == "G" and trafione == 0):
                            print(f"Wow!! Wygrales {250 * 36}zł")
                            pieniadze += (250 * 36)
                        else:
                            print("Przegrales")
                            pieniadze -= 250
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
                        pieniadze += wygrane
                    else:
                        print("Przegrales")
                        pieniadze -= 250
            else:
                print("Musisz podac poprawny tryb")
            tax_trans += 1
        else:
            print("Nie stac cie na ruletke")
    except ValueError:
        print("Musisz wpisac poprawne pole!!")

def blackjack():
    global pieniadze
    global tax_trans
    if (pieniadze >= 250):
        tax_trans += 1
        karty_krupiera = random.randint(2, 11) + random.randint(2, 11)
        karty_gracza = random.randint(2, 11) + random.randint(2, 11)
        while True:
            if (karty_gracza == 21 and karty_krupiera != 21):
                print(f"O kurde wygrales. (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                pieniadze += 500
                break
            elif (karty_gracza != 21 and karty_krupiera == 21):
                print(f"Przegrales. (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                pieniadze -= 250
                break
            elif (karty_gracza == 21 and karty_krupiera == 21):
                print(f"Remis (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                break
            if (karty_gracza > 21):
                print(f"Przegrales (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                pieniadze -= 250
                break
            if (karty_krupiera > 21):
                print(f"Wygrales (krupier miał {karty_krupiera} kart, a ty {karty_gracza})")
                pieniadze += 500
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

def oddaj():
    global pieniadze
    global tax_trans
    try:
        if (pieniadze == 0):
            print("Jak ty pieniedzy nie masz\n")
        else:
            ile = int(input("Ile chcesz oddac?: "))
            if (ile <= 0):
               print("Nie mozesz oddac nic")
            else:
               print("Okej.")
               if (ile > pieniadze):
                   print("Nie stac cie by tyle oddac\n")
               else:    
                   pieniadze = pieniadze - ile
                   tax_trans += 1
                   print("Dziekujemy za wplate.\n")
    except ValueError:
        print("Wpisz liczbe")

def kredyt():
    global pieniadze
    global rrso_kredyt
    global tax_trans
    global dlug
    try:
        if (pieniadze > 10001):
            mozliwosci = [15000, 25000, 50000]
            print("Okej...")
            print("Ile chcesz pozyczyc? (15000, 25000, 50000)")
            ilosc = int(input("Chce pozyczyc: "))
            if (ilosc in mozliwosci):
                print(f"Ok, RRSO to {rrso_kredyt}%")
                pieniadze = pieniadze + ilosc
                dlug = dlug + (ilosc * (rrso_kredyt / 100 + 1))
                tax_trans += 1
                print(f"Twoj aktualny dlug to: {round(dlug)}\n")
            else:
                print("Nie mozesz wyplacic takiej kwoty\n")
        else:
            print("Nie stac cie na kredyt, potrzebujesz 10001zł.")
    except ValueError:
        print("Wpisz liczbe")

def pozyczka():
    global pieniadze
    global dlug
    global rrso_pozyczka
    global tax_trans
    try:
        if (pieniadze < 100):
            mozliwosci = [500, 1000, 2500, 10000]
            print("Ile chcesz pozyczyc? (500, 1000, 2500, 10000)")
            ilosc = int(input("Chce pozyczyc: "))
            if (ilosc in mozliwosci):
                print(f"Ok, RRSO to {rrso_pozyczka}%")
                pieniadze = pieniadze + ilosc
                dlug = dlug + (ilosc * (rrso_pozyczka / 100 + 1))
                tax_trans += 1
                print(f"Twoj aktualny dlug to: {round(dlug)}\n")
            else:
                print("Nie mozesz wyplacic takiej kwoty\n")
        else:
            print("Ale po co ci pozyczka, idz wydaj to w kasynie\n")
    except ValueError:
        print("Wpisz liczbe")

def zmien_szanse():
    global szansa
    global realna_szansa
    global tax_trans
    if (500 <= realna_szansa <= 1000):
        szansa = round(szansa - 5)
        realna_szansa = round(realna_szansa - 5)
    elif (300 <= realna_szansa <= 499):
        szansa = round(szansa - 4)
        realna_szansa = round(realna_szansa - 4)
    elif (200 <= realna_szansa <= 299):
        szansa = round(szansa - 3)
        realna_szansa = round(realna_szansa - 3)
    elif (10 <= realna_szansa <= 199):
        szansa = round(szansa - 2)
        realna_szansa = round(realna_szansa - 2)
    else:
        szansa = round(szansa)      
        realna_szansa = round(realna_szansa)  
    tax_trans += 1

def praca():
    global pieniadze
    global tax_trans
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
    pieniadze_wypraconwane = random.randint(0, 1000)
    if (pieniadze_wypraconwane > 0):
        print(f"Ok masz pieniadze ({pieniadze_wypraconwane}zł)")
        pieniadze += pieniadze_wypraconwane
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
                pieniadze += 5000
            else:
                print("Nie udalo sie")
                if (pieniadze >= 500):
                    pieniadze -= 500
                else:
                    pieniadze = 0
        elif (odpowiedz == "nic"):
            print("Ok, pracodawca uciekl.")
    tax_trans += 1
                
def main():
    global pieniadze
    global dlug
    global tax_trans
    global realna_szansa
    try:
        while True:
            print(f"Pieniadze na kasyno: {round(pieniadze)}")
            if (dlug > 0):
                print(f"Masz dlug wynoszacy {round(dlug)} zlotych. Dlug bedzie automatycznie splacany w kwocie 2% długu przy kazdej transkacji.")
                if (pieniadze < (dlug * 0.02)):
                    print("Nie masz pieniedzy na splacenie dlugu, wypozycz wiecej albo sie pozegnaj z mieszkaniem")
                else:
                    pieniadze = pieniadze * 0.98
                    splacono = pieniadze * 0.02
                    dlug = dlug - splacono
                    print("Pomyslnie splacono 2% dlugu.")
                    # Bo nie chce mi sie pisac systemu spłacania
            if (tax_trans >= 30):
                tax_trans = 0
                if (pieniadze >= 100):
                    pieniadze -= pieniadze / 10
                    print(f"Zabrano podatek {round(pieniadze / 10)}zł. (więcej na inne)")
                else:
                    dlug = 1000
                    print("Nałożono dług 1000 złotych ze względu na brak wystarczającej ilości pieniędzy na koncie, by zapłacić podatki.")
            print("$$$ KASYNO $$$")
            print(f"Masz szanse 1/{szansa}")
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
                        if ((pieniadze - 300) < 0):
                            print("Nie stac cie")
                        else:    
                            print("Ok")
                            pieniadze -= 300
                            zmien_szanse()
                    elif (co == "pozyczka"):
                        print("Ok")
                        pozyczka()
                    elif (co == "kredyt"):
                        print("Ok")
                        kredyt()
                    else:
                        print("ok")
                        break
            elif (liczba == "wyjdz"):
                quit()
            elif (liczba == "gry"):
                while True:
                    print("Wpisz 'blackjack' by zagrac w blackjacka (250zl)")
                    print("Wpisz 'ruletka' by zagrac w ruletke (250zl)")
                    co = input(": ")
                    if (co == "blackjack"):
                        blackjack()
                    elif (co == "ruletka"):
                        ruletka()
                    else:
                        print("ok")
                        break
            elif (liczba == "inne"):
                while True:
                    print("Wpisz 'oddaj' by oddac pieniadze w rece panstwowe")
                    print("Wpisz 'praca' by pracowac")
                    print("Wpisz 'podatki' by zobaczyc informacje o podatkach.")
                    co = input(": ")
                    if (co == "oddaj"):
                        print("Oj tak")
                        oddaj()
                    elif (co == "praca"):
                        praca()
                    elif (co == "podatki"):
                        print("""
Podatki zabierają ci 10% twojego stanu bankowego co 30 transakcji. 
Sprawdzenie informacji o podatkach NIE liczy się jako transakcja.
W momentu niskiego stanu konta, państwo nałoży dług w ilości 1000 złotych.
""")
                    else:
                        print("ok")
                        break
            else:
                time.sleep(1)
                print("Procesuje liczbe czekaj")
                if (pieniadze >= 100):
                    time.sleep(1)
                    print("Dobra\n")
                    time.sleep(1)
                    if(random.randint(1, realna_szansa) != (round(realna_szansa * 0.84))):
                        print("Oj niestety nie wygrales przykro mi")
                        pieniadze -= 100
                    else:
                        print("O KURDE JACKPOT")
                        pieniadze = pieniadze + 100000
                        realna_szansa += 50
                    tax_trans += 1
                else:
                    print("Nie stac cie juz wiecej na kasyno, wez pozyczke w sklepie")
    except KeyboardInterrupt:
        print("Nie nie wychodzisz z kasyna")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

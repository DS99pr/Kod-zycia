import time
import random

pieniadze = 5000
realna_szansa = 1000
szansa = 1000
dlug = 0
rrso = 20
def blackjack():
    global pieniadze
    if (pieniadze >= 250):
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

def oddaj():
    global pieniadze
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
                   print("Dziekujemy za wplate.\n")
    except ValueError:
        print("Wpisz liczbe")

def pozyczka():
    global pieniadze
    global dlug
    global rrso
    try:
        if (pieniadze < 100):
            mozliwosci = [500, 1000, 2500, 10000]
            print("Ile chcesz pozyczyc? (500, 1000, 2500, 10000)")
            ilosc = int(input("Chce pozyczyc: "))
            if (ilosc in mozliwosci):
                print(f"Ok, RRSO to {rrso}%")
                pieniadze = pieniadze + ilosc
                dlug = dlug + (ilosc * (rrso / 100 + 1))
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

def praca():
    global pieniadze
    print("Pracujesz wiec teraz msuisz poczekac 10 sekund na peiniadze")
    time.sleep(10)
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
                

def main():
    global pieniadze
    global dlug
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
            print("$$$ KASYNO $$$")
            print(f"Masz szanse 1/{szansa}")
            print("Wybierz sobie liczbe bo to kasyno i jak zgadniesz liczbe 0-9 to wygrasz pieniadze")
            liczba = input("Jaka? (wpisz sklep by coś kupic): ")
            if (liczba == "sklep"):
                while True:
                    print("Witaj w sklepie")
                    print("Wpisz 'szansa' by zwiekszyc swoja szanse w kasynie o 0.5% (za 300zl)")
                    print("Wpisz 'pozyczka' by pozyczyc pieniadze")
                    print("Wpisz 'oddaj' by oddac pieniadze w rece panstwowe")
                    print("Wpisz 'praca' by pracowac")
                    print("Wpisz 'blackjack' by zagrac w blackjacka (250zl)")
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
                    elif (co == "oddaj"):
                        print("Oj tak")
                        oddaj()
                    elif (co == "praca"):
                        praca()
                    elif (co == "blackjack"):
                        blackjack()
                    else:
                        print("ok")
                        break
            elif (liczba == "wyjdz"):
                quit()
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
                else:
                    print("Nie stac cie juz wiecej na kasyno, wez pozyczke w sklepie")
    except KeyboardInterrupt:
        print("Nie nie wychodzisz z kasyna")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

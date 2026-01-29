import time
import random

pieniadze = 5000
szansa = 1000
dlug = 0
rrso = 20
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
                print(f"Twoj aktualny dlug to: {dlug}\n")
            else:
                print("Nie mozesz wyplacic takiej kwoty\n")
        else:
            print("Ale po co ci pozyczka, idz wydaj to w kasynie\n")
    except ValueError:
        print("Wpisz liczbe")

def zmien_szanse():
    global szansa
    szansa = round(szansa - 5)

def praca():
    print("Pracujesz wiec teraz msuisz poczekac 24 sekundy na peiniadze")
    time.sleep(24)
    print("Ok masz pieniadze")
    pieniadze += 150

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
            print("Kasyno")
            print("Wybierz sobie liczbe bo to kasyno i jak zgadniesz liczbe 0-9 to wygrasz pieniadze")
            liczba = input("Jaka? (wpisz sklep by coś kupic): ")
            if (liczba == "sklep"):
                while True:
                    print("Witaj w sklepie")
                    print("Wpisz 'szansa' by zwiekszyc swoja szanse w kasynie o 0.5% (za 300 monet)")
                    print("Wpisz 'pozyczka' by pozyczyc pieniadze")
                    print("Wpisz 'oddaj' by oddac pieniadze w rece panstwowe")
                    print("Wpisz 'praca' by pracowac")
                    co = input(": ")
                    if (co == "szansa"):
                        if (pieniadze - 300 <= 0):
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
                    if(random.randint(1, szansa) != (round(szansa * 0.84))):
                        print("Oj niestety nie wygrales przykro mi")
                        pieniadze -= 100
                    else:
                        print("O KURDE JACKPOT")
                        pieniadze = pieniadze + 100000
                else:
                    print("Nie stac cie juz wiecej na kasyno, wez pozyczke w sklepie")
    except KeyboardInterrupt:
        print("Nie nie wychodzisz z kasyna")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

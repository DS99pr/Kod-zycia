import time
import random
def main():
    pieniadze = 500
    try:
        while True:
            print(f"Pieniadze na kasyno: {pieniadze}")
            print("Ten kod odmieni twoje zycie")
            print("Kasyno")
            print("Wybierz sobie liczbe bo to kasyno i jak zgadniesz liczbe 0-9 to wygrasz pieniadze")
            input("Jaka?: ")
            time.sleep(1)
            print("Procesuje liczbe czekaj")
            time.sleep(1)
            print("Dobra\n")
            time.sleep(1)
            if(random.randint(1, 10000) != 853):
                print("Oj niestety nie wygrales przykro mi")
                pieniadze -= 100
            else:
                print("Udalo ci sie tym razem xd")
                pieniadze += 1000
    except ValueError:
        print("No masz liczbe wpisac xdd")
    except KeyboardInterrupt:
        print("Nie nie wychodzisz z kasyna")

if (__name__ == "__main__"):
    main()
# Mam nadzieje ze ten kod odmienil twoje zycie jesli nie to przecyztaj readme zlodzieju nieczysty

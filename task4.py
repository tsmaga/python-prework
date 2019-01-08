import random
Gracz=False
GraczWynik = 0
KomputerWynik = 0
while Gracz == False:

    Gracz = input("Wybierz figurę: (P)apier, (K)amień, (N)ozyce")
    Komputer = random.choice(['P', 'K', 'N'])

    if Gracz == Komputer:
        print('Remis!')
    elif Gracz == 'P' and Komputer == 'K':
        print("Gracz: Papier\n"
              "Komputer: Kamień")
        print('+--------------+\n'
              '|Gracz wygrywa!|\n'
              '+ -------------+')
        GraczWynik+=1
    elif Gracz == 'P' and Komputer == 'N':
        print("Gracz: Papier\n"
              "Komputer: Nożyce")
        print('+----------------+\n'
              '|Komputer wygrywa|\n'
              '+----------------+')
        KomputerWynik +=1
    elif Gracz == 'K' and Komputer =='P':
        print("Gracz: Kamień\n"
              "Komputer: Papier")
        print('+----------------+\n'
              '|Komputer wygrywa|\n'
              '+----------------+')
        KomputerWynik +=1
    elif Gracz == 'K' and Komputer == 'N':
        print("Gracz: Kamień\n"
              "Komputer: Nożyce")
        print('+--------------+\n'
              '|Gracz wygrywa!|\n'
              '+ -------------+')
        GraczWynik +=1
    elif Gracz =='N' and Komputer =='P':
        print("Gracz: Nożyce\n"
              "Komputer: Papier")
        print('+--------------+\n'
              '|Gracz wygrywa!|\n'
              '+ -------------+')
        GraczWynik +=1
    elif Gracz == 'N' and Komputer == 'K':
        print("Gracz: Nożyce\n"
              "Komputer: Kamień")
        print('+----------------+\n'
              '|Komputer wygrywa|\n'
              '+----------------+')
        KomputerWynik+=1
    else:
        print("To nie jest poprawna zagrywka, wybierz figurę: (P)apier, (K)amień, (N)ozyce:")
    print("Aktualny wynik: Gracz {} : {} Komputer".format(GraczWynik, KomputerWynik))

    Dalej = input('Czy chcesz grać dalej? t/n')
    if Dalej == 't':
        Gracz=False
    else Dalej == 'n':
        print("Koniec gry!")
        break


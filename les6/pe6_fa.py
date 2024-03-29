kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
aantalkluizen = int((len(kluizen)))
aantalBezetteKluizen = sum(1 for line in open('kluizen.txt'))
menuKeuze = 0


def toon_aantal_kluizen_vrij():
    vrijeKluisjes = aantalkluizen - aantalBezetteKluizen
    return vrijeKluisjes

def nieuwe_kluis():
    with open('kluizen.txt', 'r+') as f:
        for line in f:
            line = line.split(';')
            kluizen.remove(int(line[0])) # herontdekken
        if kluizen:# betere naamgeving
            kluisNummer = kluizen[0]
            kluisCode = input("Kies uw code:")
            statusBericht = "Uw kluis is " + str(kluisNummer)
            f.write('\n' + str(kluisNummer) + ';' + str(kluisCode))
            f.close()
        else:
            statusBericht = ("Er zijn geen momenteel geen kluizen beschikbaar.")
            #sluit file
        return statusBericht


def kluis_openen(opgegevenNummer, opgegevenCode):
    kluisCombinatie = str(opgegevenNummer) + ';' + str(opgegevenCode)
    with open("kluizen.txt") as f:
        for line in f:
            line = line.rstrip()
            if kluisCombinatie == line:
                print("kluis is geopend")
                #sluit file
    return


while menuKeuze != 4:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn \n2: Ik wil een nieuwe kluis \n3: Ik wil even iets uit mijn kluis halen \n4: Afsluiten')
    menuKeuze = input("Maak uw keuze:")

    try:
        menuKeuze = int(menuKeuze)
    except ValueError:
        print('Ongeldige waarde, kies graag een nummer uit het menu')
        continue

    if menuKeuze == 1:
        print(toon_aantal_kluizen_vrij())
    elif menuKeuze == 2:
        print(nieuwe_kluis())
    elif menuKeuze == 3:
        opgegevenNummer = input("Geef uw kluis nummer op:")
        opgegevenCode = input("Geef uw kluis code op:")
        kluis_openen(opgegevenNummer, opgegevenCode)
    elif menuKeuze == 4:
        print("Programma wordt afgesloten")
    else:
        print('Ongeldige optie, kies graag een nummer uit het menu')



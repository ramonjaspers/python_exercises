import datetime

weekDeel = datetime.datetime.today().weekday()
basisAfstandKilometerTarief = 0.80
grootteAfstandKilometerTarief = 0.60
kilometerDrempelPrijs = 15
jongEnOudWeekendKorting = 0.65
jongEnOudweekKorting = 0.7
weekendKorting = 0.60
jongeKortingsLeeftijd = 12
oudeKortingsLeeftijd = 65
isHetNuWeekend = weekDeel > 4

def standaardprijs(afstandKM):
    totaalprijs = 0
    if afstandKM < 50:
        totaalprijs = (afstandKM * basisAfstandKilometerTarief)
    elif afstandKM >= 50:
        totaalprijs = kilometerDrempelPrijs + (afstandKM * grootteAfstandKilometerTarief)
    return totaalprijs


def ritprijs(leeftijd, isHetEenRitInHetWeekend, afstandKM):
    totaalprijs = standaardprijs(afstandKM)
    heeftRechtOpLeeftijdKorting = leeftijd < jongeKortingsLeeftijd or leeftijd >= oudeKortingsLeeftijd
    if heeftRechtOpLeeftijdKorting and isHetEenRitInHetWeekend:
        eindprijs = totaalprijs * jongEnOudWeekendKorting
    elif heeftRechtOpLeeftijdKorting and not isHetEenRitInHetWeekend:
        eindprijs = totaalprijs * jongEnOudweekKorting
    elif isHetEenRitInHetWeekend:
        eindprijs = totaalprijs * weekendKorting
    else:
        eindprijs = totaalprijs
    return eindprijs


# kilometers = float(input("Geef het aantal kilometers op: "))
# leeftijd = float(input("Geef je leeftijd op: "))
# print(ritprijs(leeftijd,isHetNuWeekend, kilometers))

leeftijden = [11, 12, 64, 65]
afstanden = [20, 40, 60]
for leeftijd in leeftijden:
    for afstand in afstanden:
        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Weekdagen: ' + str(ritprijs(leeftijd, False, afstand)) + ' euro')
        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Weekend: ' + str(ritprijs(leeftijd, True, afstand)) + ' euro')
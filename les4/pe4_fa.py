import datetime

weekDeel = datetime.datetime.today().weekday()
basisAfstandKilometerTarief = 0.80
grootteAfstandKilometerTarief = 0.60
kilometerDrempelPrijs = 15
jongEnOudWeekendKorting = 0.65
jongEnOudweekKorting = 0.7
weekendKorting = 0.60
weekendRit = bool

if weekDeel <= 4:
    weekendRit = False
else:
    weekendRit = True

def standaardprijs(afstandKM):
    if afstandKM < 50:
        totaalprijs = (afstandKM * basisAfstandKilometerTarief)
    elif afstandKM >= 50:
        totaalprijs = kilometerDrempelPrijs + (afstandKM * grootteAfstandKilometerTarief)
    elif afstandKM <= 0:
        totaalprijs = 0
    return totaalprijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    totaalprijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
        eindprijs = totaalprijs * jongEnOudWeekendKorting
    elif leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        eindprijs = totaalprijs * jongEnOudweekKorting
    elif weekendrit == True:
        eindprijs = totaalprijs * weekendKorting
    else:
        eindprijs = totaalprijs
    return eindprijs


# kilometers = float(input("Geef het aantal kilometers op: "))
# leeftijd = float(input("Geef je leeftijd op: "))
#
# print (ritprijs(leeftijd, weekendRit, kilometers))


leeftijden = [11, 12, 64, 65]
afstanden = [20, 40, 60]

for leeftijd in leeftijden:
    for afstand in afstanden:
        print(str(leeftijd) + ' Jaar oud | ' + str(afstand) + 'KM | Weekend: ' + str(ritprijs(leeftijd, True, afstand)) + ' euro')
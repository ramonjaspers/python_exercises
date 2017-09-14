def standaardtarief(Standaardbedrag):



def standaardprijs(afstandKM):
    treinrit = 0.80
    kilometerverhoging = 0.60
    kilometerdrempelprijs = 15
    totaalprijs = treinrit + (afstandKM * kilometerverhoging)
    if afstandKM >= 50:
        totaalprijs + kilometerdrempelprijs
    elif afstandKM <= 0:
        totaalprijs = 0
    return totaalprijs


def ritprijs(leeftijd, weekendrit, afstandKM):

import math
def kwadraten_som(grondgetallen):
    totaal = 0
    for getal in grondgetallen:
        if getal >= 0:
            totaal += getal * getal
    return totaal



getallenLijst = [4, 5, 3, -81]

print(kwadraten_som(getallenLijst))


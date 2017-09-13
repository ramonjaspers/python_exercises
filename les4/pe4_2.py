def som(getallen):
    totaal = 0
    for getal in getallen:
        totaal = totaal + getal
    return totaal

getallenLijst = (2, 2, 3, 4)

print(som(getallenLijst))
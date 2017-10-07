stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Heerhugowaard', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', '\'s-Hertogenbosch', 'Utrecht Centraal', 'Eindhoven', 'Weert,',
            'Roermond', 'Sittard', 'Maastricht']

beginstationInput = ""
eindstationInput = ""

def inlezen_beginstation(stationslijst):
    beginstation = input("Voer het station van vertrek in:")
    if beginstation in stationslijst:
        while beginstation == "Maastricht":
            print("U kunt niet vanaf dit station vertrekken")
            beginstation = input("Voer het station van vertrek in:")
        return beginstation
    else:
        print("Het opgegeven station bestaat niet.")
        inlezen_beginstation(stationslijst)

def inlezen_eindstation(stationslijst, beginstation):
    eindstation = input("Voer het eind station in:")
    beginstationindex = stationslijst.index(beginstation)
    if eindstation in stationslijst:
        eindstationindex = stationslijst.index(eindstation)
        while eindstationindex < beginstationindex:
            print("Deze trein komt niet in " + eindstation + ".")
            eindstation = input("Voer het eind station in:")  # MAASTRICHT > MAASTRICHT > SCHAGEN > FOUTIEF
            eindstationindex = stationslijst.index(eindstation)
        return eindstation
    else:
        print(eindstation + "komt niet voor in dit traject.")
        inlezen_eindstation(stationslijst, beginstation)


def omroepen_reis(stationslijst, beginstation, eindstation):
    beginstationnummer = stationslijst.index(beginstation) + 1
    eindstationnummer = stationslijst.index(eindstation) + 1
    haltes = eindstationnummer - beginstationnummer
    kosten = haltes * 5
    print("\nHet beginstation " + str(beginstation) + " is het " + str(beginstationnummer) + "e station in het traject")
    print("Het eindstation " + str(eindstation) + " is het " + str(eindstationnummer) + "e station in het traject")
    print("De afstand bedraagt " + str(haltes) + " stations(s)")
    print("De prijs van het kaartje is " + str(kosten) + " euro\n")
    print("Jij stapt in de trein in: " + beginstation)
    for station in stationslijst[beginstationnummer:eindstationnummer - 1]:
        print("-" + station)
    print("Jij stapt uit in: " + eindstation)



while beginstationInput == eindstationInput:
    beginstationInput = inlezen_beginstation(stations)
    eindstationInput = inlezen_eindstation(stations, beginstationInput)
omroepen_reis(stations, beginstationInput, eindstationInput)

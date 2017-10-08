import xmltodict

with open('stations.xml') as f:
    doc = xmltodict.parse(f.read())

print("Dit zijn de codes en types van de 4 stations:")
for station in doc['Stations']['Station']:
    code = (station['Code'])
    soort = (station['Type'])
    print(str(code) + " - " + str(soort))

print("\nDit zijn alle stations met één of meer synoniemen:")
for station in doc['Stations']['Station']:
    code = (station['Code'])
    synoniem = (station['Synoniemen'])
    if synoniem:
        print(str(str(code) + " - " + str(synoniem['Synoniem'])))
    else:
        break

print("\nDit is de lange naam van elk station:")
for station in doc['Stations']['Station']:
    code = (station['Code'])
    lang = (station['Namen']['Lang'])
    print(str(code) + "- " + str(lang))

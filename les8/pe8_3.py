def code(invoerstring):
    beveiligdeString= ""
    for letter in invoerstring:
        rangOrder = ord(letter)
        letterNumber = rangOrder+3
        beveiligdeLetter =(str(chr(letterNumber)))
        beveiligdeString += beveiligdeLetter
    return beveiligdeString



gebruikerNaam = input("Voer uw naam in:")
beginStation = input("Voer het station van vertrek in:")
eindStation = input("Voer het eind station in:")

klantInfo = str(gebruikerNaam+beginStation+eindStation)

print(code(klantInfo))

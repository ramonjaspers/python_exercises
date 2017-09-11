cijferICOR = 6
cijferPROG = 8
cijferCSN = 7


beloning = (cijferCSN + cijferPROG + cijferICOR) * 30
gemiddelde = (cijferCSN + cijferPROG + cijferICOR)/3
overzicht = 'Het gemiddelde cijfer ='+ str(gemiddelde) +'De totale beloning='+ str(beloning)

print(beloning)
print(gemiddelde)
print(overzicht)
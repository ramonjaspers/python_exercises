Age = float(input("Geef je leeftijd op: "))
Pass = input("Heb je een Nederlands paspoort:")
if Age >= 18 and Pass == "ja":
    print ('Gefeliciteerd, je mag stemmen!!')
else:
    print ('Helaas je mag nog niet stemmen')

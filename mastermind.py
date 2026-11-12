import random as rand

#Skriver reglerna
print(f"Datorn kommer att slumpa en kod på fyra siffror mellan 1 och 6.\nDu ska försöka gissa denna kods siffror på max 12 drag.")
print(f"Efter respektive gissning så kommer du få en respons:\nFör varje korrekt siffra på korrekt plats:y \nFör varje korrekt gissning på fel plats:x \nFör de siffror som inte finns med i koden ges ingen markering")


#Låter dig välja svårighetsgrad
while True:
    try:
        svårighet = int(input("Ange önskad nivå: Lättare (1), Svårare (2) ->"))
        if svårighet in [1, 2]:
            break
        else:
            print("Ogiltigt val, Försök igen!")
    except ValueError:
        print("Ogiltigt val, Försök igen!")
        continue


#Slumpar en kod baserat på svårighetsgraden
kod = []
if svårighet == 1:
    while len(kod) < 4:
        siffra = rand.randint(1,6)
        if siffra not in kod:
            kod.append(siffra)
elif svårighet == 2:
    for i in range(4):
        kod.append(rand.randint(1, 6))


#Själva spelet
alla_gissningar = []
alla_responser = []
while True:
    respons = []
    gissning = input("Ange gissning som följd av fyra siffror --> ")
    print(f"\nDrag #", " "*4, "Drag", " "*7, "Feedback\n", "-"*32)
    
    #Jämför din gissning mit koden
    for i in range(4):
        if int(gissning[i]) == kod[i]:
            respons.append("y")
        elif int(gissning[i]) in kod:
            respons.append("x")
    
    # Lägger till mellanslag mellan siffrorna och svaren med vanliga loopar
    gissning_text = ""
    for siffra in gissning:
        gissning_text = gissning_text + siffra + " "
    respons_text = ""
    for bokstav in respons:
        respons_text = respons_text + bokstav + " "     
    alla_gissningar.append(gissning_text)
    alla_responser.append(respons_text)
    
    # Skriver ut spelplanen rad för rad (12 ner till 1)
    print("Drag #", " "*3, "Drag", " "*7, "Feedback")
    print("-" * 34)
    for rad in range(12, 0, -1):
        print()
        if rad >= 10:
            rad_text = "  " + str(rad)
        else:
            rad_text = "   " + str(rad)     
        if rad <= len(alla_gissningar):
            print(rad_text + "     " + alla_gissningar[rad - 1] + "    " + alla_responser[rad - 1])
        else:
            print(rad_text)
    
    #Slutar spelet om du har alla rätt
    if respons == ["y", "y", "y", "y"]:
        print("Du vann")
        break
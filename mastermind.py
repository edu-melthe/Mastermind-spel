import random as rand

print(f"Datorn kommer att slumpa en kod på fyra siffror mellan 1 och 6.\nDu ska försöka gissa denna kods siffror på max 12 drag.")
print(f"Efter respektive gissning så kommer du få en respons:\nFör varje korrekt siffra på korrekt plats:y \nFör varje korrekt gissning på fel plats:x \nFör de siffror som inte finns med i koden ges ingen markering")

kod = []
for i in range(4):
    kod.append(rand.randint(0, 6))

print(kod)

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
    

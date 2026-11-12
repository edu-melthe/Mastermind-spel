import random as rand

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
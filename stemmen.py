
stemmen_jef = 0
stemmen_martino = 0

print("Welkom bij de verkiezingen van Florijnia!")
print("Je kunt stemmen op jef of martino.")
print("Type 'UITSLAG' om de stemmen te stoppen en de winnaar te zien.\n")

stem = input("Op wie wil je stemmen? ")

while stem != 'UITSLAG':

    if stem.lower() == 'jef':
        stemmen_jef += 1
    elif stem.lower() == 'martino':
        stemmen_martino += 1
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

    stem = input("Op wie wil je stemmen? ")

# Bepalen van de winnaar op basis van het aantal stemmen
if stemmen_omer > martino:
    print("Omer heeft gewonnen!")
elif stemmen_martino > stemmen_jef:
    print("martino heeft gewonnen!")
else:
    print("Het is een gelijkspel!")

input('Press ENTER to exit')


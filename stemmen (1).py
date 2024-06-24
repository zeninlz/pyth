
stemmen_omer = 0
stemmen_mehmet = 0

print("Welkom bij de verkiezingen van Florijnia!")
print("Je kunt stemmen op Omer of Mehmet.")
print("Type 'UITSLAG' om de stemmen te stoppen en de winnaar te zien.\n")

stem = input("Op wie wil je stemmen? ")

while stem != 'UITSLAG':

    if stem.lower() == 'omer':
        stemmen_omer += 1
    elif stem.lower() == 'mehmet':
        stemmen_mehmet += 1
    else:
        print("Ongeldige keuze. Probeer opnieuw.")

    stem = input("Op wie wil je stemmen? ")

# Bepalen van de winnaar op basis van het aantal stemmen
if stemmen_omer > stemmen_mehmet:
    print("Omer heeft gewonnen!")
elif stemmen_mehmet > stemmen_omer:
    print("Mehmet heeft gewonnen!")
else:
    print("Het is een gelijkspel!")

input('Press ENTER to exit')


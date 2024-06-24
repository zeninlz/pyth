score_speler1 = int(input("Voer de score van speler 1 in: "))

score_speler2 = int(input("Voer de score van speler 2 in: "))

if score_speler1 > score_speler2:
    print("Speler 1 heeft gewonnen!")
elif score_speler2 > score_speler1:
    print("Speler 2 heeft gewonnen!")
else:
    print("Het is een gelijkspel!")

input('Press ENTER to exit')
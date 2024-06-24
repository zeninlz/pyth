
def bereken_product(a, b):
    return a * b

getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))

resultaat = bereken_product(getal1, getal2)

print(f"Het product van {getal1} en {getal2} is: {resultaat}")

input('Press ENTER to exit')
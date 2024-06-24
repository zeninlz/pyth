
hobbies = []

for i in range(3):
    hobby = input(f"wat is jouw hobby {i+1}: ")
    hobbies.append(hobby)

print("Jouw hobby's zijn:")
for hobby in hobbies:
    print(hobby)

with open('output.txt', 'w') as file:
    for hobby in hobbies:
        file.write(hobby + '\n')

print("De hobby's zijn opgeslagen in het bestand 'output.txt'.")

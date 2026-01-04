# Étape 4 : enumerate()
fruits = ["pomme", "banane", "cerise"]

for index, fruit in enumerate(fruits):
    print(f"{index} → {fruit}")

# Début de l'index à 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} → {fruit}")

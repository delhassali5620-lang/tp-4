# lab6_notes.py

# Étape 1 : Validation d'une note
seuil = 10  # seuil d'admission

try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide.")
    exit(1)

if note >= seuil:
    print("Admis")
else:
    print("Refusé")

print("\n--- Boucle while pour messages ---")
# Étape 2 : Répéter une action avec while
mot_cle = "stop"
message = ""

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")
    if message.lower() != mot_cle and message != "":
        print(f"Vous avez saisi : {message}")

print("Boucle terminée, mot-clé détecté.\n")

# Étape 3 : Parcourir une séquence avec for et range()
print("--- Affichage nombres de 1 à 5 ---")
for i in range(1, 6):
    print(f"Nombre {i}")

print("--- Affichage nombres pairs de 0 à 8 ---")
for i in range(0, 10, 2):
    print(i)

print("--- Compte à rebours de 5 à 1 ---")
for i in range(5, 0, -1):
    print(i)

# Étape 4 : Utiliser enumerate() pour index + valeur
fruits = ["pomme", "banane", "cerise"]
print("\n--- Liste de fruits avec index ---")
for index, fruit in enumerate(fruits):
    print(f"{index} → {fruit}")

print("\n--- Liste de fruits avec index à partir de 1 ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} → {fruit}")

# Étape 5 : Combiner les concepts
print("\n--- Saisie multiple de notes et statut ---")
notes = []

while True:
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree)
        notes.append(note)
    except ValueError:
        print("Valeur incorrecte, merci d'entrer un nombre.")

for index, note in enumerate(notes, start=1):
    statut = "Admis" if note >= seuil else "Refusé"
    print(f"Étudiant {index} : note {note} → {statut}")

# Étape 6 : Idées d'extension (exemple moyenne)
if notes:
    moyenne = sum(notes)/len(notes)
    print(f"\nMoyenne de la classe : {moyenne:.2f}")
    if moyenne >= seuil:
        print("Classe globalement admise")
    else:
        print("Classe globalement en échec")

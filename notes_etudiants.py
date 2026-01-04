# Étape 5 : Combiner while + for + if

seuil = 10
notes = []

while True:
    entree = input("Entrez une note ou 'stop' : ").strip()
    if entree.lower() == "stop":
        break
    try:
        note = float(entree)
        if note < 0 or note > 20:
            print("Note hors plage")
            continue
        notes.append(note)
    except ValueError:
        print("Valeur incorrecte, merci d'entrer un nombre.")

for index, note in enumerate(notes, start=1):
    statut = "Admis" if note >= seuil else "Refusé"
    print(f"Étudiant {index} : note {note} → {statut}")

# lab4_flux.py - Étape 1 : Validation d'une note

seuil = 10  # note minimale pour être admis

try:
    note = float(input("Entrez la note de l'étudiant : "))
except ValueError:
    print("Saisie invalide.")
    exit(1)

if note >= seuil:
    print("Admis")
else:
    print("Refusé")

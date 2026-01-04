# Étape 2 : boucle while avec mot-clé
mot_cle = "stop"
message = ""

while message.lower() != mot_cle:
    message = input("Tapez un message (ou 'stop' pour quitter) : ")
    if message.lower() != mot_cle and message != "":
        print(f"Vous avez saisi : {message}")

print("Boucle terminée, mot-clé détecté.")

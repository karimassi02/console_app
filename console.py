import datetime

def est_palindrome(chaine):
    # Supprimer les espaces et mettre en minuscules pour la comparaison
    chaine = chaine.replace(" ", "").lower()
    return chaine == chaine[::-1]

def au_revoir():
    heure_actuelle = datetime.datetime.now().hour
    if 6 <= heure_actuelle < 18:
        print("Au revoir!")
    else:
        print("Bonne nuit!")

def miroir(chaine):
    # Retourne le texte en miroir
    return chaine[::-1]

def main():
    # Obtenir l'heure actuelle
    heure_actuelle = datetime.datetime.now().hour

    # Dire Bonjour ou Bonsoir selon l'heure
    if 6 <= heure_actuelle < 18:
        print("Bonjour!")
    else:
        print("Bonsoir!")

    # Demander une saisie à l'utilisateur
    while True:
        saisie = input("Saisissez un mot ou une phrase (ou tapez 'q' pour sortir) : ")
        if saisie.lower() == "q":
            au_revoir()
            break

        # Affiche le texte en miroir
        texte_miroir = miroir(saisie)
        print(f"{texte_miroir}")

        # Vérifie si c'est un palindrome
        if est_palindrome(saisie):
            print("Bien dit !")

if __name__ == "__main__":
    main()

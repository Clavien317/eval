def Expert(experience):
    print("Années d'expérience fournies :", experience)
    
    # Trouver le premier maximum
    premier_max = max(experience)
    # Trouver le deuxième maximum après avoir temporairement enlevé le premier maximum
    experience_sans_premier_max = experience.copy()
    experience_sans_premier_max.remove(premier_max)
    deuxieme_max = max(experience_sans_premier_max)
    
    print("Les deux plus experts sont : [", experience.index(premier_max), ",", experience.index(deuxieme_max), "]")
    
    moins_expert = min(experience)
    print("Le moins expert est : [", experience.index(moins_expert), ",", experience.index(moins_expert), "]")

def PairDev(nbre):
    experience = []
    if nbre % 2 == 0:
        for _ in range(nbre):
            annee = int(input("Entrer année d'expérience : "))
            experience.append(annee)
        print("Années d'expérience fournies :", experience)
        Expert(experience)
    else:
        print("Le nombre d'années d'expérience doit être pair.")

nbre = int(input("Combien d'années d'expérience entrez-vous? \n"))
PairDev(nbre)

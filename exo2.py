

def Expert(experience):
    print(experience)
    plus = max(experience)
    # experience.pop(plus)
    deuxiem = max(experience)
    print("Le plus expert est : [",experience.index(plus),",",experience.index(deuxiem),"]")
    moins = min(experience)
    print("Le moins expert est : [",experience.index(moins),",",experience.index(moins),"]")

def PairDev(nbre):
    experience=[]
    if(nbre%2 ==0):
        while (nbre>0):
            nbre=nbre-1
            annee = int(input("Entrer annee d'exp : "))
            experience.append(annee)
        print(experience)
        Expert(experience)
    else:
        print("Non pair")


nbre = int(input("Combien annee entrez-vous? \n"))
PairDev(nbre)
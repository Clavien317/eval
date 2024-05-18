


def repeat():
    return True



def isValid(html):
    inf="<"
    sup=">"
    slac="/"
    for i in html:
        if(i !=slac):
            print("Code invalid...")
        else:
            if(inf in i):
                print("Ouverture ok")
            elif(sup in i):
                print("Fermeture ok")
            elif(slac in i):
                print("Slace pour fermee ok")
            else:
                print("Pas html...")
            # verify

            
balise = str(input("Entrer un code html : \n"))
isValid(balise)
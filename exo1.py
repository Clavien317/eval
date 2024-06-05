def isValid(html):
    tags = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = i + 1
            is_closing = False
            
            if j < len(html) and html[j] == '/':
                is_closing = True
                j += 1
            
            while j < len(html) and html[j] != '>':
                j += 1
            
            if j == len(html):
                print("Code invalid: '>' manquant")
                return False
            
            tag = html[i+1:j] if not is_closing else html[i+2:j]
            
            if not is_closing:
                tags.append(tag)
            else:
                if len(tags) == 0 or tags[-1] != tag:
                    print("Code invalid: balise fermante non correspondante")
                    return False
                tags.pop()
            
            i = j
        i += 1
    
    if len(tags) == 0:
        print("Code valid")
        return True
    else:
        print("Code invalid: balise(s) non fermée(s)")
        return False

balise = input("Entrer un code html : \n")
isValid(balise)

#### Imports et définition des variables globales


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: La liste des tuples (caractère, nombre d'occurrences consécutives).
    """
    if not s:
        return []
    
    result = []
    c = s[0]
    nb = 1

    for char in s[1:]:
        if char == c:
            nb += 1
        else:
            result.append((c, nb))
            c = char
            nb = 1
    
    # Ajouter la dernière séquence de caractères
    result.append((c, nb))
    
    return result



def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici

    # cas de base
    if(not s):
        return []
    # recherche nombre de caractères identiques au premier
    count = 1
    while count < len(s) and s[0] == s[count]:
        count += 1
    # appel récursif
    
    return [(s[0], count)] + artcode_r(s[count:])
    

#### Fonction principale


def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

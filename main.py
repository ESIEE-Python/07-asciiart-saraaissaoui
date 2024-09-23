"""
Ce module contient des fonctions pour compresser des chaînes de caractères et leurs tests unitaires.
"""

def artcode_i(s):
    """
    Compresse une chaîne de caractères en groupant les caractères identiques successifs.
    Retourne une liste de tuples où chaque tuple contient un caractère et son nombre 
    d'occurrences consécutives.
    """
    char_list = [s[0]]
    count_list = [1]
    n = len(s)
    for k in range(1, n):
        if s[k] == s[k-1]:
            count_list[-1] += 1
        else:
            char_list.append(s[k])
            count_list.append(1)
    return list(zip(char_list, count_list))

def artcode_r(s):
    """
    Fonction récursive pour compresser une chaîne de caractères.
    Retourne une liste de tuples où chaque tuple contient un caractère 
    et son nombre d'occurrences consécutives.
    """
    def rec2(s, char_list, count_list, k):
        if k == len(s):
            return list(zip(char_list, count_list))
        if s[k] == char_list[-1]:
            count_list[-1] += 1
        else:
            char_list.append(s[k])
            count_list.append(1)
        return rec2(s, char_list, count_list, k+1)

    return rec2(s, [s[0]], [1], 1)

# Tests
def test_artcode_i():
    """Test de la fonction artcode_i avec une chaîne de caractères spécifique."""
    assert artcode_i('MMMMaaacXolloMM') == [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1),
                                            ('l', 2), ('o', 1), ('M', 2)]

def test_artcode_r():
    """Test de la fonction artcode_r avec une chaîne de caractères spécifique."""
    assert artcode_r('MMMMaaacXolloMM') == [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1),
                                            ('l', 2), ('o', 1), ('M', 2)]

def main():
    """Affiche les résultats de l'exécution des fonctions artcode_i et artcode_r."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()

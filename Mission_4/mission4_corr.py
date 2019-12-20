def is_adn(s):
    """ pre : contient un chaine de caractères
        post : retourne true si la chaine de caractères est de l'adn
        et false dans le cas contraire
    """
    x = "ATGC"
    y = 0
    for i in s:
        s = i.upper()
        if s not in x or s == " ":
            y += 1
    if y == 0:
        return True
    else:
        return False


def positions(s, p):
    """ pre : donner 2 chaines de caractères avec la chaine s plus grande que la p
        post:retourner les occurences d'une chaine dans l'autre chaine
    """
    x = []
    s = s.upper()
    p = p.upper()
    if len(s) >= len(p):
        for i in range(len(s) - len(p) + 1):
            if p == s[i:len(p) + i]:
                x.append(i)
    print(x)


def distance_h(s1, s2):
    """ pre : donner 2 chaines d'ADN
        post: si les chaines sont de mêmes longueurs, la distance de hamming est retournée
            sinon, "None" est retourné.
    """
    d = 0
    if len(s1) != len(s2):
        return None
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return (print(d))


distance_h("atcaggac", "acaccgcc")


def plus_long_palindrome(x):
    """pre: recevoir une chaine de caractères
       post: afficher le palindrome le plus long de la chaine
     """
    palindrome = ""
    x = list(x)
    for i in range(len(x)):
        y1 = x[:i + 1]
        for j in range(len(x) - len(y1) + 1):
            y1 = x[j:len(y1) + j]
            if len(y1) == 0:
                palindrome = ""
            else:
                y2 = []
                for k in range(-1, -len(y1) - 1, -1):
                    y2.append(y1[k])
                if y1 == y2:
                    palindrome = y1
    print("".join(palindrome))


plus_long_palindrome("atcgatttagatcgatagaaaaaaaaaaaaaaaaaggctag")    
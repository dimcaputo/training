# ----------------
# Fonctions d'aide
# ----------------
def swap(tab, i, j):
    """Échange la place de deux éléments dans un tableau"""
    x = tab[i]
    y = tab[j]
    tab[i] = y
    tab[j] = x


# ---------------
# Tris classiques
# ---------------
def bubble_sort(tab):
    """Trie le tableau en déplaçant les plus grosses valeurs vers la fin du
    tableau, un peu comme des bulles dans l'eau qui remonteraient à la
    surface"""
    for i in range(len(tab)-1, 0, -1):
        for j in range(i):
            if tab[j+1] < tab[j]:
                swap(tab, j+1, j)


def insertion_sort(tab):
    """Trie le tableau en plaçant l'élément courant à la bonne place dans
    le sous-tableau déjà trié"""
    for i in range(1,len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = x


def selection_sort(tab):
    """Trie le tableau en cherchant le plus petit élément à mettre dans la
    première case, puis le second plus petit à mettre dans la seconde case,
    etc"""
    for i in range(len(tab)-1):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        if min != i:
            swap(tab, i, min)


# --------------
# Tris récursifs
# --------------
def merge_sort(tab):
    """Trie le tableau via le principe de « diviser pour mieux régner »
    avec l'intelligence du tri qui se trouve au moment de la fusion"""
    merge_sort_r(tab, 0, len(tab))
    
    #raise NotImplementedError

def merge_sort_r(tab, start, end):
    #raise NotImplementedError
    if start < end-1:
        middle = int((start+end)/2)
        merge_sort_r(tab, start, middle)
        merge_sort_r(tab, middle, end)
        merge(tab,start,middle,end)


def merge(tab, start, middle, end):
    #raise NotImplementedError
    temp = tab.copy()

    i=start
    j=middle
    for k in range(start, end):
        if i < middle and j < end:
            if tab[i] <= tab[j]:
                temp[k] = tab[i]
                i = i+1
            else:
                temp[k] = tab[j]
                j = j+1
        else :
            if i < middle:
                temp[k] = tab[i]
                i = i+1
            else:
                temp[k] = tab[j]
                j = j+1
    for k in range(start, end):
        tab[k] = temp[k]


def quick_sort(tab):
    """Divise le tableau en deux, trie chacune des sous-parties et fusionne
    intelligemment les deux sous-parties triées"""
    quick_sort_r(tab, 0, len(tab)-1)
    #raise NotImplementedError

def quick_sort_r(tab, first, last):
    #raise NotImplementedError
    if first < last:
        pivot = partition(tab,first,last)
        quick_sort_r(tab, first, pivot-1)
        quick_sort_r(tab, pivot+1, last)

        
def partition(tab, first, last):
    #raise NotImplementedError
    pivot = tab[first]
    i = first
    j = last
    while i <= j:
        if tab[i] <= pivot:
            i = i + 1
        else:
            if tab[j] > pivot:
                j = j - 1
            else:
                (tab[i],tab[j]) = (tab[j],tab[i])
    (tab[first], tab[j]) = (tab[j], tab[first])
    return j

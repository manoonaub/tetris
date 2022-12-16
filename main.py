def read_grid(path) : #qui retourne une grille valide lue à partir du contenu du fichier
    with open (path, "r") as f:
        grid = []
        for l in f:
            ligne = []
            for c in l:
                if c == "0":
                    ligne.append(0)
                if c == "1":
                    ligne.append(1)
                if c == "2":
                    ligne.append(2)

            grid.append(ligne)
        f.close()
        return grid

def print_grid(grid): #affichage de la grille
    for l in grid:
        for c in l:
          if c == 0:  # pas de blocs
              print(" ", end=" ")
          if c == 1: # case vide
              print(".", end=" ")
          if c == 2: #,case remplie
              print("□", end=" ")
        print()

def save_grid(path, grid) : #sauvegarde de le grille
    with open (path, "w") as f:
        for l in grid:
            for c in l:
                f.write(str(c))
                f.write(" ")
            f.write("\n")
        f.close()
#liste de tous les blocs
blocs_liste = [[[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
               [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0]],
                [[1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 1, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],],
                [[0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 0, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0],
                [1, 1, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0]],
                [[0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0]],
                [[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0]]]


triangle_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                                 24, 25, 26, 27, 28, 29, 30]
#liste des blocs pour le plateau triangle
cercle_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42]
#liste des blocs pour le plateau cercle
losange_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 43, 44, 45, 46, 47, 48, 49, 50,
                 51, 52, 53, 54, 55, 56]
#liste des blocs pour le plateau losange
def print_blocs(grid): #choix du plateau
    if grid == "triangle":
        for case in triangle_liste:
            print(blocs_liste[case])
    elif grid == "cercle":
        for case in cercle_liste:
            print(blocs_liste[case])
    elif grid == "losange":
        for case in losange_liste:
            print(blocs_liste[case])
    else:
        print("choissisez une forme valide")

def menu(): #menu
    print("MENU")
    print("1. commencer à jouer")
    print("2. règles du jeu")
    choix = int(input("Saisissez votre choix"))
    while choix != 1 and choix != 2:
        print("Ce n'est pas possible, veuillez réessayer")
        choix = int(input("Saisissez votre choix"))

    while choix==2: #règles du jeu
        print("regle du jeu")
        print("Lorsque le menu est affiché, vous devez taper 1 afin de commencer le jeu. ")
        print("Il vous sera alors proposé trois plateaux différents: le cercle,le triangle et le losange.")
        print("Ainsi après avoir choisi le plateaux, celui-ci s'affiche et 3 blocs vous sont présentés.")
        print("Le but de ce jeu est d'obtenir le score le plus élevé possible.")
        print("Pour ce faire vous devez placer les blocs de sorte à créer un maximum de lignes.")
        print("MENU")
        print("1. commencer à jouer")
        print("2. règles du jeu")
        choix = int(input("Saisissez votre choix"))
        while choix != 1 and choix != 2:
            print("Ce n'est pas possible, veuillez réessayer")
            choix = int(input("Saisissez votre choix"))
    if choix == 1: #choix du plateau
        print("1° cercle ")
        print("2° triangle")
        print("3° losange ")
        forme= int(input("Choissisez une forme"))
        while forme != 1 and forme != 2 and  forme != 3 :
            print("Ce n'est pas possible, veuillez réessayer")
            choix = int(input("Saisissez votre choix"))
        if forme == 1:
            plateau = "cercle"
            grid = plateau_cercle()
        elif forme == 2:
            plateau = "triangle"
            grid = plateau_triangle()
        elif forme == 3:
            plateau = "losange"
            grid = plateau_losange()
        print("1° Choisir parmi l'ensemble des blocs ")
        print("2° Choisir de manière aléatoire")
        blocs = int(input("Choissisez une forme"))
        while blocs != 1 and blocs != 2:
            print("Ce n'est pas possible, veuillez réessayer")
            choix = int(input("Saisissez votre choix"))
        if blocs == 1:
            suggestion_blocs = "ensemble"
        elif blocs == 2:
            suggestion_blocs = "aléatoire"

        print_grid(grid)

def plateau_losange(): #génération du plateau losange
    M=[]

    for i in range(21):
        liste=[]
        for l in range(21):
            if i<11:
                if  l>=10-i and l<=10+i:
                    liste.append(1)

                else:
                    liste.append(0)
            elif i>=11:
                if l>=i-10 and l<21-(i-10):
                    liste.append(1)
                else:
                    liste.append(0)
        M.append(liste)
    return M

def plateau_triangle(): #génération du plateau triangle
    M=[]

    for i in range(10):
        liste=[]
        for l in range(21):
            if i<11:
                if  l>=10-i and l<=10+i:
                    liste.append(1)
                else:
                    liste.append(0)
        M.append(liste)
    return M

def plateau_cercle(): #génération du plateau cercle
    M=[]

    for i in range(21):
        liste=[]
        for l in range(21):
            if i==0 or i==20:
                if l<3 or l>17:
                    liste.append(0)
                else:
                    liste.append(1)
            elif i==1 or i==19:
                if l<2 or l>18:
                    liste.append(0)
                else:
                    liste.append(1)
            elif i==2 or i==18:
                if l<1 or l>19:
                     liste.append(0)
                else:
                    liste.append(1)
            else:
                liste.append(1)
        M.append(liste)
    return M

def print_blocs(grid): #affichage des blocs en fonction du plateau
    compteur = 0
    for ligne in grid:
        for colonne in ligne:
            if colonne == 0:
                compteur = compteur + 1
    if compteur == 220:
        print(losange_liste)
    elif compteur == 60:
        print(cercle_liste)
    elif compteur == 110:
        print(triangle_liste)

#def select_bloc():



grid=read_grid("losange.txt")
#save_grid("tetris.txt", grid)
#print_blocs("cercle")
#plateau_cercle()
#print_blocs(grid)

print_blocs(grid)


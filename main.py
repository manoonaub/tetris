def read_grid(path) :
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

        return grid

def print_grid(grid):
    for l in grid:
        for c in l:
          if c == 0:
              print("  ", end=" ")
          if c == 1:
              print(".", end=" ")
          if c == 2:
              print("□", end=" ")
        print()

print_grid(read_grid("losange.txt"))

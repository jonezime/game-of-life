from tkinter import *
import tkinter.font as tkFont

# traitement du fichier de données en entrée
with open("datas.txt") as file:
    content = file.read().splitlines()
height = int(content[0])
width = int(content[1])
wrap = int(content[2])
startCells = []
for index in range(3, len(content)):
    line = content[index].replace(
        "(", "").replace(")", "").replace(" ", "").split(",")
    startCells.append((int(line[0]), int(line[1])))

# largeur d'une cellule (en px)
side = 15
# matrice des cellules à l'instant T0
currentCells = [[0 for row in range(height)] for col in range(width)]
# matrice des cellules à l'instant T1
nextCells = [[0 for row in range(height)] for col in range(width)]
# matrice de la grille générale
grid = [[0 for row in range(height)] for col in range(width)]


def draw():
    # dessin de la configuration de départ sur la matrice
    for y in range(height):
        for x in range(width):
            grid[y][x] = canvas.create_rectangle(
                x*side, y*side, (x+1)*side, (y+1)*side, outline="gray", fill="white")
    for cell in startCells:
        canvas.itemconfig(grid[cell[1]][cell[0]], fill="black")
        currentCells[cell[1]][cell[0]] = 1


def nextEvolution():
    # vérifie l'évolution des cellules
    countChangeCells = 0
    for y in range(height):
        for x in range(width):
            currentState = currentCells[y][x]
            countNeighbors = whoIsAround(x, y, wrap)
            isAlive = False if currentState == 0 else True
            nextState = isCellAlive(countNeighbors, isAlive)
            nextCells[y][x] = nextState
            if currentState != nextState:
                countChangeCells += 1
    return countChangeCells > 0


def whoIsAround(x, y, wrap):
    # compte le nombre de cellueles voisines
    countNeighbors = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if not (i == y and j == x):
                if wrap == 0 and height > i >= 0 and width > j >= 0 and currentCells[i][j] == 1:
                    countNeighbors += 1
                if wrap == 1:
                    wrapX = j
                    wrapY = i
                    if i < 0:
                        wrapY = height - 1
                    if i >= height:
                        wrapY = 0
                    if j < 0:
                        wrapX = width - 1
                    if j >= width:
                        wrapX = 0
                    if currentCells[wrapY][wrapX] == 1:
                        countNeighbors += 1
    return countNeighbors


def isCellAlive(countNeighbors, isAlive):
    # les règles du jeu : la cellule va-t-elle s'éteindre ou non ?
    if isAlive:
        if countNeighbors == 2 or countNeighbors == 3:
            return True
        else:
            return False
    else:
        if countNeighbors == 3:
            return True
        else:
            return False


def life():
    # change la couleur des cellules en fonction de leur prochain état
    # définit l'arrêt du jeu et le message de fin...
    isNext = nextEvolution()
    for y in range(height):
        for x in range(width):
            if nextCells[y][x] == 1:
                couleur = "black"
            else:
                couleur = "white"
            canvas.itemconfig(grid[y][x], fill=couleur)
            currentCells[y][x] = nextCells[y][x]
    if isNext:
        window.after(100, life)
    else:
        canvas.create_text(height*side/2, width*side/2,
                           text="Life is over...", justify="center", width=width*side, font=tkFont.Font(family="Helvetica", size=26), fill="red")


# création de la matrice de jeu
window = Tk()
window.title("Le jeu de la vie")
canvas = Canvas(window, width=side*width, height=side*height)
canvas.pack()


def main():
    draw()
    window.after(500, life)
    window.mainloop()


if __name__ == '__main__':
    main()

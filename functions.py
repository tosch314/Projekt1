def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                #bo[i][j] ="y"
                return i, j #gibt Zeile/Spalte zurück

def validate(bo, num, pos):
    #Untersucht die Zeile 
    for i in range(len(bo)):
        #bo[pos[0][i]] ist die Zeile und Spalte - sprich startet an Position 0 der ersten Zeile
        #pos[1]  != i soll er nicht untersuchen, da der Wert in diese Zeile eingefügt wurde, soll sich nur alle anderen "Werte" anschauen
        if bo[pos[0]][i] == num and pos[1] !=i:
            return False
    
    #Untersucht die Spalte    
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] !=i:
            return False

    #Untersucht die Box
    #--> War mir zu hoch.. pos[0], pos[1] hab ich oben schon nicht 100% gerallt. :/
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                False
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        #wird nichts gefunden, ist das Sudoku gelöst und es wird "True wiedergegeben - nix zu solven?!
        return True
    else:
        #in der Funktion find_empty werden die leeren "Stellen" (Zeile/Spalte) zurückgegeben
        row, col = find

    for i in range(1, 10):
        #Hier wird der Wert in die gefundene leeze Zeile eingesetzt
        if validate(bo, i, (row, col)):
            bo[row][col] = i
            #
            if solve(bo):
                return True

            bo[row][col] = 0

    return False


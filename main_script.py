from functions import solve
import functions


sudoku = [
    [0, 9, 0, 3, 6, 0, 1, 0, 4],
    [0, 7, 5, 0, 0, 2, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 3, 4, 8, 0, 0, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 2, 5, 4, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 8, 0, 0, 6, 3, 0],
    [6, 0, 4, 0, 3, 1, 0, 2, 0],
]

#Für das setzen der "-", um das Sudoku besser lesen zu können
# i !=0, da Schleife mit 0 startet und nicht direkt mit - gestartet werden soll
# i % 3, da nach jeder dritten "Spalte" die "-" gesetzt werden sollen, für die Lesbarkeit, wo kein Rest ist, wird gesetzt
def print_sudoku(bo):
    for i in range(len(bo)): 
        if i % 3==0 and i != 0:
            print("- - - - - - - - - - - -")
    
        for j in range(len(bo)):
            if j % 3==0 and j != 0:
                #ohne "end" wird nach dem | in die nächste Zeile gesprungen. end="" = "stay on the same line"
                print(" | ", end="")
        
            if j == 8:
                print (bo[i][j])
            else:
                print (str(bo[i][j]) + " ", end="")

#find_empty(sudoku)
print_sudoku(sudoku)
solve(sudoku)
print("-------------------------")

print_sudoku(sudoku)

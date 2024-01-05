def isValidSudoku(board): #ορισμος σθναρτησης
    def is_valid_unit(unit):#ορισμος εσωτερικης συνάρτησησ που πέρνει εναν πίνακα (unit)
        seen = set() #dhmiourgia synoloy (seen) gia na krata ta monadika stoixeia toy (unit)
       
        for num in unit: # elegxei kathe arithmo sto unit
            if num != '.': # an arithmos diaforos tou kenou (".") tote elegxei an exei emfanistei
                #sto synolo (seen)
                if num in seen: # an exei emfanistei tote epistrefei false
                    return False
                seen.add(num) # diaforetika prostithetai sto synolo (seen)
        return True #ean ola ta stoixeia einai monadika h synarthsh apistrefei true

    # elegxos grammwn
    for row in board: # enas vrogxos pou epeksergazetai kathe grame tou pinaka
        if not is_valid_unit(row): #kaleitai synarthsh gia elegxo egkyrothtas se kathe grammh
            return False # an dn einai egkyrh epistrefei false

    # elegxos sthlwn
    for col in zip(*board):#(zip)enwnei ths stiles tou pinaka se grammes
        #(*)xrhsimopoeite gia na ksepaketarei ths styles toy pinaka 
        if not is_valid_unit(col): # epeksergasia kathe sthlhs(col) tou pinaka
            #(is_valid_unit(col)) kaleitai h synarthsh gia elegxo egkyrothtas ths kathe sthlhs
            #an dn einai egkyrh 
            return False #epistrefei false

    # elegxei ola ta 3x3 koutia
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [board[x][y] 
                      # epeksergasia kathe koutiou 
                       for x in range(i, i + 3) 
                         for y in range(j, j + 3)
                       ]
            if not is_valid_unit(square): #(is_valid_unit(square)) kaleitai h synarthsh gia
                #elegxo kathe tetragwnou an dn einai egkyro
                return False #epistrefei false

    return True #epistrofh apo telesmatos

# paradeigmata

#sudoku_board = [

 #["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]
#]
#result = isValidSudoku(sudoku_board)
#print(result)

sudoku_board = [

["5", "3", ".", ".", "7", ".", ".", ".", "."],
["6", ".", ".", "1", "9", "5", ".", ".", "."],
[".", "9", "8", ".", ".", ".", ".", "6", "."],
["8", ".", ".", ".", "6", ".", ".", ".", "3"],
["4", ".", ".", "8", ".", "3", ".", ".", "1"],
["7", ".", ".", ".", "2", ".", ".", ".", "6"],
[".", "6", ".", ".", ".", ".", "2", "8", "."],
[".", ".", ".", "4", "1", "9", ".", ".", "5"],
[".", ".", ".", ".", "8", ".", ".", "7", "9"]

]
result = isValidSudoku(sudoku_board)
print(result)
# school project 
# by nickthe freak

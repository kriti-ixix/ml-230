#Importing Libraries

theBoard = {'1': " ", '2': ' ', "3": ' ', '4': ' ', '5': ' ', '6': ' ','7': ' ', '8': ' ', '9': ' '}

# user defined function
def printBoard(board):
    print(board['7']+ '|'+ board['8']+ '|'+ board['9'])
    print('-+-+-')
    print(board['4']+ '|'+ board['5']+'|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|'+ board['2']+ '|' + board['3'])
 
    
def playGame():
    player1 = input('Enter first player name: ')
    player2 = input('Enter another player name: ')
    
    print(player1 + ':X' +" " + player2 + ':O')
    
    turn = 'X'
    count = 0
    
    player = player1
    
    while True:
        printBoard(theBoard)
        
        if count==9:
            print('the game ends in a draw')
            break
        if player == player1:
            move = input('Enter your move {}: '.format(player1))
        else:
            move = input('Enter you move {}: '.format(player2))
            
            
            
        if move not in theBoard.keys():
            print('Invalid move')
            continue
        
        if theBoard[move]== ' ':
            theBoard[move]= turn
            
        #CHecking for winner
        
            winner = checkWin(turn)
            if winner!= '':
                printBoard(theBoard)
                print('Congratulation!! the winner is ', player)
                print("***Thanks for playing***")
                break 
            
            else :
                count+=1
                if turn == "X":
                    turn = "O"
                    player = player2
                else:
                    turn = 'X'
                    player =  player1
                    
                
        else:
            print('Sorry this place is already filled')
            continue
            
            
            
            
def checkWin(turn):
    winner = ''
    
    #Checking for rows
    
    if (theBoard['7']== theBoard['8']==theBoard['9']== turn) or(theBoard['4']== theBoard['5']==theBoard['6']== turn)or(theBoard['1']== theBoard['2']==theBoard['3']== turn):
        winner = turn
     
    #Checking for vertical
    if (theBoard['7']== theBoard['4']==theBoard['1']== turn) or(theBoard['8']== theBoard['5']==theBoard['2']== turn)or(theBoard['9']== theBoard['6']==theBoard['3']==turn):
        winner = turn
        
    #Checking for diagonals
    if (theBoard['7']== theBoard['5']==theBoard['3']== turn) or(theBoard['1']== theBoard['5']==theBoard['9']== turn):
        winner = turn
        
    return winner
        
        
    
# Main loop
def main():
    playGame()
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    

   


 
    
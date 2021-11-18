#School Project by Synthesz

from random import randint 

# display of lists
display=[[" "," "," "," "],[" "," "," "," "],[" "," "," "," "],[" "," "," "," "]]

# creation of a display using the gaps in the lists
def show(display):
    print("---------")
    print("|"+display[0][0]+"|"+display[0][1]+"|"+display[0][2]+"|"+display[0][3]+"|")
    print("---------")
    print("|"+display[1][0]+"|"+display[1][1]+"|"+display[1][2]+"|"+display[1][3]+"|")
    print("---------")
    print("|"+display[2][0]+"|"+display[2][1]+"|"+display[2][2]+"|"+display[2][3]+"|")
    print("---------")
    print("|"+display[3][0]+"|"+display[3][1]+"|"+display[3][2]+"|"+display[3][3]+"|")
    print("---------")

# general conditions
possible_numbers_instance=["0","1","2","3"]
victory=False
stalemate=False
which_turn=0

# case verification to know if a case is used or not 
def case_verification(p,r,c):
    if p[r][c]==" ":
        return True
    else:
        return False

# verifying if 4 o/x are aligned
def verification_victory(p):
    if p[0][0]==p[0][1] and p[0][1]==p[0][2] and p[0][2]==p[0][3] and p[0][3]!=" ":
        return True
    elif p[1][0]==p[1][1] and p[1][1]==p[1][2] and p[1][2]==p[1][3] and p[1][3]!=" ":
        return True
    elif p[2][0]==p[2][1] and p[2][1]==p[2][2] and p[2][2]==p[2][3] and p[2][3]!=" ":
        return True
    elif p[3][0]==p[3][1] and p[3][1]==p[3][2] and p[3][2]==p[3][3] and p[3][3]!=" ":
        return True
    elif p[0][0]==p[1][0] and p[2][0]==p[1][0] and p[3][0]==p[2][0] and p[3][0]!=" ":
        return True
    elif p[0][1]==p[1][1] and p[2][1]==p[1][1] and p[3][1]==p[2][1] and p[3][1]!=" ":
        return True
    elif p[0][2]==p[1][2] and p[2][2]==p[1][2] and p[3][2]==p[2][2] and p[3][2]!=" ":
        return True
    elif p[0][3]==p[1][3] and p[2][3]==p[1][3] and p[3][3]==p[2][3] and p[3][3]!=" ":
        return True
    elif p[0][0]==p[1][1] and p[2][2]==p[1][1] and p[3][3]==p[2][2] and p[3][3]!=" ":
        return True
    elif p[0][3]==p[1][2] and p[1][2]==p[2][1] and p[2][1]==p[3][0] and p[0][3]!=" ":
        return True
    elif " " not in p[0] and " " not in p[1] and " " not in p[2] and " " not in p[3]:
        return None
    else:
        return False

# giving end result
def result(k):
    if victory==True:
        print("Player "+k+" wins the match")
    elif stalemate==True:
        print("The match ended up in a stalemate")

gamemode_type=["1","2"]
print("1: player1(x) vs IA(o)")
print("2: player1(x) vs player2(o)")
gamemode_choice=input("How much person are playing the game?: ")
while gamemode_choice not in gamemode_type:
    gamemode_choice=input("TypeError: please choose a number between 1 or 2: ")
print("\n")

#-------------------------------mode player vs ia--------------------------------------------------
if gamemode_choice=="1":
    while victory==False and stalemate==False:
        if which_turn%2==0:
            player="x"
        else:
            player="o"
    
        if player=="x":
            row=input("player "+player+": choose your row with a number between 0 and 3: ")
            while row not in possible_numbers_instance:
                print("TypeError: please choose a number between 0 and 3 only")
                row=input("player "+player+": choose your row with a number between 0 and 3: ")
            row=int(row)
            column=input("player "+player+": choose your column number between 0 and 3: ")
            print("\n")
            while column not in possible_numbers_instance:
                print("TypeError: please choose a number between 0 and 3 only")
                column=input("player "+player+": choose your column number between 0 and 3: ")
            column=int(column)
            if case_verification(display,row,column)==False:
                print("La case ne peut pas être choisie. ")
                print("\n")
                which_turn-=1
            else:
                display[row][column]=player
                show(display)
        elif player=="o":
            row=randint(0,3)
            column=randint(0,3)
            if case_verification(display,row,column)==False:
                which_turn-=1
            else:
                print("The AI "+player+" choosed row: "+str(row))
                print("The AI "+player+" choosed column: "+str(column))
                print("\n")
                display[row][column]=player
                show(display)
            
        if verification_victory(display)==True:
            victory=True
        elif verification_victory(display)==None:
            stalemate=True
        else:
            which_turn+=1
    result(player)
#-------------------------------mode player vs player--------------------------------------------------
if gamemode_choice=="2":
    while victory==False and stalemate==False:
        if which_turn%2==0:
            player="x"
        else:
            player="o"
            
        row=input("player "+player+": choose your row with a number between 0 and 3 ")
        while row not in possible_numbers_instance:
            print("TypeError: please choose a number between 0 and 3 only")
            row=input("player "+player+": choose your row with a number between 0 and 3")
        row=int(row)
        
        column=input("player "+player+": choose your column number between 0 and 3: ")
        while column not in possible_numbers_instance:
            print("TypeError: please choose a number between 0 and 3 only")
            column=input("player "+player+": choose your row with a number between 0 and 3")
        print("\n")
        column=int(column)
        if case_verification(display,row,column)==False:
                print("Error: this spot cannot be choosen: already filled")
                which_turn-=1
        else:
            display[row][column]=player
            show(display)
        if verification_victory(display)==True:
            victory=True
        elif verification_victory(display)==None:
            stalemate=True
        else:
            which_turn+=1
    result(player)

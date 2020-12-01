#Python 3.7 (windows)
#Rock-Paper-scissors :)



import random 
import time


 
def logic(user_move, computer_move):
    # Same Move , A tie 
    if user_move ==  computer_move :
        isWin =  0
        return isWin

    # Player: Rock , Computer: Paper, player losses
    elif user_move == list_[1] and computer_move == list_[2]:
        isWin =  False
        return isWin

    # Player: Rock , Computer: Scissors, player wins 
    elif user_move == list_[1] and computer_move == list_[3]:
        isWin =  True
        return isWin

    # Player: Paper , Computer: rock , player wins 
    elif user_move == list_[2] and computer_move == list_[1]:
        isWin =  True
        return isWin

    # Player: Paper , Computer: Scissors, player wins 
    elif user_move == list_[2] and computer_move == list_[3]:
        isWin =  True
        return isWin
    
    # Player: Sccisors , Computer: Rock, player losses
    elif user_move == list_[3] and computer_move == list_[1]:
        isWin =  True
        return isWin

    # Player: Sccisors , Computer: Rock, player wins
    elif user_move == list_[3] and computer_move == list_[2]:
        isWin =  True
        return isWin





list_ = {1:"Rock", 2:"Paper", 3:"Scissors"}
score = 0

def main(user_move, score):

    random_ = random.randint(1,3)
    computer_move = list_[random_]

    isWin = logic(user_move, computer_move)
    if isWin == 0:
        result = "Ties"
    elif isWin:
        result = "Wins"
        score += 1
    else :
        result = "losses"

    print(" ")
    print(f"""
        Player  {result} againt computer :P
        your move : {user_move}
        computer's move : {computer_move}

        Your Score : {score}

    """)
    print(" ")

    return score




while True:
    try:
        print("*" * 50)
        print(" ")
        print("""
            Select a Number to perform moves
            1 : Rock
            2 : Paper
            3 : Scissors

            * Press ctrl + Q to exit :) *
        """)
        print(" ")
        print("*" * 50)

        user_move = input(">>> ")
        try:
            if int(user_move) > 3 :
                print(" Not a valid move! try again")
            else:
                user_move = list_[int(user_move)]
                score = main(user_move, score)
        except:
            print("Somthing went wrong!!")
            
    except KeyboardInterrupt:
        print("""
        thanks for using hope you enjoyjed :)
        Exiting Gracefully.....
        """)
        break

''' TIC_TAC_TOE'''
import sys
print("Welcome to tic tac toe!")
def print_data(a_r):
    '''Prints the  data'''
    print("  |   |")
    print(a_r[7]+" | "+a_r[8]+" | "+a_r[9])
    print("  |   |")
    print("_________")
    print("  |   |")
    print(a_r[4]+" | "+a_r[5]+" | "+a_r[6])
    print("  |   |")
    print("_________")
    print("  |   |")
    print(a_r[1]+" | "+a_r[2]+" | "+a_r[3])
    print("  |   |")

def player_sym():
    '''PLAYER selects the SYMBOL and start game function is called'''
    a_list = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    p_1 = ' '
    while p_1 not in ('X', 'O'):
        p_1 = input("player 1: Do you want to be X or O? ").upper()
    if p_1 == 'X':
        p_2 = 'O'
    else:
        p_2 = 'X'
    print("player 1 will go first.")
    if input("Are you ready to play? Yes or No.").lower() == 'yes':
        start_game(p_1, p_2, a_list)
        replay()
    else:
        print("Thank u :)")

def start_game(p_1, p_2, a_list):
    '''STARTsGAME and players chooses the positions that they want to enter '''
    f_lag = True
    c_ount = 0
    i_np = ''
    print_data(a_list)
    while f_lag:
        n_um = int(input("Choose your next position: (1-9) "))
        if n_um not in range(1, 10) or a_list[n_um] != " ":
            print("position not present! or it is filled")
            continue
        c_ount += 1
        if c_ount%2 != 0:
            a_list[n_um] = p_1
            i_np = p_1
        else:
            a_list[n_um] = p_2
            i_np = p_2

        print_data(a_list)
        if c_ount in range(5, 9):
            f_lag = logic(a_list, i_np)

        if c_ount == 9:
            f_lag = logic(a_list, i_np)
            if f_lag is True:
                print("Draw match")
                f_lag = False

def logic(a_r, in_put):
    '''LOGIC FUNCTION that checks whether there is any winner'''
    if ((a_r[1] == in_put and a_r[2] == in_put and a_r[3] == in_put) or\
        (a_r[4] == in_put and a_r[5] == in_put and a_r[6] == in_put) or\
        (a_r[7] == in_put and a_r[8] == in_put and a_r[9] == in_put) or\
        (a_r[1] == in_put and a_r[4] == in_put and a_r[7] == in_put) or\
        (a_r[2] == in_put and a_r[5] == in_put and a_r[8] == in_put) or\
        (a_r[3] == in_put and a_r[6] == in_put and a_r[9] == in_put) or\
        (a_r[1] == in_put and a_r[5] == in_put and a_r[9] == in_put) or\
        (a_r[3] == in_put and a_r[5] == in_put and a_r[7] == in_put)):
        print("Congratulations you won the game")
        return False

    return True

def replay():
    '''REPLY FUNCTION works as recursive function used for replaying the game'''
    while input("Do you want to play again? yes or no ").lower() == 'yes':
        player_sym()
    sys.exit()
player_sym()

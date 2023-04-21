import random as Rd

def game(comp, player):
    if  comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True


a = Rd.randint(1,3)
#print(a)
if a == 1:
    comp = 's'
elif a == 2:
    comp = 'w'
elif a == 3:
    comp = 'g'
player = input("your turn: ")
print(f" comp baba: {comp}" )
print(f" player : {player}" )
X = game(comp, player)
if X == None:
    print("Tie")
elif X:
    print("Win")
else:
    print("lose")
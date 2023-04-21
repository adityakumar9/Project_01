print("Press 1 for Addition \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division" )
num = int(input("Chose The Number: "))

def add(D):
    D = D[0] + D[1]
    return D

def sub(S):
    S = S[0] - S[1]
    return S

def dev(V):
    V = V[0] / V[1] if V[1] != 0 else "Un-define"
    return V

def mul(M):
    M = M[0] * M[1]
    return M


if  num == 1:
    sid = [float(input("Enter first value ")), float(input("Enter second value "))]
    print("Answer is: ", add(sid))
elif num == 2:
    sid = [float(input("Enter first value ")), float(input("Enter second value "))]
    print("Answer is: ", sub(sid))
elif num == 3:
    sid = [float(input("Enter first value ")), float(input("Enter second value "))]
    print("Answer is: ", mul(sid))
elif num == 4:
    sid = [float(input("Enter first value ")), float(input("Enter second value "))]
    print("Answer is: ", dev(sid))
else:
    print("Please press correct number, Number is invalid: ")
val = [int(input("first value: ")), int(input("second value: "))]
class calc:

    def Adi(self, A):
        A = A[0] + A[1]
        return A
    def Sub(self, S):
        S = S[0] - S[1]
        return S
    def Mul(self, M):
        M = M[0] * M[1]
        return M
    def Div(self, D):
        D = D[0] / D[1] if D[1] != 0 else "Undefine"
        return D

Calculator = calc()
print("Summary is: ")
print(Calculator.Adi(val))
print(Calculator.Sub(val))
print(Calculator.Mul(val))
print(Calculator.Div(val))
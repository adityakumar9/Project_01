#n = 5

# for i in range(n):
#     run = run * (i+1)
# print(run)

# factorial
def FactF(n):
    run = 1
    for i in range(n):
        run = run * (i+1)
    return(run)

print(FactF(5))



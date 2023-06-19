def safe(solve, pos, epoch):

    for i in range(pos):
        if (solve[i] == epoch) or (abs(solve[i] - epoch) == abs(i - pos)):
            return False
    return True

def findsolution(solve, pos):

    if pos == len(solve):
        print(solve)

    for i in range(len(solve)):
        if safe(solve, pos, i) == True:
            solve[pos] = i
            findsolution(solve,pos+1)
            solve[pos] = -1


if __name__ == "__main__":
    qeen = int(input("Ingrese la cantidad de reinas: "))
    solve = []

    for i in range(qeen):
        solve.append(-1)

    findsolution(solve, 0)
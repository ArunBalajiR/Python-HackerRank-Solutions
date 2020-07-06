def print_formatted(number):
    space=len(str(bin(n))[2:])
    for i in range(1,n+1):
        print(str(i).rjust(space,' '),oct(i)[2:].rjust(space,' '),hex(i)[2:].upper().rjust(space,' '),bin(i)[2:].rjust(space,' '))

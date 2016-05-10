def solve_fmla(fmla):

    totalMath = 0

    while

    if fmla[i] == '*':
        
        totalMath += int(fmla[i-1]) * int(fmla[i+1])

    else:

        totalMath += fmla[i]

    if fmla[i] == '+' :
        
        totalMath += int(fmla[i-1]) + int(fmla[i+1])

    else:

        totalMath += fmla[i]

    return totalMath

print solve_fmla('1+2*3+4')


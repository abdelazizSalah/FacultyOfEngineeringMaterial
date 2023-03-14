def computeHighPower(a, b, n):
    c = 0
    f = 1
    for bit in bin(b)[2:]:
        c = 2 * c
        f = (f * f) % n
        if bit == '1':
            c = c + 1
            f = (f * a) % n
    return f


print(computeHighPower(14, 27, 55))

def cariKPK(bilanganSatu, bilanganDua):
    x = bilanganSatu
    y = bilanganDua

    while x!=y:
        if x > y:
            y = bilanganDua + y
        elif x < y:
            x = bilanganSatu + x
    return x

print(cariKPK(3, 4))
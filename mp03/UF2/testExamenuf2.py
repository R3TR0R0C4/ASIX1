def llista(divisor, llistaNmeros):
    for num in llistaNmeros:
        if num % divisor == 0:
            print(f"{num} és divisible entre {divisor} sense residu")

llista(2, [1, 2, 3, 4, 5, 6, 7, 8])


def llista2(llista, n):
    if not llista:
        return []
    elif llista[0]%n==0:
        return [llista[0]] + llista2(llista[1:],n)
    else:
        return llista2(llista[1:],n)


    

print(llista2([1, 2, 3, 4, 5, 6, 7, 8], 2))
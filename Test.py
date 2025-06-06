def faculteit(n):
    totaal = 1
    while n > 1:
        totaal *= n
    return n

if __name__ == "__main__" :
    print("-- start test --")
    
    print(faculiteit(0))
    print(faculiteit(1))
    print(faculiteit(2))
    print(faculiteit(3))
    print(faculiteit(4))
    print(faculiteit(5))

    print("-- Einde test --")

    

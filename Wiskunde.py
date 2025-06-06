import math

def faculteit(n):
    totaal = 1
    while n > 1:
        totaal *= n
        n -= 1
    return totaal

def oppervlak_cirkel_sector(graden, straal) :
    return (graden/360) * math.pi * straal ** 2

if __name__ == "__main__" :
    print("-- start test --")
    
    print(faculteit(0))
    print(faculteit(1))
    print(faculteit(2))
    print(faculteit(3))
    print(faculteit(4))
    print(faculteit(5))
    
    print(f"90 graden en straal = 2 : |{oppervlak_cirkel_sector(90, 3):.2f} cm2") 

    print("-- Einde test --")

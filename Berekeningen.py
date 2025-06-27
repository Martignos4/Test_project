import math

def omtrek_cirkel(straal):
    if straal < 0:
        return 0
    return 2 * math.pi * straal

def oppervlakte_rechthoek(lengte, breedte):
    if lengte < 0 or breedte < 0:
        return 0
    return lengte * breedte

def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

def gemiddelde(getallen):
    if type(getallen) != list or len(getallen) == 0:
        return 0
    return sum(getallen) / len(getallen)

# === Assert tests ===

# omtrek_cirkel
assert math.isclose(omtrek_cirkel(1), 2 * math.pi)
assert omtrek_cirkel(-5) == 0

# oppervlakte_rechthoek
assert oppervlakte_rechthoek(3, 4) == 12
assert oppervlakte_rechthoek(-2, 5) == 0

# pythagoras
assert math.isclose(pythagoras(3, 4), 5.0)
assert math.isclose(pythagoras(5, 12), 13.0)

# gemiddelde
assert gemiddelde([1, 2, 3, 4]) == 2.5
assert gemiddelde([]) == 0
assert gemiddelde("geen lijst") == 0

print("Alle tests geslaagd.")
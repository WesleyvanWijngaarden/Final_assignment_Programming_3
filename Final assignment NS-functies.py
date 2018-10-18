def standaartprijs(afstandKM : float):
    prijs = 0
    if afstandKM > 0:
        if afstandKM > 50:
            prijs = 15 + (afstandKM * 0.60)
        else:
            prijs =  afstandKM * 0.80
    return prijs
def ritprijs(leeftijd: int, weekendrit: bool, afstandKM: float):
    normaalprijs = standaartprijs(afstandKM)
    korting = 0
    LeeftijdOUD = 65
    LeeftijdJONG = 12
    if leeftijd >= LeeftijdOUD or leeftijd <= LeeftijdJONG:
        if weekendrit:
            korting = 1 - 0.35
        else:
            korting = 1- 0.30
    elif weekendrit:
        korting = 1- 0.40
    return round(normaalprijs*korting, 2)
print(ritprijs(11, True, 14))
print(ritprijs(11, True, 15))
print(ritprijs(11, True, -1))
print(ritprijs(11, False, 14))
print(ritprijs(11, False, 15))
print(ritprijs(11, False, -1))
print(ritprijs(12, True, 14))
print(ritprijs(12, True, 15))
print(ritprijs(12, True, -1))
print(ritprijs(12, False, 14))
print(ritprijs(12, False, 15))
print(ritprijs(12, False, -1))
print(ritprijs(64, True, 14))
print(ritprijs(64, True, 15))
print(ritprijs(64, True, -1))
print(ritprijs(64, False, 14))
print(ritprijs(64, False, 15))
print(ritprijs(64, False, -1))
print(ritprijs(65, True, 14))
print(ritprijs(65, True, 15))
print(ritprijs(65, True, -1))
print(ritprijs(65, False, 14))
print(ritprijs(65, False, 15))
print(ritprijs(65, False, -1))

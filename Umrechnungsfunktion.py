def Geschwindigkeitsumrechnung(parameter1):
    #Code
    ergebnis = parameter1 * 1.60934
    return ergebnis

print("Wie viel mph sollen umgerechnet werden?")
mph = float(input())

print(mph, "mph sind", round(Geschwindigkeitsumrechnung(mph),2), "kph")


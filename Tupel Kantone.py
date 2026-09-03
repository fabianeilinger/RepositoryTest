kant = ['Zürich', 'Basel', 'Luzern']
kant[2] = 'Genf'
print(kant)

kant.extend(['Luzern', 'Schwyz', 'Küssnacht', 'Immensee'])  #Oder +=
#oder
print(kant)

tupel = (13, 4.15, "Fabian", None, True)
print('Tupel:', tupel)

z = (2, 4, 7, 4, 5, 6, 4, 3, 4, 2, 4)
print('Die Zahl 4 kommt', z.count(4), 'mal vor.')
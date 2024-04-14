def nombres_pairs(liste):
    pairs = []         # liste vide 
    for nombre in liste:
        if nombre % 2 == 0:   #modulo pour vérifier le nombre pair 
            pairs.append(nombre)

    return pairs
    


nombre_initiale = [1,2,3,4,5,6,7,8,9,10]
resultat = nombres_pairs(nombre_initiale) 
print(resultat)



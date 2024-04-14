def list_fusione (list1,list2):                         #EX/ Définir une fonction qui fusinne deux listes index par index. Par exemple, [a,b,c] et [1,2,3] devraient devenir [a1,b2,c3]
    fusion=[]
    for i in range (len(list1)):
        fusion.append (list1[i] + str(list2[i]))
        
    return fusion

list1=["a","b","c"]
list2=[1,2,3]
print(list_fusione(list1,list2))

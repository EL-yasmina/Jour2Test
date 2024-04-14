def my_list(list):
    inverse =[]                                  #list vide in python   # range (len, fin ,step) range(10 -1 -1)
    i = len (list)- 1
    while i >=0 :
            inverse.append(list[i])
            i-=1
    return inverse
list = [1,2,3,4,5]
list_invert= my_list(list)
print(list_invert)
        


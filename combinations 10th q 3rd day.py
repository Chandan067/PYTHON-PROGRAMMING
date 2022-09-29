def comb(L):  
    a=int(input("Enter first number:"))  
    b=int(input("Enter second number:"))  
    c=int(input("Enter third number:"))  
     
    L.append(a)  
    L.append(b)  
    L.append(c)  
    for i in range(3):  
        for j in range(3):  
            for k in range(3):  
                  

                if (i!=j and j!=k and i!=k or i == j, i == k, j == k):  
                    print(L[i], L[j], L[k])                   
comb([])  
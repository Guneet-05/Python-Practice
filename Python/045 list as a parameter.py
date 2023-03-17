def even_odd(list):
    even,odd=0,0
    for ele in list:
        if ele%2==0:
            even+=1
        else:
            odd+=1
    
    return even,odd

even,odd=even_odd([10,15,20,25,30])
print("even=",even)
print("odd=",odd)

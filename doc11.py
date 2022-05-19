
def  generate_Range(min, max, step):
    i=min
    k=[]
    while i<=max:
        if step>0:
            k.append(i)
            i=i+step
    print(k)
generate_Range(2,10,2)    
generate_Range(1,10,3)





    
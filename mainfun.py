# def add1(a,b):
#     return a+b
# def add2(c,d):
#     return c-d
# def add3(e,f):
#     return e*f
# def main_fun():
#     g=add1(4,5)
#     k=add2(10,5)
#     l=add3(30,2)
#     return g,k,l
# print(main_fun()) 

i=int(input("enter the no"))
rev=0
x=i
while (i>100):
    rev=(rev*0)+i%10
    i=i//10
if (x==rev):
    print("paildrom no")
else:
    print("not paildrom no")

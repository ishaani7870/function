# def number():
#     i=1
#     while i<=100:
#         if i%2==0:
#             print(i,"even")
#         elif i%2!=0:
#             print(i,"odd")
#         i=i+1
# number()

# a=int(input("enter the no"))
i=1
while i<=100:
    a=1
    c=0
    while a<=i:
        if i%a==0:
            c=c+1
        a=a+1
        if c==2:
            print("prime no")
        else:
            print("not prime no")
        i=i+1
    # else:
        # print("not prime no")
        
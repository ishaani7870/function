           
def sum (a,b,c=4):
    d=a+b+c
    print(d)
sum(6,19,5)


    
# def sum (a,b):
#     x=a+b
#     print(x)
# sum (a=4,b=6)
    
# def sum (*a):
#     print(a)
# sum(26,8,10,4)

# def sum (**a):
#     print(a)
# sum(a=5,b=7,c=10)


   

# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("The number must be whole.")
#     if number < 0:
#         raise ValueError("The number must be non-negative.")
#     #Factorial calculation
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number - 1)
#     return inner_factorial(number)
# factorial(4)ef outer_func(who):ef outer_func(who):
#     def inner_func():
#         print(f"Hello, {who}")
#     inner_func()
# outer_fu
#     def inner_func():
#         print(f"Hello, {who}")
#     inner_func()
# outer_fu


# def outer_func(who):
#     def inner_func():
#         print(f"Hello, {who}")
#     inner_func()
# outer_func("World!")


print("ishaani")
print("ali")
def fun(a,b):
    c=a+b
    print(c)
fun(4,8)
print("kashif")
print("kajal")

def outer_fun():
    def inner_fun():
        print("i,am,ishaani")
    inner_fun()
outer_fun()

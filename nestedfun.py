# def increment(number):
#     def inner_increment():
#         return number + 1
#     return inner_increment()
# print(increment(10))

# def make_point(x, y):
#     def point():
#         print(f"Point({x}, {y})")
#     def get_x():
#         return x
#     def get_y():
#         return y
#     def set_x(value):
#         nonlocal x
#         x = value
#     def set_y(value):
#         nonlocal y
#         y = value
#     point.get_x = get_x
#     point.set_x = set_x
#     point.get_y = get_y
#     point.set_y = set_y
#     return point
# make_point(1, 2)
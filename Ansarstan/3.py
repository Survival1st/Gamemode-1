# Iterator and generator
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
T = num.__iter__()
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(T.__next__())
print(dir(num))
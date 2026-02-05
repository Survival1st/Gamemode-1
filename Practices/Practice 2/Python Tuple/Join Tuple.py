#1 example
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)

#2 example
fruits = ("apple", "banana")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'apple', 'banana')

#3 example
t1 = (1, 2)
t2 = (3, 4)
t3 = (5, 6)

joined = (*t1, *t2, *t3)
print(joined) # (1, 2, 3, 4, 5, 6)


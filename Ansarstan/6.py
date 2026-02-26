def infinite():
    n = 0
    while True:
        yield n
        n += 1
gen = infinite()

for i in gen:
    if i > 167:
        break
    print(i)
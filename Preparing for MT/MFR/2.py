def hf(x):
    if int(x) > 18:
        return True
    else:
        return False
a = input().split()
print(filter(hf, a))

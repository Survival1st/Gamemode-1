def calc(op, x, y):
    return op(x,y)
def div(a, b):
    if b != 0:
        return a / b
    print("Denom was 0.")

res = calc(div, 2, 0)
#2 example
def div_by(n, d):
    """n and d are ints > 0
    Returns True if d is divides n evenly and False otherwise"""
    #n = 10 and d = 3
    #n = 195 and d = 13
    return n % d == 0
print(div_by(10, 3))  # False
print(div_by(195, 13))  # True
class poweroftwo:
    def __init__(self, me):
        self.max = me
        self.current = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.max:
            result = 2** self.current
            self.current += 1
            return result 
        else: raise StopIteration

power = poweroftwo()
for i in power:
    print(i)


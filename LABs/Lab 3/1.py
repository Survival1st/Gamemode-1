def x():
    n = input()
    is_v = True  
    
    for i in n:
        if int(i) % 2 != 0: 
            is_v = False
            break            
            
    if is_v:
        print("Valid")
    else:
        print("Not valid")

x()
    
    
    
    

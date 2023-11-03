def pow(x,y):
    if y == 0 or (x == 0 and y == 0)  :
        return 1
       
    if y < 0:
        return 1/x * pow( x,y+1)
    

    
    return x * pow( x,y-1)

print(pow(0,0))
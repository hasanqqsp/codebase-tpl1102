def pow(x,y):
    if y == 0:
        return 1    # untuk mendukung definisi 0^0 dan x^0
       
    if y < 0:
        return 1/x * pow( x,y+1) # untuk mendukung pangkat negatif
     
    return x * pow( x,y-1)

print(pow(0,0))
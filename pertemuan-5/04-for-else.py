for i in range(0,5):
    print(i) 
else:
    print("Looping Complete with no interuption")

#output : 
# 0
# 1
# 2
# 3
# 4
# Looping Complete with no interuption

for i in range(0,5):
    print(i) 
    if(i == 2):
        break
else:
    print("Looping Complete with no interuption")
    
#output : 
# 0
# 1

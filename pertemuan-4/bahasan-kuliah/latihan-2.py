print(True and False)
print(False or True)
# Output : True
print(1 == 1 and 2 == 1)
#     True  and False
# Output : False
print("true" == True)
# Output : False
print(False and 0!=0)
# Output : False ( 0 != 0 tidak akan dievaluasi)
print(not (10 ==  1 or 1000 == 1000))
#     not   ( False  or True) (Kerjakan dahulu perbandingan)
#     not (True) 
#     False
print("pete" == "jengkol" and (not(3==4 or 3 == 3)))
#       False (Selanjutnya tidak akan dievaluasi)
print(3 == 3 and not ("test" == "test" or "Python" == "Fun"))
#       True and not ( True ("Python" == "Fun"  tidak dievaluasi))
#       True and False

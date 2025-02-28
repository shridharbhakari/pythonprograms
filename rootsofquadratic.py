a=int(input("ENTER THE COEFFICIENT OF x2 : "))
b=int(input("ENTER THE COEFFICIENT OF x : "))
c=int(input("ENTER THE COEFFICIENT TERM : "))
discri=b**2-4*a*c
if discri == 0 :
    print(discri)
    print("THE EQUATION HAS TWO EQUAL ROOTS ")
elif discri>0:
    print(discri)
    print("THE EQUATION HAS TWO REAL ROOTS ")
else:
    print(discri)
    print("THE EQUATION HAS TWO COMPLEX ROOTS ")

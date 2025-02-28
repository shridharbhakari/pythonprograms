m1=int(input("ENTER THE MARKS FOE C PROGRAMMING : "))
m2=int(input("ENTER THE MARKS FOE PYTHON PROGRAMMING : "))
m3=int(input("ENTER THE MARKS FOE JAVA PROGRAMMING : "))
totalmarks=m1+m2+m3
print("TOTAL MARKS = ",totalmarks)
average = (m1+m2+m3)/3
print("AVERAGE MARKS = ",average)
grade=(totalmarks/300)*100
if grade <=59 :
    print("F")
elif grade >= 60 and grade <= 69 :
    print("D")
elif grade >= 70 and grade <= 79 :
    print("C")
elif grade >= 80 and grade <= 89 :
    print("B")
else:
    print("A")

bill=200
call=int(input("ENTER THE NO OF CALLS : "))
if call >=0 and call <=100 :
    bill=bill
    print("TOTAL BILL : ",bill)
elif call >100 and call <=150 :
    bill=bill+(call-100)*0.60
    print("TOTAL BILL : ",bill)
elif call >150 and call <=200 :
    bill=bill+(50)*0.60+(call-200)*0.50
    print("TOTAL BILL : ",bill)
elif call >200 :
    bill+=(50)*0.60+(50)*0.50+(call-200)*0.40
    print("TOTAL BILL : ",bill)
else:
    print("PLEASE ENTER VALID NO OF CALLS")

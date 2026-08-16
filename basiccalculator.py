a=int(input("Enter the a value : "))
b=int(input("Enter the b value : "))
operator=input("chose the operator ,+, - ,* ,/ : " )

if operator=="+":
    print("addition : ",a+b)
elif operator=="-":
    print("substraction : ",a-b)
elif operator=="*":
    print("multiplication : ",a*b)
elif operator=="/":
    print("division : ",a/b)
else:
    print("no such kind of operation")
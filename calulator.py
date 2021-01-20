print("**************************************************************ITS A INPUT BASED CALCULATOR******************************************************************")
print("______________________________________________________________ENTER 1 FOR ADD________________________________________________________________")
print("______________________________________________________________ENTER 2 FOR SUBTRACT______________________________________________________________")
print("______________________________________________________________ENTER 3 FOR MULTIPLY______________________________________________________________")
print("______________________________________________________________ENTER 4 FOR DIVIDE______________________________________________________________")

operator = int(input("ENTER YOUR OPERATOR: "))
a = float(input("ENTER YOUR FIRST NUMBER: "))
b = float(input("ENTER YOUR SECOND NUMBER: "))

def operation():
    if operator == 1:
        print("YOUR SUM OF NUMBER1 AND NUMBER 2 IS", a+b)
    elif operator == 2:
        print("YOUR DIFFRENCE OF NUMBER1 AND NUMBER2 IS", a-b)
    elif operator == 3:
        print("YOUR MULTIPLICATION OF NUMBER1 AND NUMBER2 IS", a*b)
    elif operator == 4:
        print("YOUR DIVISION OF NUMBER1 AND NUMBER2 IS", a/b)
    else:
        print("WRONG STATEMENT")

print(operation())





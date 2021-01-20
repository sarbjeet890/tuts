print("ITS A INPUT BASED CALCULATOR")
print("ENTER 1 FOR ADD")
print("ENTER 2 FOR SUBTRACT")
print("ENTER 3 FOR MULTIPLY")
print("ENTER 4 FOR DIVIDE")

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





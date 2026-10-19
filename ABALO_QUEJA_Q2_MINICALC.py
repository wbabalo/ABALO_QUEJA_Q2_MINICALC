# ABALO
a = int(input(f"Enter First Number: "))
b = int(input(f"Enter Second Number: "))

def addition(a, b):
    c = a + b
    print(c)
    return c


def subtraction(a, b):
    ca = a - b
    print (ca)
    return ca


def multiplication(a, b):
    cb = a * b
    print (cb)
    return cb

def division(a, b):
    if b == 0:
        print("cant divide 0")
    else:
        print(cc)
        return cc


print("Enter your Choice")
print("1 for adding")
print("2 for subtracting")
print("3 for multiplying")
print("4 for dividing")
c = int(input("Enter ur choice"))
# QUEJA
if c == 0:
        print("error")
elif c == 1:
    print(addition(a, b))
elif c == 2:
    print (subtraction(a, b))
elif c == 3:
    print (multiplication(a, b))
elif c == 4:
    print (division(a, b))
else:
    print("error")


# New: getValues()

def getValues():
  
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  return num1, num2

number1, number2 = getValues()

print(f"First number: {number1}")
print(f"Second number: {number2}")


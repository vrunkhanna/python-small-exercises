a = int(input("enter your age: "))
b = int(input("enter your partner age: "))
c = b - a
d = a - b
if a < b:
    print("you are younger than your partner with difference:", c, "Years")
elif a == b:
    print("your and your partner age is same which is: ", a)
else:
    print("You are elder than your partner", d, "Years")
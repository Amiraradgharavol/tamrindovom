#Exit
a = []

while True:
    x = int(input(" plz enter number:"))
    a.append(x)

    b = input("enter exit and the end: ")
    if b == "exit":
        break

sum1= sum(a)
print("sum =", sum1)
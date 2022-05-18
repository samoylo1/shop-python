laptop = 15000
phone = 7000
keyboard = 3000

a = int(input("Laptop: "))
b = int(input("Phone: "))
c = int(input("Keyboard: "))

if a >= 0:
    l = laptop*a
if b >= 0:
    h = phone*b
if c >= 0:
    n = keyboard*c

if a + b + c > 0:
    print("You have to pay: ", l + h + n)
else:
    print("You have to buy something!")
import random
star = int(input("enter the first num :"))
end = int(input("enter the end num :"))
g = int(input("enter the giss num :"))
if star <= g <= end:
    print(random.randint(star, end))
    if random == g:
        print("true")
    else:
        print("error")
else:
    print("out of range")

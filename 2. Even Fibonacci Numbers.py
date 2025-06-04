a,b = 1,2
total=0

while a < 4000000:
    temp = a
    a = b
    b = temp+b
    if a % 2 ==0:
        total = total +a

print(total)

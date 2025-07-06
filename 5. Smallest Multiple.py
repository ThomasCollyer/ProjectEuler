#Be strategic
#If it is divisble by 20 => it is divisible by 2,4,5 and 10
#19 is prime
#If it is divisble by 18 => it is divisible by 2,3 and 9
#17 is prime
#16 => 2,4 and 8
#15 => 3 and 5
#14 => 2 and 7
#13 is prime
#12 => 2 and 6
#11 is prime
#10 => 2 and 5
#9 => 3 and 3
#8 => 2 and 4
#7 is prime
#6 => 2 and 3
#5 is prime
#4 => 2
#3 is prime
#2 is prime

def find_smallest(x):
    return all((
        x % 20 == 0,
        x % 19 == 0,
        x % 18 == 0,
        x % 17 == 0,
        x % 16 == 0,
        x % 15 == 0,
        x % 14 == 0,
        x % 13 == 0,
        x % 12 == 0,
        x % 11 == 0,
        ))

#Use return all
accept_flag = 0
current_num = 20
while True:
    if find_smallest(current_num) == True:
        break
    else:
        current_num += 1
print("Smallest number is " + str(current_num))


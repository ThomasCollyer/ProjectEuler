def is_palindrome(x):
    x  = str(x)
    digits = [digit for digit in x]
    for i in range(len(digits)):
        if digits[i] != digits[len(digits)-i-1]:
            return 0
    return 1

#Generate all numbers that are products of 3 digits
product_nums = []
for i in range(100,1000):
    for j in range(100,1000):
        product_nums.append(i*j)

#Keep only the numbers that are palindromes
palindromes = [i for i in product_nums if is_palindrome(i) == 1]

#Get the largest palindrome
print(max(palindromes))


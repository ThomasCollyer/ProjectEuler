from math import ceil, floor

def get_factors(x):
    orig_x = x
    #Get all the numbers between 2 and ceil(sqrt(x)) these are the only numbers
    #that can potentially be factors. Then reverse the order, which simplifies computation
    potential_factors = [i for i in range(2,ceil(x**0.5)+1)]
    potential_factors = list(reversed(potential_factors))
    factors = []

    #Check if each potential factor is indeed a factor and make a list of these factors
    for potential in potential_factors:
        if x % potential == 0:
            factors.append(potential)
            #Divide input x by the factor to stop repeated factors occuring unnecessarily
            x = x / potential

    #Check if x at this point is prime, add it to the list if so
    if is_prime(x) == 1:
        factors.append(x)

    #This part uses recursion. It tests if each factor is prime, if so it will run get_factors repeatedly
    #on non-prime factors until eventually, all our original factors are broken down into primes
    for i in range(len(factors)):
        if is_prime(factors[i]) == 1:
            pass
        else:
            factors[i] = get_factors(factors[i])

        new_factors = []
        for factor in factors:
            if str(type(factor)) == "<class 'list'>":
                for item in factor:
                    new_factors.append(int(item))
            else:
                new_factors.append(int(factor))
    factors = new_factors
    return factors
    

        

#Function to test if a given number x is prime
def is_prime(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    for i in range(2,ceil(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1
    

#Uncomment to run
#input_num = 12345
#prime_factors = list(sorted(get_factors(input_num)))
#prime_factors = [int(i) for i in prime_factors]
#print(prime_factors)





sum_of_squares = sum([i**2 for i in range(101)])
square_of_sums = sum([i for i in range(101)])**2

diff = square_of_sums - sum_of_squares
print(diff)

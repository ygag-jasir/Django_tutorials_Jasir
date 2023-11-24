# PrimeNumber Problem

# Prime Number: A number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).


for x in range(1,100):
    if x % x and x % 1 == 0:
        print("x : ",x)
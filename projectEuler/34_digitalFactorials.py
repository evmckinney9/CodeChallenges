import timeit
from math import factorial

#project euler problem 34

start = timeit.default_timer()

factorialDictionary = {}
for i in range(0, 10):
    factorialDictionary[i] = factorial(i)

def main():
    guess = 50000
    total = 0   
    while (guess >= 3):
        if (isDigitalFactorial(guess)):
            total += guess
        guess = guess-1
    print(total)

def isDigitalFactorial(n):
    sum = 0
    for digit in [int(d) for d in str(n)]:
        sum += factorialDictionary[digit]
        if sum > n : return False
    if (sum == n) : 
        return True
   
if __name__ == "__main__":
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
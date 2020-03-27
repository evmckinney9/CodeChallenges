import timeit

#project euler problem 36

start = timeit.default_timer()
N = 1000000

def main():
    total = 0
    guess = N
    while (guess > 0):
        if (isDoubleBasePalindrome(guess)):
            total += guess
        guess = guess -1
    print(total)
   

def isDoubleBasePalindrome(n):
    return isPalindrome(str(n)) and isPalindrome(str(bin(n))[2:])

def isPalindrome(n):
    if (len(n) <= 1): return True
    if n[0] == n[len(n)-1]:
        return isPalindrome(n[1:len(n)-1])
    return False

if __name__ == "__main__":
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
from itertools import permutations
import timeit

#project euler problem 32

start = timeit.default_timer()
universe = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def main():
    guess = 7900 #9874
    total = 0

    while (guess >= 4300): #1234
        if (isPandigitalProduct(guess)):
            total += guess
        guess = guess -1
    print(total)


def isPandigitalProduct(n):
    if not uniqueDigits(n): return False

    remainingDigits1 = universe.difference(set(str(n)))

    for m1PermLength in range(1, 1+ int(len(remainingDigits1)/2)):

        m1Set = permutations(remainingDigits1, m1PermLength)

        for m1 in m1Set:
            remainingDigits2 = universe.difference(set(str(n)).union(m1))
            
            m2Set = permutations(remainingDigits2, len(remainingDigits1) - m1PermLength)

            for m2 in m2Set:

                int_m1 = int("".join(map(str, m1)))
                int_m2 = int("".join(map(str, m2)))
                #print(int_m1, int_m2)
                
                if not (int_m1 > n or int_m2 > n):

                    if (int_m1 * int_m2 == n): 
                        #print(f"{int_m1} * {int_m2} = {n}")
                        return True
                
    return False
            

def uniqueDigits(n):
    return len(set(str(n))) == len(str(n))
   
if __name__ == "__main__":
    main()
    #print(isPandigitalProduct(7254))
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
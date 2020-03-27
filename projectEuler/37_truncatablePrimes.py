import timeit

#project euler problem 37

start = timeit.default_timer()
N = 1000000
is_prime = [1]*N
is_prime[0] = 0
is_prime[1] = 0
x = range(0, 10)
y = [1, 2, 3, 5, 7, 9]



def main():
    count = 0

    #tree acts as master list of created primes
    tree = []
    #stack acts as list of references to nodes to create subtrees from
    stack = []

    stack.append(7)
    stack.append(3)

    while (count < 11):

        root = stack.pop(0)

        if (root == 797):
            mm = 9

        for d in y:
            fail = 0
            possible = int(str(d) + str(root))
            #check if prime in one direction
            if is_prime[possible] == 1:
                stack.append(possible)
                #check is remains prime while breaking down other direction
                possible_check = int(possible/10)
                while (possible_check > 0):
                    if is_prime[possible_check] != 1:
                        fail = 1
                        break
                    possible_check = int(possible_check/10)
                if fail == 0:
                    #print(possible)
                    tree.append(possible)
                    count += 1
    total = sum(tree)
    print(f"total : {total}")

def sieve():
    i = 2

    # This will loop from 2 to int(sqrt(x))
    while i*i <= N:
        # If we already crossed out this number, then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            # Cross out this as it is composite
            is_prime[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1

   
   
if __name__ == "__main__":
    sieve()
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
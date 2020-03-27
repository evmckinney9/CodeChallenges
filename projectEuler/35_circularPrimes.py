import timeit

#project euler problem 35

start = timeit.default_timer()
N = 1000000
is_prime = [1]*N
is_prime[0] = 0
is_prime[1] = 0

def main():
    total = 2 #count 2, 5 to start
    guess = N
    while (guess > 0):
        failed = 0
        digit_set = str(guess)

        if len(set(["0", "2", "4", "5", "6", "8"]).intersection(digit_set)) > 0:
            guess = guess - 1
            continue

        list_circle = [str(guess)]
        list_circle = circle(list_circle, str(guess))
        
        for perm  in list_circle:
            int_perm = int("".join(perm))
            if is_prime[int_perm] == 0 :
                failed = 1
                break

        if failed == 0:
            print(guess)
            total += 1

        guess = guess -1

    print("total: ", total)

def circle(l, n):
    if len(l) == len(n):
        return l
    new_str = n[1:] + n[:1]
    l.append(new_str)
    return circle(l,new_str)
    

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
    
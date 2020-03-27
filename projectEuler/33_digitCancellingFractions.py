import timeit

#project euler problem 33

start = timeit.default_timer()

def main():
    total = 0
    for numerator in range(10,100):
        for denominator in range(numerator+1, 100):
            #check if a single repeated digit and that it is not 0
            #if statements used to avoid trivial cases and division by 0.
            if len([d for d in str(numerator) if str(d) in str(denominator) and d != "0"]) == 1:
                if len([d for d in str(denominator) if str(d) in str(numerator)]) == 1:
                    short_num = int("".join([d for d in str(numerator) if d not in str(denominator)]))
                    short_den = int("".join([d for d in str(denominator) if d not in str(numerator)]))
                    if (short_den != 0 and short_num/short_den == numerator/denominator):
                        print(f"{numerator}/{denominator} => {short_num}/{short_den}")

      
if __name__ == "__main__":
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
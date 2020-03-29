import timeit

#project euler problem 38

start = timeit.default_timer()

def main():
    m = 1
    cat = ""
    for x in range(9487, 9234, -1):
        while(True):
            cat += str(x*m)
            m+=1
            if len(cat) == 9 and uniqueDigits(int(cat)):
                print(cat)
                return
            elif len(cat) >= 9:
                cat = ""
                m = 1
                break
        
            

def uniqueDigits(n):
    return len(set(str(n))) == len(str(n)) and "0" not in str(n)
   
if __name__ == "__main__":
    main()
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    
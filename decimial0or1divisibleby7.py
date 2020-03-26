import matplotlib.pyplot as plt
import time

###QUESTIONABLY WORKINg???

exp = 8
def brutemethod():
    startslow = time.time()
    tot = 0
    results = []
    while tot < 10**exp:
        bool = True
        for digit in str(tot):
            if digit != '0' and digit != '1':
                bool = False
        if bool:
            results.append(tot)
        tot+= 7
    endslow = time.time()
    print(f"brute time : {endslow-startslow}")
    return results


def fastmethod():
    startfast = time.time()
    results2 = []
    rcounter = 0
    dectopguess = 0
    n =0
    prevshift = 0
    while dectopguess < 10**exp:
        topguess = bin(n*7)
        dectopguess = int(str(topguess[2:]))
        shift = 1
        flip = 0
        while dectopguess%7 != 0 or dectopguess in results2:
            index = ((n-1-flip)*7)+shift
            shift +=1
            if n == 15:     #HARD-CODE BAD!
                index = 97
            topguess = bin(index)
            dectopguess = int(str(topguess[2:]))
        if dectopguess < 10**exp:
            # if results[rcounter] == dectopguess:
            #     results2.append(dectopguess)
            # else:
            #     results2.append("missed!")
            #     results2.append(dectopguess)
            #     rcounter+=1
            results2.append(dectopguess)
        rcounter+=1
        n+=1
        prevshift = shift

    endtime = time.time()
    print(f"fast time : {endtime-startfast}")
    return results2



def main():
    results = brutemethod()
    results2 = fastmethod()
    for i in range(len(results2)):
        print(f"brute: {results[i]}; fast: {results2[i]} n: {i}")


def plot(results):
    x = []
    x2 = []
    y= []
    y2=[]
    for n in range(1,len(results)):
        given = results[n-1]
        fornext = results[n] - given
        binarygiven = int(str(given),2)
        fornextbinary = int(str(results[n]),2) - binarygiven
        #print(f"given: {given}, binarygiven: {binarygiven}; fornext: {fornext} fornextbinary: {fornextbinary}")
        #print(binarygiven%fornextbinary)
        print(f"binarygiven: {binarygiven}; fornextbinary: {fornextbinary}; n:{n}")
        x.append(n)
        y.append(binarygiven/(n))

    plt.plot(x,y, 'o')
    print(max(y))
    plt.show()


if __name__ == "__main__":
    main() #compare two times for brute vs fast
    # results = fastmethod()
    # for a in results:
    #     print(a)
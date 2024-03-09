import signal
import sys
import os
run = True

def signal_handler(sig, frame):
    global run
    os.write(sys.stdout.fileno(),b"You pressed Ctrl+C!\n")
    run = False



class Primes:
    def Execute(self):
        global run
        primes = []
        counter = 2
        if os.path.isfile("primes.txt"):
            with open("primes.txt","r") as outFile:
                primes = list(map(int,list(outFile)))
                counter = 2
                outFile.close()

        if primes:
            counter = primes[0]
        else:
            primes = [2, 2]
        while run == True:
            isPrime = True
            for prime in primes[1:]:
                if (counter % prime) == 0:
                    isPrime = False
            if(isPrime) and (counter != primes[-1]):
                primes.append(counter)
                print("Found prime number: {}".format(counter))
            counter += 1

        print("Outside while")
        primes[0] = counter
        with open("primes.txt","w+") as outFile:
            outFile.write('\n'.join(str(prime) for prime in primes))
            outFile.close()
            

def main():
    
    signal.signal(signal.SIGINT, signal_handler)
    p = Primes()
    p.Execute()
    print('Press Ctrl+C to exit')

if __name__ == "__main__":
    main()
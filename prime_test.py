import random

# SAMPLE PRIMES
Large1 = 5392383212153798271252675141844558630694581411163315034502420654720546892554490673272968707353842429
Large2 = 738412258415779233091125031513
Large3 = 9264014769743134810094779
Small1 = 1151
Small2 = 883
Small3 = 47

# SAMPLE COMPOSITES
Flarge1 = 10000000000000000000000000000
Flarge2 = 651681654687998454651654
Flarge3 = 99998778456654654668
Fsmall1 = 8000
Fsmall2 = 224
Fsmall3 = 21


def prime_test(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    e = n - 1
    b = random.randint(2, e)

    if pow(b, e, n) == 1:
        return True

def prime_loop(n):
    is_prime = True
    for i in range(75):
        passed = prime_test(n)
        if not passed:
            is_prime = False
    return is_prime

def program_test(lower_bound, upper_bound):
    primes = 0
    composites = 0
    for i in range(lower_bound, upper_bound+1):
        if prime_loop(i):
            primes += 1
        else:
            composites += 1
    return (primes, composites)


def main():
    was_negative = False
    print("Welcome to the prime number tester. ")
    print("Choose one of the following selections: ")
    print("Test Sample Numbers:")
    print("(a, b, c) = Large prime numbers. (d, e, f) = Small prime numbers. ")
    print("(t, u, v) = Large composite numbers.  (x, y, z) = Small composite numbers. ")
    print("(p) Test all numbers between 1 - 300,000. (o) Test all numbers between bounds of your choice. ")
    print("(n) = Enter integer of your choice. ")
    inp = input("Please make a selection: ")

    if inp == 'a':
        n = Large1
    elif inp == "b":
        n = Large2
    elif inp == "c":
        n = Large3
    elif inp == "d":
        n = Small1
    elif inp == "e":
        n = Small2
    elif inp == "f":
        n = Small3

    elif inp == "t":
        n = Flarge1
    elif inp == "u":
        n = Flarge2
    elif inp == "v":
        n = Flarge3
    elif inp == "x":
        n = Fsmall1
    elif inp == "y":
        n = Fsmall2
    elif inp == "z":
        n = Fsmall3
    
    elif inp == "p":
        print("Testing... ")
        primes, composites = program_test(1, 300000)
        print("Done! ")
        print("Tested numbers between 1 - 300,000. ")
        print("Found", primes, "primes and", composites, "composites. ")
        if primes > 0:
            return True
        else:
            return False

    elif inp == "o":
        lower = int(input("Please enter the lower bound: "))
        upper = int(input("Please enter the upper bound: "))
        if lower > upper:
            print("Testing... ")
            primes, composites = program_test(upper, lower)
        elif lower == upper:
            if prime_loop(lower):
                print("PRIME")
                print(lower, "is a prime number. ")
                return True
            else:
                print("COMPOSITE")
                print(lower, "is a composite number. ")
        else:
            print("Testing... ")
            primes, composites = program_test(lower, upper)
    
        print("Done! ")
        print("Tested numbers between", lower, "-", str(upper) + ". ")
        print("Found", primes, "primes and", composites, "composites. ")
        return True

        
    elif inp == "n":
        n = input("Please enter an integer: ")
        if n[0] == "-":
            n = n[1::]
            was_negative = True
        n = int(n)
    else:
        print("Input not recognized.  Goodbye.  ")
        return


    if prime_loop(n):
        print("PRIME")
        if was_negative:
            n = "-" + str(n)
        print(n, "is a prime number. ")
        return True
    else:
        print("COMPOSITE")
        if was_negative:
            n = "-" + str(n)
        print(n, "is a composite number. ")
        return False


main()

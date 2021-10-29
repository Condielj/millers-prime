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

    e = n - 1
    b = random.randint(2, e)

    is_prime = False

    if n == 2:
        is_prime = True

    elif n % 2 == 0:
        is_prime = False

    elif pow(b, e, n) == 1:
        is_prime = True

    return is_prime


def prime_loop(n):
    is_prime = True
    for i in range(20):
        passed = prime_test(n)
        if not passed:
            is_prime = False
    return is_prime


def main():
    was_negative = False
    print("Welcome to the prime number tester. ")
    print("Choose one of the following selections: ")
    print("Test Sample Numbers:")
    print("(a, b, c) = Large prime numbers. (d, e, f) = Small prime numbers. ")
    print("(t, u, v) = Large composite numbers.  (x, y, z) = Small composite numbers. ")
    print("(n) = Enter own integer. ")
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

    elif inp == "n":
        n = input("Please enter an integer: ")
        if n[0] == "-":
            n = n[1::]
            was_negative = True
        n = int(n)
    else:
        print("Input not recognized.  Goodbye.  ")

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

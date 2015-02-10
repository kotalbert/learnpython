def is_prime(x):
    if x > 2:
        #Prime finding algorithm
        n = x
        while n > 2:
            n -= 1
            if x%n == 0:
                return False
                break
        else:
            return True
    else:
        if x == 2:
            return True
        else:
            return False

#testing function
    
rng = range(0,10)
for n in rng:
    print "Testing: %d" %n, "is prime: ", is_prime(n)
    

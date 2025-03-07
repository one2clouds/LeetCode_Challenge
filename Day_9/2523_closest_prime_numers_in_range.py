import math.sqrt as sqrt
def closest_Primes(left, right):

    def get_primes():
        is_prime = [True] * (right+1)
        is_prime[0] = is_prime[1] = False

        for n in range(2, int(sqrt(right))+1):
            if not is_prime[n]:
                continue
            for m in range(n+n, right+1, n):
                is_prime[m] = False

        primes = []

        for i in range(len(is_prime)):
            if is_prime[i] and i>=left:
                primes.append(i)
        return primes
        
    primes = get_primes()

    res = [-1, -1]
    difference = right - left + 1
    for i in range(len(primes)):
        if primes[i] - primes[i-1] < diff:
            diff = primes[i] - primes[i-1]
            res = [primes[i-1], primes[i]]

    return res 



if __name__=="__main__":
    nums = [1,2,3]
    print(closest_Primes(left=10, right=10))

import math
num_range = int(input('range? '))
def find_primes(num_range):
    final = []
    for num in range(2, num_range+1):
        factors = []
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                factors.append(i)
            else:
                continue
        '''for x in range(0, len(factors)):
            factors.append(num/factors[x])
        factors.sort()'''
        if len(factors) == 0:
            final.append(num)
        else:
            continue
    print final
    return len(final)
print(find_primes(num_range))

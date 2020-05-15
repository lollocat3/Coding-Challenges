import math
numbers = int(input('how many numbers?'))
num_list = []
for i in range(2, numbers+1):
    num_list.append(i)
def primes(array):
    copy = array[::]
    temp = []
    #print array
    for j in range(0, len(copy)):
        for k in range(1, numbers/2+1):
            x = copy[j]*k
            #print x
            #print x
            temp.append(x)
        #print temp
        for o in range(1, len(temp)):
            if temp[o] in array:
                array.remove(temp[o])
        #array.insert(0, temp[0])
        #print array
        #print temp
        del temp[:]
        #print copy[j]
    print 'there are ' + str(len(array))+ ' primes between 2 and ' + str(numbers)
    print 'here they are: '
    print array

primes(num_list)

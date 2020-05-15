import math
import numpy as np
def digit_finder(num, index): 
        return ((num%10**index)-(num%(10**(index-1))))/(10**(index -1))
def isPalindrome(x):
    if x < 0:
        return False
    for i in range(int(math.floor(len(str(int(x)))/2))): 
        if int(digit_finder(x, i+1)) ==int(digit_finder(x, len(str(x))-i)): 
            continue 
        else: 
            return False 
    return True 

if __name__ == '__main__':
	while True:
		num = int(input('input: '))
		if num == 0:
			break
		print(isPalindrome(num))
		
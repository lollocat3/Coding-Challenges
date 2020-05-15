def reverse(x):
    num = []
    final = 0
    neg = False
    if x < 0:
    	x*=-1
    	neg = True
    for i in range(len(str(x))):
        digit = ((x)%(10**(i+1))-(x)%(10**(i)))/(10**i)
        num.append(digit)
    print(num)
    for j in range(len(str(x))):
    	final+=num[j]*10**(int(len(str(x))-(j+1)))
    if neg == True:
    	final *= -1
    if final > 2**31-1 or final < -2**31:
    	final = 0

    return int(final)


print(reverse(388983832892589))
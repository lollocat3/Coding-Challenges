def num_finder(string):
	lis = list(string)
	for i in range(len(lis)):
		if lis[i] != ' ':
			lis = lis[i:]
			break
	for j in range(len(lis)):
		if not lis[j].isdigit() and not lis[j] == '-' :
			lis = lis[:j]
			break
	final_str = ''
	for k in range(len(lis)):
		final_str = final_str+lis[k]
	if final_str == '':
		final = int('0')
	else:
		final = int(final_str)
	if final > 2**31-1:
		return 2**31-1
	elif final < -2**(31):
		return -2**(31)
	return final

print(num_finder('823841732987'))
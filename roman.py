def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    num_list = list(s)
    final = 0
    i = 0
    while i <= len(num_list)-1:
        num = num_list[i]
        if num == 'I':
            if i == len(num_list)-1:
                final+= 1
                i+=1
            elif num_list[i+1] == 'V':
                final+=4
                i+=2
            elif num_list[i+1] == 'X':
                final+=9
                i+=2
            else:
                final += 1
                i+=1
        elif num == 'V':
            final += 5
            i+=1
        elif num == 'X':
            if i == len(num_list)-1:
                final+= 10
                i+=1
            elif num_list[i+1] == 'L':
                final+=40
                i+=2
            elif num_list[i+1] == 'C':
                final+=90
                i+=2
            else:
                final+= 10
                i+=1
        elif num == 'L':
            final += 50
            i+=1
        elif num == 'C':
            if i == len(num_list)-1:
                final+= 100
                i+=1
            elif num_list[i+1] == 'D':
                final+=400
                i+=2
            elif num_list[i+1] == 'M':
                final+=900
                i+=2
            else:
                final += 100
                i+=1
        elif num == 'D':
            final += 500
            i+=1
        elif num == 'M':
            final+= 1000
            i+=1
    print(s+' = '+ str(final))
    return final

romanToInt('X')
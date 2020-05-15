from tqdm import tqdm
import time
def twoSum(array, target, index = None):
    final = []
    for i in range(len(array)):
        for j in range(len(array)-1-i): 
                if i != index and i+j+1 != index:
                    if array[i]+array[i+j+1] == target: 
                        final.append([array[i], array[i+j+1]])
    return final   
            

def all_triples(num_terms): 
    array = [i for i in range(num_terms)] 
    perms = [] 
    for i in range(num_terms): 
        for j in range(num_terms): 
            for k in range(num_terms): 
                if i != j and i != k and j !=  k:  
                    perms.append([i, j, k]) 
    for l in range(len(perms)): 
        for k in range(len(perms)): 
            if l != k: 
                if sorted(perms[l]) == sorted(perms[k]): 
                    perms[k] = ['l'] 
    perms = list(filter((['l']).__ne__, perms)) 
    return perms 

def threeSum(array):
    target = 0
    perms = all_triples(len(array)) 
    final = [] 
    for i in range(len(perms)): 
        for j in range(len(perms)): 
            if i != j or len(perms)== 1: 
                if (array[perms[i][0]]+array[perms[i][1]]+array[perms[i][2]]) ==target: 
                    final.append([array[perms[i][0]],array[perms[i][1]],array[perms[i][2]]])     
                
    for k in range(len(final)): 
        for z in range(len(final)): 
            if k!=z: 
                if sorted(final[k]) == sorted(final[z]): 
                    final[z] =['l'] 
    final = list(filter((['l']).__ne__, final)) 
    return final

def fast_3sum(array):
    final = []
    for i in tqdm(range(len(array))):
        matches = twoSum(array, -array[i], i)
        for element in matches:
            element.append(array[i])
            final.append(sorted(element))
    cleanlist= []
    [cleanlist.append(x) for x in final if x not in cleanlist]
    return cleanlist



if __name__ == '__main__':
    array = [-4,-5,-6,3,11,-13,3,14,1,-10,11,6,8,9,-6,-9,6,3,-15,-8,0,5,6,-8,14,-11,0,2,14,-15,14,-13,-5,-15,5,13,-13,-6,13,-4,-1,1,-13,14,-13,-12,-10,9,6,12,8,14,-5,-8,-9,-6,-4,-2,3,-5,-2,-6,-2,1,-5,-12,-1,-11,-11,-11,0,-4,-2,-5,-5,0,-2,-7,-14,-10,-10,10,-11,-8,-13,-13,1,-2,-7,11,8,6,-9,-9,14,1,-13,-9,-3,-9,-5,13,2,8,-7,13,-14,6,-9,-13,3,-12]
    #print(threeSum(array))
    print(fast_3sum(array))
    
    #print(threeSum(array))
    #print(twoSum(array, 3, 0))
    #print(fast_3sum(array))
        

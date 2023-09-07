#Diego Lopez basics

def isPalindrome(n):

     string = str(n)
    
    # Check if the string is equal to its reverse
     return string == string[::-1]


def nthmax(n, a):

    if n >= len(a) or n < 0:
        return None
    
    sorted(a)   #sort the array

    return a[n]   #return the nth index number
        

def freq(s):
 
    max = {} 

    largest = 0

    most_freq = ""

    if s == "" :  #checks if string is empty

        return ""
    
    else :

        for letter in s:

            if letter not in max :

                max[letter] = 0

            max[letter] += 1 

    for let1 in max :

        if largest < max[let1] :

            largest = max[let1]
            most_freq = letter


    return most_freq


def zipHash(arr1, arr2):

    map1 = {}

    if len(arr1) != len(arr2):
        return None
    
    else:

        for i in len(arr1):

            map1[arr1[i]] = arr2[i]

    
    return map1


def hashToArray(hash): 

    list1 = []

    if len(hash) == 0 :
        return list1 
    
    else :

        i = 0
        
        for keys in hash:
            
            list1.append(keys)

            list1[i] = hash[keys]

            i += 1
        
    return list1


def maxLambdaChain(init, lambdas):
    
    result = init

    for num in lambdas:
        result = max(result, num(result))

    return result








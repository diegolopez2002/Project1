#Diego Lopez basics

def isPalindrome(n):

     string = str(n)
    
    # Check if the string is equal to its reverse
     return string == string[::-1]


def nthmax(n, a):

    sortedarray = sorted(a, reverse=True)

    if n < len(sortedarray):
        return sortedarray
    else:
        None



def freq(s):
     maxletter = {}

     count = 0

     mostfreq = ""

     for letter in s:
          if letter not in maxletter:
               maxletter[letter] = 1

          else:

               maxletter[letter] += 1

        
          if maxletter[letter] > count:
               count = maxletter[letter]
               mostfreq = letter 
               
     
     return mostfreq
     
 

def zipHash(arr1, arr2):

    map1 = {}

    if len(arr1) != len(arr2):
        return None
    
    else:

        for i in range(len(arr1)):

            map1[arr1[i]] = arr2[i]
             
    return map1


def hashToArray(hash): 
     
     array = []
     for key in hash.keys():
          array.append([key, hash[key])

     return array
          

def maxLambdaChain(init, lambdas):
    
    result = init

    for num in lambdas:
        result = max(result, num(result))

    return result








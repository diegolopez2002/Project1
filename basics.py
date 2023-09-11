
def isPalindrome(n):

     string = str(n)
    
    # Check if the string is equal to its reverse
     return string == string[::-1]

def nthmax(n, a):

     if n < 0:
          return None

     array = []
     for item in a:
          if item not in array:
               array.append(item)

     sorted_unique = sorted(array, reverse=True)

     if n < len(sorted_unique):
          return sorted_unique[n]
     else:
          return None


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

     result = {} #initalize dictionary
     
     if len(arr1) != len(arr2):
          return None

     if len(arr1) == 0 or len(arr2) == 0:
          return result


     for i in range(len(length)): 
          
          if arr1[i] is None or arr2[i] is None:
            return None
               
          result[arr1[i]] = arr2[i] #assign to dictionary

     return result


def hashToArray(hash): 

     if hash is None:
          return None

     result = []
     for key in hash.keys():
          result.append([key, hash[key]])
     return result


def maxLambdaChain(init, lambdas):

     if not lambdas: # return init if lambdas is empty
          return init

     result = init 
     
     for num in lambdas:
          if num is None or not callable(num):
               continue

          result = max(init, num(result))

     return result




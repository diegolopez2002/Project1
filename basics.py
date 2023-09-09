
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

     sorted_unique = sorted(unique_elements, reverse=True)

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

     if len(arr1) != len(arr2):
          return None
    
     result = {}
     for i in range(len(arr1)):
          result[arr1[i]] = arr2[i]

     return result


def hashToArray(hash): 

     result = []
     for key in hash.keys():
          result.append([key, hash[key]])
     return result


def maxLambdaChain(init, lambdas):
    
     result = init

     for num in lambdas:
          result = max(result, num(result))

     return result




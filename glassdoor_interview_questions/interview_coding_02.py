import collections

def learningDictionary():
    ages = {'julian': 20, 'bob': 23, 'zack': 3, 'anthony': 95, 'daniel': 41}
    # ages.items() will print out all of the dictionary items inside ages
    print("Printing each key value by looping through \'ages.items()\'")
    for i,j in ages.items():
        print("Name:{} Age:{}".format(i,j))

    # lambda function practices
    # lambda arguments : expression 
    # ( lambda arguments : expression )(arg_parameters)
    # i.e. (lambda x,y : x + y)(3,4)  = 7 will be returned
    print("\nInitializing and running add function:")
    add = lambda x,y : x + y
    print("Add Function:", add(3,4))
    print("Inline Multiply:",(lambda x,y:x*y)(8,8))

    # Let's break this down, x**2 == x^2
    print("\nUnderstanding what it means to sort by alternate key using function:")
    print(sorted(range(-5, 6), key=lambda x: x ** 2))
    # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    # [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25] <- alternate key applied for comparing
    # [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5] <- negative numbers show up earlier in the list
    # What happens here is that we take the exponent of it's value and then sort it, meaning -1 and +1 will be sorted equally via alternate key

    print("\nPrinting the dictionary using collections.Counter:")
    words = ["ii", "i", "leetcode", "i", "ii", "coding", "vanvan", "vanvan", "vanvan"]
    # This will count the occurrences and also sort the words in descending order
    count = collections.Counter(words)
    print(count) # {'vanvan': 3, 'ii': 2, 'i': 2, 'leetcode': 1, 'coding': 1}
    keyList = count.keys()
    print(keyList) # ['ii', 'i', 'leetcode', 'coding', 'vanvan'] 
    filterList = sorted(keyList, key=lambda w: (-count[w], w)) # iterable = ['coding', 'i', 'ii', 'leetcode', 'vanvan']
    # ['ii', 'i', 'leetcode', 'coding', 'vanvan']
    # [(-2, "ii"), (-2, "i"), (-1, "leetcode"), (-1, "coding"), (-3, "vanvan")]
    # ['vanvan', 'i', 'ii', 'coding', 'leetcode']
    # Sort increasing order using index 0 within tuple and by default, it will sort first, second, third, etc etc
    # https://stackoverflow.com/questions/644170/how-does-python-sort-a-list-of-tuples
    k = 2
    print(filterList[:k])
    # This will return the first two element per Python slicing syntax
    # start:stop:increment
    # start defaults to 0, so technically it's doing filterList[0:2]

    # sorted(iterable, key=None, reverse=False)
    # iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
    #   - This is the iterator of items you want to sort, i.e. dict_items([('julian', 20), ('bob', 23), ('zack', 3), ('anthony', 95), ('daniel', 41)])
    # key - A function that serves as a key for the sort comparison. Defaults to None
    # reverse - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided(ascending order).
    incSortAges = sorted(ages.items(), key=lambda x: x[0])
    # iterable - dict_items([('julian', 20), ('bob', 23), ('zack', 3), ('anthony', 95), ('daniel', 41)]
    # key - for each item, ('julian', 20), we will sort using the first item in the tuple aka x[0]
    # output == [('anthony', 95), ('bob', 23), ('daniel', 41), ('julian', 20), ('zack', 3)]

# https://www.w3schools.com/python/python_ref_set.asp
# Python set function
def learningSets():
    ht = set()
    people = {"Jay", "Idrish", "Archi", 1, 64} 

    for i in range(4):
        ht.add(i)

    print("ht:", ht)
    print("people:", people)
    print("Union:", ht|people)
    print("Intersection:", ht&people)
    print("Difference ht-people:", ht-people)
    print("Difference people-ht:", people-ht)

# Question: Given two strings, merge each letter into one string
# String A: bobo, String B: fire
# Output: bfoibroe
def mergeString(a,b):
    # to avoid index out of bound errors, let's merge based off of which string is smaller
    smallerStr = b
    biggerStr = a
    mergedStr = ""
    if len(a) < len(b):
        smallerStr = a
        biggerStr = b

    for i in range(0, len(smallerStr)):
        mergedStr = mergedStr + a[i] + b[i]
    
    return mergedStr + biggerStr[len(smallerStr):]

# Question: Find the first unique non repeating character in a string
# Examples:
# s = "leetcode"
# return l
# s = "loveleetcode"
# return v
def uniqueChar(str):
    someDict = {}
    for i in str:
        if i in someDict:
            someDict[i] = someDict[i] + 1
        else:
            someDict[i] = 1
    
    print("Populating Dictionary:", someDict)
    for (k,v) in someDict.items():
        if v == 1:
            return k

def uniqueCharIndex(str):
    someDict = collections.Counter(str)
    print("Populating Dictionary:", someDict)

    for i in range(0, len(str)):
        if someDict[str[i]] == 1:
            return i

    # Using enumerate, for list. It is also possible to enumerate over a dictionary
    # https://stackoverflow.com/questions/36244380/enumerate-for-dictionary-in-python
    # for (i,v) in enumerate(str):
    #     if someDict[v] == 1:
    #         return i

    return -1

# Find the K most element in a list.
# So like if k is 3, then print the most, 2nd most, and 3rd most
# someList = [4,4,4,60,1,1,1,20,20], k=2
def kMostElement(someList, k):
    someDict = {}
    for i in someList:
        if i not in someDict:
            someDict[i] = 1
        else:
            someDict[i] = someDict[i]+1

    someList = []
    for ky,v in sorted(someDict.items(), key=lambda x:x[1] ,reverse=True):
        if k > 0:
            someList.append(ky)
        k = k - 1

    return someList


if __name__ == '__main__':
    #learningDictionary()
    learningSets()
    # Test cases for uniqueChar func
    #print("The unique char 'loveleetcode':", uniqueChar('loveleetcode'))
    #print("The unique char 'leetcode':", uniqueChar('leetcode'))
    # Test cases for uniqueCharIndex func
    #print("The unique char index 'loveleetcode':", uniqueCharIndex('loveleetcode'))
    # Test cases for mergeString func
    print("The merged string for bobo and fire is:",mergeString("bobo","fire"))
    print("The merged string for bobo and fire is:",mergeString("bobo","fireooooo"))
    print("The 2nd most element for [4,4,4,60,1,1,1,20,20] is:",kMostElement([4,4,4,60,1,1,1,20,20],2))
# Find the K most element in a list.
# So like if k is 3, then print the most, 2nd most, and 3rd most
def kMostElement(someList, k):
    someDict = {}
    outList = []

    for i in someList:
        if i in someDict:
            someDict[i] = someDict[i] + 1
        else:
            someDict[i] = 1

    print(someDict)

    for j in sorted(someDict.items(), key=lambda x: x[1], reverse=True):
        if k != 0:
            outList.append(j[0])
            k = k - 1

    print("Output List:",outList)

# When you run your script, the __name__ variable equals __main__. 
# When you import the containing script, it will contain the name of the script.
if __name__ == '__main__':
    # Output = if k = 2: [a, d] 
    arr = ['a','a','a','a','b','b','c','d','d','d',]
    kMostElement(arr, 2)
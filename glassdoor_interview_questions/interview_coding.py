import os

# Question: Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
def FizzBuzz (num):
    # error handling for negative words and over 100 (if this is considered an error)
    if (num <= 0 or num > 100):
        print("This value is invalid.")
        # this will return None value in the background
        return

    # range(n) generates an iterator to progress the integer numbers starting with 0 and ending with (n -1)
    for i in range(1, num + 1):
        # The % (modulo) operator yields the remainder from the division of the first argument by the second.
        # Thus, if the remainder is 0, we know the value is multiples of both 3 and 5     
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            # Using continue passes for the next iteration of the for loop
            # Using pass just does nothing
            print(i)


# Using recursion, to traverse a directory until I can find files which contains a specific keyword and returns~
# Recursion is made for solving problems that can be broken down into smaller, repetitive problems. 
# It is especially good for working on things that have many possible branches and are too complex for an iterative approach.
# So let’s go back to the factorial call stack image from above. Every time we add a new call to the stack, 
# we are increasing the amount of memory that we are using. If we are analyzing the algorithm using Big O notation, 
# then we might note that this increases our SPACE complexity.
def FindFilesRecursion (path, keyword):

    for entry in os.listdir(path):
        # Check to see if the entry is a file, else call the recursion
        if os.path.isfile(os.path.join(path,entry)):
            SearchFile(os.path.join(path,entry), entry, keyword)
        else:
            FindFilesRecursion(os.path.join(path,entry), keyword)

fileList = []
# with statement In addition, it will automatically close the file. The with statement provides
# a way for ensuring that a clean-up is always used.
def SearchFile (full_path, file, keyword):
    # Open the file in read only mode, will automatically close file
    with open(full_path, 'r') as readObj:
        for line in readObj:
            if keyword in line:
                fileList.append(file)
                return
            
# With the iterative approach, we can make use of os.walk(path, topdown=True)
# for every directory within a path, it will yield a three tuple-result, otherwise, it yields nothing
def FindFilesIter (path, keyword):

    for root, subdir, files in os.walk(path, topdown=True):
        for file in files:
            SearchFile(os.path.join(root,file), file, keyword)

# When you run your script, the __name__ variable equals __main__. 
# When you import the containing script, it will contain the name of the script.
if __name__ == '__main__':
    # FizzBuzz(101)
    # FindFilesRecur('/Users/bryan/Documents/Personal/Site-Reliability-Cloud-Learning/glassdoor_interview_questions/', 'Site')
    FindFilesIter('/Users/bryan/Documents/Personal/Site-Reliability-Cloud-Learning/glassdoor_interview_questions/', 'FizzBuzz')
    print(fileList)

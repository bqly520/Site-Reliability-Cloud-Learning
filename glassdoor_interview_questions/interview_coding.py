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
        print(i)
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            # Using continue passes for the next iteration of the for loop
            # Using pass just does nothing
            pass

# When you run your script, the __name__ variable equals __main__. 
# When you import the containing script, it will contain the name of the script.
if __name__ == '__main__':
    FizzBuzz(101)
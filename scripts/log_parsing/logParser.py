import re
# Playing around with re.findall method first
# re.findall() module is used when you want to iterate over the lines of the file, it will return a list of all the matches in a single step.
timestamp = []
numMessages = []
def extractDates(file):
    with open(file, "r") as readObj:
        count = 0
        for line in readObj:
            # Will return an array of all of the matches with date format, 2012-02-03 20:11:35
            # arrayMatch = re.findall('^\d{4}-\d{2}-\d{2}\s.....:\d{2}',line)

            # Will return an array of all of the matches AT the specified date, 2012-02-03 20:11:35
            # arrayMatch = re.findall('^2012-02-03 20:11:35',line)

            # System Log regex matching: Between Mar 21 17:00:00 to March 21 19:00:00
            # We are using an list for numMessages because integers are immutable
            arrayMatch = re.findall('Mar\s21\s1[78]', line)
            if(len(arrayMatch)):
                timestamp.append(line)
                count = count + 1
        numMessages.append(count)



if __name__ == '__main__':
    extractDates( "/var/log/system.log" )
    print("Number of messages within time frame: " + str(numMessages[0]))
    #for i in timestamp:
    #    print(i)
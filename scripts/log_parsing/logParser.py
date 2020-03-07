def printFile(file):
    f = open(file, "r")
    print(f.read())
    f.close()

def extractDates(file):
    f = open(file, "r")
    for x in f:
        print(x)
    f.close()

if __name__ == '__main__':
    extractDates( "sample.log" )
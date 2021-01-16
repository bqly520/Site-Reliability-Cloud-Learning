class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.recents = []

    def update_recents(self, key: int) -> None:
        if key in self.recents:
            self.recents.remove(key)
        self.recents.insert(0, key)

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_recents(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if self.capacity <= len(self.cache) and key not in self.cache:
            del self.cache[self.recents.pop()]
        self.cache[key] = value
        self.update_recents(key)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# https://www.askpython.com/python/oops/python-class-constructor-init-function
# The object class is the base of all the classes in Python.
# https://www.programiz.com/python-programming/file-operation
class someBobo(object):

    def __init__(self):
        pass

    def splitEqualArray(self, arr):
        size = len(arr)
        if size < 2: return -1

        for i in range(1,size):
            if sum(arr[0:i]) == sum(arr[i:size]):
                return i

        # returns -1 if there is no equal split
        return -1

    # Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
    # Where g = 9.8 m/s^2 (gravitational constant)
    # Write a program to read in the data files from disk, it must then print the NAMES of only the bipedal dinosaurs from fastest to slowest.
    def csvDinosaurs(self, ds1, ds2):
        # {dinosaur:(stride_length,stance)}
        # since we only care about bipedal dinosaurs, only put bipedal dinosaurs in dictionary
        someDict2 = {}
        with open('sample_data/'+ ds2,'r') as f2:
            for line in f2:
                #print(line, end='') since excel file has newline, set end to ''(empty), default is \n
                # assuming all dinosaurs are unique
                line = line.replace('\n','')
                arr2 = line.split(',')
                if arr2[2] == 'bipedal':
                    someDict2[arr2[0]] = (arr2[1],arr2[2])

        # {dinosaur:(leg_length,diet)}
        someDict1 = {}
        with open('sample_data/'+ ds1,'r') as f1:
            for line in f1:
                #print(line, end='') since excel file has newline, set end to ''(empty), default is \n
                # assuming all dinosaurs are unique
                line = line.replace('\n','')
                arr1 = line.split(',')
                if arr1[0] in someDict2:
                    someDict1[arr1[0]] = (arr1[1],arr1[2])
        
        resultList = []
        for dino in someDict2.keys():
            # assuming there may be some mismatches in sample data
            if dino in someDict1:
                speed = ((float(someDict2[dino][0])/float(someDict1[dino][0]))-1)*((float(someDict1[dino][0])*9.8)**0.5)
                resultList.append((dino,speed))
        
        for dinoNuggets,num in sorted(resultList, key=lambda x:x[1], reverse=True):
            print(dinoNuggets)

    # return the minimum time spread which I assume is max_temp-min_temp... probably wrong :p
    # goal: print the order of days according to minimum time spread
    def minTempSpread(self, file):
        someDict = {}
        with open('sample_data/'+file,'r') as f:
            for line in f:
                line = line.replace('\n','')
                row = line.split(',')
                if row[1].isdigit():
                    timeDiff = int(row[1])-int(row[2])
                    someDict[row[0]] = timeDiff
        
        for day,t in sorted(someDict.items(),key=lambda x:x[1]):
            print(day)



if __name__ == '__main__':
    obj = someBobo()
    #print("Running Split Equal array Func")
    #print('index:',obj.splitEqualArray([1,3,4,6,14]))
    #obj.csvDinosaurs("fb_dataset1.csv","fb_dataset2.csv")
    obj.minTempSpread('weather.csv')
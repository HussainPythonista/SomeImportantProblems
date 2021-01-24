class HashTable:
    def __init__(self):
        self.Max=10
        self.array=[0 for i in range(10)]

    def getHash(self,date):
        h=0#For adding the ordered value
        for i in date:
            h+=ord(i)#for calculating the ASCII Value
        place=h%self.Max #10 is size of memory location
        self.array[place]=99
hash=HashTable()
hash.getHash("march 6")
print(hash.array)

    
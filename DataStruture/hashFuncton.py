class HashTable:
    def __init__(self):
        self.Max=10
        self.array=[0 for i in range(10)]

    def getHash(self,element):
        h=0#For adding the ordered value
        for i in element:
            h+=ord(i)#for calculating the ASCII Value
        place=h%self.Max #10 is size of memory location
        return place
    def push(self,key,value):
        hash=self.getHash(key)

        self.array[hash]=value

hash=HashTable()
hash.push("march 6",99)
print(hash.array)

    